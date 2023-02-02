import itertools
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator

dataset_path = "resources/images"

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = datagen.flow_from_directory(dataset_path,
                                              target_size=(256, 256),
                                              color_mode='grayscale',
                                              class_mode='binary',
                                              subset='training')
validation_generator = datagen.flow_from_directory(dataset_path,
                                                   target_size=(256, 256),
                                                   color_mode='grayscale',
                                                   class_mode='binary',
                                                   subset='validation')

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
train_generator = itertools.cycle(train_generator)
validation_generator = itertools.cycle(validation_generator)
model.fit(train_generator, steps_per_epoch=100, epochs=10, validation_data=validation_generator, validation_steps=50)

model.save("resources/ai_model")
