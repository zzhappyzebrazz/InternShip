# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 08:04:23 2020

@author: minhhala

test names list
['all test names are listed here for reference']
"""


import os
import os.path
import shutil
#declared directory
shared = 'shared directory folder to save images'
dest_path = r'local directory'
#read image names
names = os.listdir(shared)
#array with all the test name to sorted
folder_name = ['all the test names above']

#array to store test name folder
test_name = []
#for loop to check and create test name folder, and put in test_name array
for x in range(0, len(folder_name)):
        if not os.path.exists(os.path.join(dest_path, folder_name[x])):
            os.makedirs(os.path.join(dest_path, folder_name[x]))
        test_name.append(os.path.join(dest_path, folder_name[x]))    
                
print(test_name[2])    
print(names[1])     
print(len(names))
   
#for loop for the number of test names to sorted
for x in range(0, len(folder_name)):
    #for loop fo the images names to sorted 
    for y in range(0, len(names)):
        if folder_name[x] in names[y] and not os.path.exists(os.path.join(test_name[x], names[y])):
            shutil.copy(os.path.join(shared, names[y]), test_name[x])
            print('sorted', folder_name[x])
