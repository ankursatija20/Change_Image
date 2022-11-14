#!/usr/bin/env python3
import os, sys
from PIL import Image
user = os.getenv('USER') # To get the username from environment variable
image_directory = '/home/{}/Change_Image/supplier_data/images/'.format(user)
#print(image_directory)
for image_name  in os.listdir(image_directory):
    if not image_name.startswith('.') and 'tiff' in image_name:
        image_path = image_directory + image_name
 #       print(image_path)
        path = os.path.splitext(image_path)[0]
  #      print(path)
        pathh = os.path.splitext(image_path)[1]
   #     print(pathh)
        im = Image.open(image_path)
        path = '{}.jpeg'.format(path)
        im.rotate(90).convert('RGB').resize((600, 400)).save(path, "JPEG")
        

