# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:15:33 2023

@author: Lenovo
"""

import pandas as pd
df=pd.read_csv(r"D:\Data_Science\data_science\Company_Data.csv")
df

#rename col
df.rename(columns={'Sales':'Sales_list','Income':'Income_list'}, inplace=True)
df

#row count
rows_count=len(df.index)
rows_count
#row count
rows_count=len(df.axes[0])
rows_count
#row count
rows_count=df.shape[0]
rows_count
#col count
col_count=df.shape[1]
print(col_count)

def add_4(x):
    return x+4
#apply for single column add 4 in col AGE
df['Age']=df['Age'].apply(add_4)
df['Age']

#apply for multiple column
df[['Advertising','Age']]=df[['Advertising','Age']].apply(add_4)
df[['Advertising','Age']]

#using lambda function for single column
df['Income_list']=df['Income_list'].apply(lambda x: x+5)
df['Income_list']

#using lambda function for multiple column
df[['CompPrice','Sales_list']]=df[['CompPrice','Sales_list']].apply(lambda x: x+2)
df[['CompPrice','Sales_list']]

#using dataframe.map
df['Sales_list']=df['Sales_list'].map(lambda A: A/2)
df['Sales_list']

import numpy as np
#using numpy.square method
df['Age']=df['Age'].apply(np.square)
df['Age']

#use groupby for single column
df2=df.groupby(['Income_list']).sum()
df2

#using group by for multiple column
df2=df.groupby(['Education','CompPrice']).sum()
df2

#using reset_index
df2=df.groupby(['Education','CompPrice']).sum().reset_index()
df2

#see no. of col name
df.columns

#get the list of all columns names from headers
column_headers=list(df.columns.values)
print("The column headers:",column_headers)

#using list(df) to get the column header as a list
column_headers=list(df.columns)
column_headers

#using list df to get the list of all column values
column_headers=list(df)
column_headers

#pandas shufle dataframe rows
#shufle the dataframe rows
df2=df.sample(frac=1)
df2
#reshufle the rows

df2=df.sample(frac=1).reset_index()
df2
df2=df.sample(frac=1).reset_index(drop=True)
df2
