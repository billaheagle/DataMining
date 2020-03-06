# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 14:07:11 2020

@author: Asus
"""

import pandas
import numpy as np
import matplotlib.pyplot as plt

def readfile():
    returnfile = pandas.read_csv(r'train_data.csv', sep=',')
    return returnfile

def convertdftnp(df):
	result = np.empty([df['A1'].size, df.columns.size-1], dtype=float)
	y=0;
	for feature_name in df.columns:
		if feature_name != 'Class':
			for x in range(0, result.shape[0]-1):
				result[x,y]=df[feature_name][x];
			y=y+1
	return result;

def savecsv(dat,strout):
	np.savetxt(strout, np.array(dat), delimiter=",")


res_pd=readfile();  
res_np=convertdftnp(res_pd);  
