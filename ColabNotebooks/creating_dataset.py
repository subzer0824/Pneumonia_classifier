# -*- coding: utf-8 -*-
"""creating_dataset

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13oAKHAvDobKoDvH0gefzLX5395ELtiJL

# **CREATING_DATASET**
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
import os
import cv2

basepath ='/content/drive/My Drive/Colab Notebooks/Pneumonia_classifier/data_covid'
categories = ['NORMAL','PNEUMONIA']

dataset = []

def create_dataset():
    
    for category in categories:
        path = os.path.join(datadir,category)
        class_num  = categories.index(category)
        for img in os.listdir(path):
            img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array,(120,100))
            dataset.append([new_array, class_num])

create_dataset()

len(dataset)

import random 
random.shuffle(dataset)

X = []
y = []
for features, label in dataset:
    X.append(features)
    y.append(label)
    
X = np.array(X).reshape(-1,120,100,1)
y = np.array(y)

from sklearn.model_selection import train_test_split
train_X, test_X, train_y, test_y = train_test_split(X,y,test_size =0.25)

train_X = train_X/255.0
test_X = test_X/255.0

import pickle
directories = ['train_X','test_X','train_y','test_y']
i = 0
files = [train_X, test_X, train_y, test_y]

for _ in files:
    pickle_out = open(directories[i],'wb')
    pickle.dump(_, pickle_out)
    pickle_out.close()
    i += 1

import shutil
files = ['train_X','test_X','train_y','test_y']
for f in files:
  shutil.move(f,'/content/drive/My Drive/Colab Notebooks/Pneumonia_classifier/train_test_dataset')