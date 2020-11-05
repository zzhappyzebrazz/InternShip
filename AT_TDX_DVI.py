# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:07:24 2020

@author: minhhala
"""
import os
import shutil
import csv
import numpy as np
import pandas as pd

Image_Folder = 'source folder directory to saved images'
# Server1 = "server1"
# Server2 = "server2"

#read file csv
df = pd.read_csv(r'read the csv file')
Lot_List = list(set(df['lot']))
#read file csv to df var
#creatr Lot_List = 


#create lot list folder
i=0

if not os.path.isdir(Image_Folder):# check path exist or not
    os.mkdir(Image_Folder)# create the path if not return FileExistsError
    print("No Folder Create Folder")
else:
    shutil.rmtree(Image_Folder)#remove entire directory tree path given
    print("Have Folder RM Folder")
    os.mkdir(Image_Folder)#tao path Image_folder
    print("Create Folder")

#copy image to lot
i=0
j=0
for row in Lot_List:
    temp_table = df[df['lot']==Lot_List[i]]
    Server_directory = list(temp_table['image_full_path']) # list of Pic
    # Server2_directory = list(Server2 + temp_table['directory'])
    old_name=list(temp_table['image_name'])
    new_name=list(temp_table['image_rename'])
    for row1 in Server_directory:
        try:
            shutil.copy2(Server_directory[j],Image_Folder)
            print("Copy Success")
            Temp_name = Image_Folder
            os.rename(os.path.join(Temp_name,old_name[j]),os.path.join(Temp_name,new_name[j]))
            print("Rename Success")
        except EnvironmentError:
            # try:
            #     print('Try Server 2')
            #     shutil.copy2(Server2_directory[j],Image_Folder)
            #     print("Success")
            #     Temp_name = Image_Folder
            #     os.rename(os.path.join(Temp_name,old_name[j]),os.path.join(Temp_name,new_name[j]))          
            # except EnvironmentError:
            print("error")
        j=j+1 # next pic
    i=i+1
    j=0
