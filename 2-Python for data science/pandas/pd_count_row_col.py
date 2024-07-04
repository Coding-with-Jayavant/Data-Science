# -*- coding: utf-8 -*-
"""
Created on Mon May  8 08:24:54 2023

@author: Lenovo
"""

import pandas as pd

technologies = ({
    'courses':["Spark","PySpark","Puma","DSML","HTML","CSS","JAVA"],
    'fee':[20000,30000,40000,3434343,54545454,5454545,60000],
    'duration':['30days','40days','50days','4days','5days','11days','90days'],
    'discount':[1000,2300,1500,43434,434343,343434,3434]
    })
df = pd.DataFrame(technologies)
df
#count number of rows in dataset
rows_count=len(df.index)
rows_count
#method second to calculate row
rows_count=len(df.axes[0])
rows_count
#####################################################33

#find number of row in dataset
row=df.shape[0]
print(row)
#find number col in dataset
col=df.shape[1]
print(col)





































