import os
from PIL import Image

path = "resources/images/sheep/"

for filename in os.listdir(path):
    if filename.endswith('.JPG') or filename.endswith('.png') or filename.endswith('.jpg') \
       or filename.endswith('.jpeg'):
        try:
            img = Image.open(path + filename)  # open the image file
            img.verify()  # verify that it is, in fact an image
        except:
            print(filename)
            os.remove(path + filename)
