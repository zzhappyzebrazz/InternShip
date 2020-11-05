# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 08:04:23 2020

@author: minhhala

test names list
['SI-SUB-B-BODY3',
 'SI-SUB-B-BODY2',
 'SI-SUB-B-FMDR',
 'SI-SUB-B-LSC',
 'SI-SUB-B-DMG',
 'SI-SUB-B-SCBR',
 'SI-SUB-B-BODY1',
 'SI-SUB-T-SCE',
 'SI-SUB-T-SCDK',
 'SI-SUB-T-FMDK',
 'SI-SUB-T-FM',
 'AL-DIE-T-VERHD1',
 'AL-SUB-T-FIDU2',
 'DATAMATRIX',
 'INVALID-BGA', 
 'REJECT-BGA',
 'SI-CMP-T-C0201S',
 'SI-DIE-T-BODY',
 'SI-DIE-T-RSDFU1',
 'SI-DIE-T-RTDFU1',
 'SI-DIE-T-RTRX1',
 'SI-SUB-B-BODY4',
 'SI-SUB-B-BODY5',
 'SI-SUB-E-BODY5',
 'SI-SUB-T-BODY1',
 'SI-SUB-T-BODY3'
 'SI-SUB-T-BODY5',
 'SI-XGA-B-LAND1',
 'SI-XGA-B-LAND2']
"""


import os
import os.path
import shutil
#declared directory
shared = '\\\\Vnatshfs.intel.com\\vnatanalysis$\\MAOATM\\VN\\Applications\\Finish\\Machine Learning\\CNP\\Image\\Reject\\'
dest_path = r'C:\Users\minhhala\Documents\Data\Data Science\Image Processing\CNP\script_test'
#read image names
names = os.listdir(shared)
#array with all the test name to sorted
folder_name = ['SI-SUB-B-BODY3','SI-SUB-B-BODY2' ,'SI-SUB-B-FMDR','SI-SUB-B-LSC', 'SI-SUB-B-DMG',
               'SI-SUB-B-SCBR', 'SI-SUB-B-BODY1', 'SI-SUB-T-SCE', 'SI-SUB-T-SCDK', 'SI-SUB-T-FMDK',
               'SI-SUB-T-FM', 'AL-DIE-T-VERHD1', 'AL-SUB-T-FIDU2', 'DATAMATRIX', 'INVALID-BGA', 
               'REJECT-BGA', 'SI-CMP-T-C0201S', 'SI-DIE-T-BODY', 'SI-DIE-T-RSDFU1', 'SI-DIE-T-RTDFU1',
               'SI-DIE-T-RTRX1', 'SI-SUB-B-BODY4', 'SI-SUB-B-BODY5', 'SI-SUB-E-BODY5', 'SI-SUB-T-BODY1',
               'SI-SUB-T-BODY3', 'SI-SUB-T-BODY5', 'SI-XGA-B-LAND1', 'SI-XGA-B-LAND2']

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