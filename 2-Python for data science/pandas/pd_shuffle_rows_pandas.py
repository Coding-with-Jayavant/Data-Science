# -*- coding: utf-8 -*-
"""
Created on Mon May  8 17:22:46 2023

@author: Lenovo
"""

#pandas shuffle rows 
import pandas as pd

technologies = ({
    'courses':["Spark","Puma","Puma","CSS","HTML","CSS","JAVA"],
    'fee':[40000,30000,40000,3434,5454,5454,40000],
    'duration':['30days','40days','50days','4days','5days','11days','90days'],
    'discount':[1000,2300,1500,43434,434343,343434,3434]
    })
df = pd.DataFrame(technologies)
df
#shuffle the rows
#when we get less accuracy because of that we need to
#shuffle the rows and again apply algorithm
df2=df.sample(frac=1)
df2

#creating new index starting from zero
df3=df.sample(frac=1).reset_index()
df3

#drop shuffle index
df4=df.sample(frac=1).reset_index(drop=True)
df4




