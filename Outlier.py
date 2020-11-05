# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 22:01:19 2020

@author: user
"""

import os
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import numpy as np
import pandas as pd

img = cv2.imread(r'D:\Pictures\img.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([30, 150, 50])
upper_red = np.array([255, 255, 180])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow('img.jpg', img)
cv2.imshow('res1.jpg', res)
cv2.waitKey(0)
plt.imshow(img)
plt.imshow(res)
# colourImg = Image.open(r'D:\Pictures\img.jpg')
# colourPixels = colourImg.convert("RGB")
# colourArray = np.array(colourPixels.getdata())

import seaborn as sns
# df = pd.DataFrame(colourArray, columns = ["red", 'green', "blue"])
# print(df.head())
# plt.hist(df)
# plt.show()

# print(df.shape)
# sns.boxplot(x = df['red'])
# sns.boxplot(x = df['green'])
# sns.boxplot(x = df['blue'])
# plt.hist(img)
# plt.show()
# imgB = img[:,:,0] = 0
# plt.hist(imgB)
# plt.show()
# plt.imshow(imgB)