# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:00:58 2020

@author: Asus
"""

import pandas

dir = "iris.data.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(dir, names=names)

print(dataset.shape)
print(dataset.head(20))
print(dataset.describe())
print(dataset.groupby('class').size())
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
dataset.hist()

from pandas.plotting import scatter_matrix
scatter_matrix(dataset)