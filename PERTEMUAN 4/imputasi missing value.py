# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:34:22 2020

@author: Asus
"""

import pandas
import numpy as np
from sklearn.impute import SimpleImputer

dir = "iris.data.missing.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
datamissing = pandas.read_csv(dir, names=names)
array = datamissing.values

#print(array)

x = array[:,0:4]
y = array[:,4]

imp = SimpleImputer(missing_values=np.NaN, strategy="mean")

X = imp.fit_transform(x)
print(X)