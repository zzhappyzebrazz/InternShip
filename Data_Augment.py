# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:54:39 2020

@author: minhhala
"""

import os
import os.path
import shutil
from PIL import Image
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt
import cv2

#find source path and dest path, list every items in the source path
src_path = r'source path'
dest_path = r'destination path'
names = os.listdir(src_path)
print(names[0])
print(os.path.join(src_path, names[3]))
#brightness adjust
#for loop to loop through all the image in the directory
for x in range(0, len(names)):
    #load image and reformat the image
    img = load_img(os.path.join(src_path, names[x]))
    img1 = img_to_array(img)
    data = expand_dims(img1, 0)
    #change the brightness of the image in range og 0.5 to 2.0
    brightness = ImageDataGenerator(brightness_range=[0.5, 2.0])
    #each time generate 1 , batch size  = 1
    bright_gen = brightness.flow(data, batch_size = 1)
    #loop 9 times each time create an image
    for y in range(33):
        print("Before saving image:")   
        print(os.listdir(dest_path))   
        #run image generator
        myBatch = bright_gen.next()
        image = myBatch[0].astype('uint8')
        #change directory to the destination path
        os.chdir(dest_path)
        #convert y from int to str for naming
        count = str(y)
        #rename
        cv2.imwrite( "Bright_adjust_" + count + "_" + names[x], image)
        #print the image saved
        print("After saving bright adjust image:")   
        print(os.listdir(dest_path)) 
        
#flip image data generator 
for x in range(0, len(names)):
    #load image and refomat the image
    img = load_img(os.path.join(src_path, names[x]))
    img1 = img_to_array(img)
    data = expand_dims(img1, 0)
    #flip image 
    flip = ImageDataGenerator(horizontal_flip=True, vertical_flip=True)
    flip_gen = flip.flow(data, batch_size = 1)
    #loop 9 times each time create an image
    for y in range(33):
        # print("Before saving image:")   
        # print(os.listdir(dest_path))   
        #run image generator
        myBatch = flip_gen.next()
        image = myBatch[0].astype('uint8')
        os.chdir(dest_path)
        count = str(y)
        #rename
        cv2.imwrite( "Flip_adjust_" + count + "_" + names[x], image)
        #print the image saved
        print("After saving image:")   
        print(os.listdir(dest_path)) 
        
#rotation image data generator 
for x in range(0, len(names)):
    #load image and refomat the image
    img = load_img(os.path.join(src_path, names[x]))
    img1 = img_to_array(img)
    data = expand_dims(img1, 0)
    #rotation image 45 degree
    rotation = ImageDataGenerator(rotation_range=45)
    rot_gen = rotation.flow(data, batch_size = 1)
    #loop 9 times each time create an image
    for y in range(33):
        # print("Before saving image:")   
        # print(os.listdir(dest_path))   
        #run image generator
        myBatch = rot_gen.next()
        image = myBatch[0].astype('uint8')
        os.chdir(dest_path)
        count = str(y)
        #rename
        cv2.imwrite( "Rotation_adjust_" + count + "_" + names[x], image)
        #print the image saved
        print("After saving image:")   
        print(os.listdir(dest_path)) 
        
#Shear image data generator        
for x in range(0, len(names)):
    #load image and refomat the image
    img = load_img(os.path.join(src_path, names[x]))
    img1 = img_to_array(img)
    data = expand_dims(img1, 0)
    #shear image max 45 degree
    shear = ImageDataGenerator(shear_range=45)
    shear_gen = shear.flow(data, batch_size = 1)
    #loop 9 times each time create an image
    for y in range(33):
        # print("Before saving image:")   
        # print(os.listdir(dest_path))   
        #run image generator
        myBatch = shear_gen.next()
        image = myBatch[0].astype('uint8')
        os.chdir(dest_path)
        count = str(y)
        #rename
        cv2.imwrite( "Shear_adjust_" + count + "_" + names[x], image)
        #print the image saved
        print("After saving image:")   
        print(os.listdir(dest_path)) 
 
        
#shift image data generator 
for x in range(0, len(names)):
    #load image and refomat the image
    img = load_img(os.path.join(src_path, names[x]))
    img1 = img_to_array(img)
    data = expand_dims(img1, 0)
    #shift image from -150px to +150px
    shift = ImageDataGenerator(width_shift_range=[-150,150])
    shift_gen = shift.flow(data, batch_size = 1)
    #loop 9 times each time create an image
    for y in range(33):
        # print("Before saving image:")   
        # print(os.listdir(dest_path))   
        #run image generator
        myBatch = shift_gen.next()
        image = myBatch[0].astype('uint8')
        os.chdir(dest_path)
        count = str(y)
        #rename
        cv2.imwrite( "Shift_adjust_" + count + "_" + names[x], image)
        #print the image saved
        print("After saving image:")   
        print(os.listdir(dest_path)) 
                
        
#zoom image data generator 
for x in range(0,len(names)):
    #load image and refomat the image
    img = load_img(os.path.join(src_path, names[x]))
    img1 = img_to_array(img)
    data = expand_dims(img1, 0)
    #zoom image from 0.5x to 2.0x
    zoom = ImageDataGenerator(zoom_range=[0.5,2.0])
    zoom_gen = zoom.flow(data, batch_size = 1)
    #loop 9 times each time create an image
    for y in range(33):
        # print("Before saving image:")   
        # print(os.listdir(dest_path))   
        #run image generator
        myBatch = zoom_gen.next()
        image = myBatch[0].astype('uint8')
        os.chdir(dest_path)
        count = str(y)
        #rename
        cv2.imwrite( "Zoom_adjust_" + count + "_" + names[x], image)
        #print the image saved
        print("After saving image:")   
        print(os.listdir(dest_path)) 
                        
# # brightness adjust from 0.5 to 2
# brightness = ImageDataGenerator(brightness_range=[0.5, 2.0])
# bright_gen = brightness.flow(data, batch_size = 1)

# #flip image 
# flip = ImageDataGenerator(horizontal_flip=True, vertical_flip=True)
# flip_gen = flip.flow(data, batch_size = 1)

# #rotation image 45 degree
# rotation = ImageDataGenerator(rotation_range=45)
# rot_gen = rotation.flow(data, batch_size = 1)

# #shear image max 45 degree
# shear = ImageDataGenerator(shear_range=45)
# shear_gen = shear.flow(data, batch_size = 1)

# #shift image from -150px to +150px
# shift = ImageDataGenerator(width_shift_range=[-150,150])
# shift_gen = shift.flow(data, batch_size = 1)

# #zoom image from 0.5x to 2.0x
# zoom = ImageDataGenerator(zoom_range=[0.5,2.0])
# zoom_gen = zoom.flow(data, batch_size = 1)

# 1007\MI03\SI-SUB-B-BODY3 batch size =2 183x6x2
#7596\MI03\SI-SUB-B-BODY3 batchsize = 9 23x6x9
#7596\MI03\SI-SUB-B-LSC batchsize = 3 139x6x3
