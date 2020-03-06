# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:55:20 2020

@author: EBS-1803
"""

import matplotlib.pyplot as plt
import numpy as np

# fake up some data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low), 0)

# basic plot
plt.boxplot(data)

N = 200
x = np.random.rand(N)
y = np.random.rand(N)

colors = np.random.rand(N)
# 0 to 15 point radiuses
area = np.pi * (15 * np.random.rand(N))**2
plt.figure()
plt.scatter(x, y, s=5, c='blue', alpha=1)
plt.figure()
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()