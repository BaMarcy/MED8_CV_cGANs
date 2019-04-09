# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:45:07 2019

@author: balog
"""

import os.path
import cv2
import glob
import os

y = 20
h = 293

def processing(hist):
    files = glob.glob("results/\\*")
    filenumber = 0
    for f in files:
        #Open image
        img = cv2.imread(f)
        if(hist == "1"):
            crop_img = img[y:y+h, 325:581]
        else:
            crop_img = img[y:y+h, 622:878]
        try:
            #Write image
            cv2.imwrite(dataset+"\\%s.jpg" %(filenumber), crop_img)
            
            print("\\%s.jpg" %(filenumber))
            filenumber += 1 #Increment image number
        except:
            #If error, pass file 
            pass 

#Create the dataset folder and sub-folders
print("Name the dataset folder:")
dataset = text = input("")
print("hist equalization(1=crop ground truth, 2=crop generated image):")
hist = text = input("")
if not os.path.exists(dataset):
    os.makedirs(dataset)  

processing(hist) #Call function
