# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:12:27 2023

@author: Lenovo
"""

#group by method
#grouping the data points (i.e. rows) based on the distinct values in the given column or columns
import pandas as pd

technologies = ({
    'courses':["Spark","Puma","Puma","CSS","HTML","CSS","JAVA"],
    'fee':[40000,30000,40000,3434343,54545454,5454545,40000],
    'duration':['30days','40days','50days','4days','5days','11days','90days'],
    'discount':[1000,2300,1500,43434,434343,343434,3434]
    })
df = pd.DataFrame(technologies)
df
#use groupby it group distinct values
df2=df.groupby(['fee']).sum()
df2
#mean of fee
df2=df.groupby('courses')['fee'].mean()
df2

#mean and max aggregation
df5=df.groupby('courses')[["fee","discount"]].agg(["mean", "max"])
df5
#use group by in multiple col
df3=df.groupby(['courses','fee']).sum()
df3

#it will reset the index 
df4=df.groupby(['fee']).sum().reset_index()
df4
########################get column name###############################
import pandas as pd

technologies = ({
    'courses':["Spark","Puma","Puma","CSS","HTML","CSS","JAVA"],
    'fee':[40000,30000,40000,3434343,54545454,5454545,40000],
    'duration':['30days','40days','50days','4days','5days','11days','90days'],
    'discount':[1000,2300,1500,43434,434343,343434,3434]
    })
df = pd.DataFrame(technologies)
df
#it will show all the column name
#method 1 to get column name
df.columns

###
#get list of all column names from headers
col_header=list(df.columns.values)
print("The number of col : ",col_header)
##########################################
#method 2 to get column name
column_headers=list(df.columns)
column_headers

#method 3 to get column name
column_headers=list(df)
column_headers
##################################################################3









































