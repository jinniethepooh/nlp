import pandas as pd
from pandas import DataFrame

import numpy as np
import os

cwd = os.getcwd()
addr = cwd + '/linkedin-data/mtcars.csv'

data = pd.read_csv(addr)
# print(data.groupby('cyl').sum())
# print(data.describe())
print(pd.crosstab(data.vs, data.cyl))

a = np.array([[1.,3.],[2.,4.]])
b = np.array([[5.,8.],[7.,9.]])
print(a * b)

x = np.array([1,2,7])
y = np.array([3,8,9])
print(np.dot(x, y))

xx = np.array([[7.,9.],[5.,12.]])
yy = np.array([[2.,8.],[7.,4.]])
print(np.dot(xx, yy))

xx = np.array([[1.,2.,3.],[4.,5.,6.]])
yy = np.array([[10.,11.],[20.,21.],[30.,31.]])
print(np.dot(xx, yy))

a = np.array([1,8,2,6,3,8,5,5,5,5])
b = np.array([17,16,20,18,22,15,21,15,17,22])
print((a + b) / 10)

a=np.array([10, 15, 20])
b=([5, 7, 9])
print((a - b) * 7)

# What is the lower and upper limit for the Tukey Outlier, given Q1= 1.714 and Q3=1.936 ?
q1 = 1.714
q3 = 1.936
delta = q3 - q1
print('upper = ', q3 + (1.5 * delta))
print('lower = ', q1 - (1.5 * delta))

