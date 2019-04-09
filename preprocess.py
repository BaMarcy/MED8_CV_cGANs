# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 04:34:23 2019

@author: balogh
"""
import os.path
import cv2
import glob
import os

def processing(hist):
    files = glob.glob("data/depth\\*")
    filenumber = 0
    for f in files:
        #Open image
        frame = cv2.imread(f)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if(hist == "2"):
            output = cv2.equalizeHist(gray)
            print("hist equalization")
        elif(hist == "3"):
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
            output = clahe.apply(gray)
            print("contrast limiting adaptive histogram equalization")
        else:
            output = frame
            print("none")
        try:
            #Write image
            cv2.imwrite(dataset+"\\%s.jpg" %(filenumber), output)
            
            print("\\%s.jpg" %(filenumber))
            filenumber += 1 #Increment image number
        except:
            #If error, pass file 
            pass 

#Create the dataset folder and sub-folders
print("Name the dataset folder:")
dataset = text = input("")
print("hist equalization(1=none, 2=hist equalization, 3=contrast limiting adaptive histogram equalization):")
hist = text = input("")
if not os.path.exists(dataset):
    os.makedirs(dataset)  

processing(hist) #Call function