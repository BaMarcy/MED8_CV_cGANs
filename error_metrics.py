# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:23:54 2019

@author: balog
"""
import numpy as np
import os.path
import cv2
import glob
import os


def rmse(predictions, targets):
    differences = predictions - targets                       #the DIFFERENCEs.
    differences_squared = differences ** 2                    #the SQUAREs of ^
    mean_of_differences_squared = differences_squared.mean()  #the MEAN of ^
    rmse_val = np.sqrt(mean_of_differences_squared)           #ROOT of ^
    return rmse_val                                           #get the ^

def processing(path):
    a = []
    files = glob.glob(path + "\\*")
    for f in files:
        #Open image
        img = cv2.imread(f)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        a.append(gray)        
    return a
        

pred = processing("error/gen_c/") #Call function
target = processing("error/gt_c/") #Call function

total1 = []
total2 = []

total3 = []

n = 6

for i in range(n):
    error = rmse(pred[i], target[i])
    #print(error)
    total1.append(error)
    
for i in range(n):
    c = np.concatenate((pred[i], target[i]))
    total3.append(c)
    
for i in range(n):
    n_error = total1[i] / ( max(total3[i][0]) - min(total3[i][0]) )
    total2.append(n_error)

print("#################")
print("RMSE")
print(round(sum(total1) / 6, 4))
print("#################")
print("NRMSE")
print(round(sum(total2) / 6, 4))