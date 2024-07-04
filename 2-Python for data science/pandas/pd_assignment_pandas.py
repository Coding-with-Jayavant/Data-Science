# -*- coding: utf-8 -*-
"""
Created on Fri May  5 09:36:00 2023

@author: Lenovo
"""


import pandas as pd
df=pd.read_csv(r"D:\Data_Science\advanced\boston_data.csv")
print(df)

#######################################################################################
#Accessing shape and size
df.shape
df.size


# Accessing one column contents
column1 = df['crim']
print(column1)


# Accessing two columns contents
two_columns = df[['age', 'tax']]
print(two_columns)


# accessing certain cell from column
df['crim'][20]

#######################################################################################
# Describe DataFrame
df.describe()


# rename() – Renames pandas DataFrame columns
df = df.rename(columns={'crim': 'Crime', 'dis': 'Distance'})
df


# Rename Column Names usin…