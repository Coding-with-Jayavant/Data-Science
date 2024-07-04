# -*- coding: utf-8 -*-
"""
Created on Mon May  8 08:33:21 2023

@author: Lenovo
"""

#pandas apply function to a col
#using DataFrame.apply() to apply function add col

import pandas as pd

matr={ "A":[1,2,3],
    "B":[4,5,6],
    "C":[7,8,9]}
df=pd.DataFrame(matr)
df

def add_3(x):
    return x+3

#add 3 in given matrics using function
df2=df.apply(add_3)
df2
##########################################################3
matr={ "A":[1,2,3],
    "B":[4,5,6],
    "C":[7,8,9]}
df=pd.DataFrame(matr)
df
def add_4(x):
    return x+4

#add 4 in row B matrics using function only this row will change
df2=df['B'].apply(add_4)
df2
#perform add operation on col A and B
#it will directly change the actual values in df
df[['A','B']]=df[['A','B']].apply(add_4)
df

#####################################################
#function increase space complexity
#and function take more memory
#because of it we use anonymous finction like lambada

df2=df.apply(lambda x: x+10)
df2
######################################33
matr={ "A":[1,2,3],
    "B":[4,5,6],
    "C":[7,8,9]}
df=pd.DataFrame(matr)
df
#apply lambda function to single col
df['A']=df['A'].apply(lambda x:x-5)
df
###############################################3
#transform function
#it will also add in 
matr={ "A":[1,2,3],
    "B":[4,5,6],
    "C":[7,8,9]}
df=pd.DataFrame(matr)
df

def add_3(x):
    return x+3

#add 3 in given matrics using transform
df2=df.transform(add_3)
df2
####################################333333
matr={ "A":[1,2,3],
    "B":[4,5,6],
    "C":[7,8,9]}
df=pd.DataFrame(matr)
df

def add_3(x):
    return x+3

#add 3 in given matrics using map
#map apply on single row
df['A']=df['A'].map(add_3)
df
############################################
#use numpy 
import numpy as np
matr={ "A":[1,2,3],
    "B":[4,5,6],
    "C":[7,8,9]}
df=pd.DataFrame(matr)
df
#square of col A using in numpy
# apply on single col
df['A']=df['A'].apply(np.square)
df

#squring a single col but directly using numpy without using pandas
df['B']=np.square(df['B'])
df

