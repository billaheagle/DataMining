# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:34:22 2020

@author: Asus
"""

import pandas
import numpy as np
from sklearn.preprocessing import MinMaxScaler

dir = "iris.data.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(dir, names=names)
array = dataset.values

#print(array)

x = array[:,0:4]
y = array[:,4]

scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(x)

np.set_printoptions(precision=3)
print(rescaledX[0:5,:])