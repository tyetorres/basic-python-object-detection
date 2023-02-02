import os

import keras.models
import numpy as np
from keras.utils import load_img, img_to_array

resource_dir = 'resources/images/'
first_dir = resource_dir + "bicycle/"
second_dir = resource_dir + "motorbike/"
target_size = (256, 256)
bike_images = []
motorbike_images = []
for image in os.listdir(first_dir):
    bike_images.append(img_to_array(load_img(first_dir + image, target_size=target_size, color_mode='grayscale')))

for image in os.listdir(second_dir):
    motorbike_images.append(img_to_array(load_img(second_dir + image, target_size=target_size, color_mode='grayscale')))

image_array = np.concatenate([bike_images, motorbike_images])
model = keras.models.load_model('resources/ai_model')
bike_count = 0
motorbike_count = 0
image_count = 0
for image in image_array:
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    if prediction > 0.5:
        motorbike_count += 1
    else:
        bike_count += 1
    image_count += 1

print("Motorbikes Detected: " + str(motorbike_count))
print("Actual Motorbike Count: " + str(len(motorbike_images)))
print("Bikes Detected: " + str(bike_count))
print("Actual Bike Count: " + str(len(bike_images)))
