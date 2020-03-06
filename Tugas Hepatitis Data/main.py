# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:17:13 2020

@author: Asus
"""

import pandas
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

dir = "hepatitis.data.csv"
names = ['CLASS', 'AGE', 'SEX', 'STEROID', 'ANTIVIRALS', 'FATIGUE', 'MALAISE',
         'ANOREXIA', 'LIVER BIG', 'LIVER FIRM', 'SPLEEN PALPABLE', 'SPIDERS',
         'ASCITES', 'VARICES', 'BILIRUBIN', 'ALK PHOSPHATE', 'SGOT', 'ALBUMIN', 'PROTIME', 'HISTOLOGY']
dataset = pandas.read_csv(dir, names=names)
array = dataset.values

print(dataset.row)

x = array[:,1:19]
y = array[:,19]

