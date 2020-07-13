#!/usr/bin/env python3
    #Iterate through each file in the folder
    #For each file:
    #   Rotate the image 90 clockwise
    #    Resize the image from 192x192 to 128x128
    #    Save the image to a new folder in .jpeg format

import os
from PIL import Image
src = os.getcwd()+"/images/"
dest = os.getcwd()+"/opt/icons/"
#directory = os.fsencode(src)
for file in os.listdir(src):
    im = Image.open(src+file).convert('RGB')
    im = im.rotate(270)
    im = im.resize((128,128))
    outfile = os.path.basename(file)
    #print(dest + outfile)
    im.save(dest + outfile, "JPEG")
