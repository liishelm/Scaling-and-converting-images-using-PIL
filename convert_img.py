#!/usr/bin/env python3

from PIL import Image
import os
directory = 'images/'
new_directory = '/opt/icons/'
for file in os.listdir(directory):
  f = os.path.join(directory, file)
  if '.DS_Store'  not in f:
    with Image.open(f) as img:
     img = img.convert('RGB')
     img = img.rotate(-90)
     img = img.resize((128,128))
     img.save(os.path.join(new_directory, file + '.jpeg'))

