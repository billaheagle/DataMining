# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:03:29 2020

@author: Asus
"""

import pandas
import numpy as np

def readfile(file, field) :
    returnfile = pandas.read_csv(file, names=field)
    return returnfile
    
def convertdftnp(df) :
    result = df.values
    return result
    
def normalizationMinMax(datanp, rangeminmax) :
    x = datanp[0].size - 1
    y = int(datanp.size / datanp[0].size) - 1
    new_min = 0
    new_max = 1
    for i in range(x) :
        min_val = rangeminmax[i][0]
        max_val = rangeminmax[i][1]
        for j in range(y) :
            old_val = datanp[j][i]
            datanp[j][i] = (old_val - min_val) / (max_val - min_val) * (new_max - new_min) + new_min
    #print(datanp)
    return datanp
    
def savecsv(datanorm, dirres) :
    file = open(dirres, "w")
    x = datanorm[0].size - 1
    y = int(datanorm.size / datanorm[0].size) - 1
    for i in range(y) :
        for j in range(x) :
            file.write(str(datanorm[i][j]))
            file.write(",")
        file.write(datanp[i][4])
        file.write("\n")
    file.close()
    

dir = "iris.data.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
rangeminmax = [[4, 8], [2, 5], [1, 7], [0, 3]]
df = readfile(dir, names)
datanp = convertdftnp(df)
datanorm = normalizationMinMax(datanp, rangeminmax)
dirres = "result.txt"
savecsv(datanorm, dirres)
    
