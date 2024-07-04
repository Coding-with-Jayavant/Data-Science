# -*- coding: utf-8 -*-
"""
Created on Wed May  3 09:15:27 2023

@author: Lenovo
"""

#deleting rows and many operation
#Evening Session
import pandas as pd

technologies = ({
    'courses':["Spark","PySpark","Puma","DSML","HTML","CSS","JAVA"],
    'fee':[20000,30000,40000,3434343,54545454,5454545,60000],
    'duration':['30days','40days','50days','4days','5days','11days','90days'],
    'discount':[1000,2300,1500,43434,434343,343434,3434]
    })
df = pd.DataFrame(technologies)
df
#Data frame properties


#It will going to return no of column and rows 
df.shape

#It will going to return the size of data frame
df.size

#It will going to return the columns
df.columns

#It will going to return the columns values in Index list
df.columns.values

#index will going to print from where it is going to start
df.index

#Accessing the column
df['duration']

#Accessing some rows and column
df[['fee','duration']]


#Select the certain rows and assign it to another data frame

df2 = df[6:]
#if we assign here 6 we get 6th and onwards

df2 = df[3:] #As we can see in this example it taking 3rd and 3rd onwards
df2

#Subtracted from specific column
df['fee'] = df['fee'] - 500
df['fee']

#Exploratery data analysis
df.describe()

#Rename dataframe column
df.columns = ('a1','a2','a3','a4')
df

#To change the rows and column using rename method
#if axis == 1 then column will be choosen
#if axis == 0 then rows will be choosen
df = df.rename({'a1':'a','a2':''}, axis = 1)
df = df.rename({'a3':'c','a4':'d'}, axis='columns')
df

technologies = ({
    'courses':["Spark","PySpark","Puma","DSML","HTML","CSS","JAVA"],
    'fee':[20000,30000,40000,3434343,54545454,5454545,60000],
    'duration':['30days','40days','50days','4days','5days','11days','90days'],
    'discount':[1000,2300,1500,43434,434343,343434,3434]
    })
df = pd.DataFrame(technologies)
df

df.columns = ('a1','a2','a3','a4')
df

#delete row in data set using drop command and set index
df1=df.drop(df.index[[1,3]])
df1

#delete row using lables
df1=df.drop([0,1])
df1
#2 onward row will deleted
df1=df.drop(df.index[2:])
df1
#####################################################################
df = pd.DataFrame(technologies)
df
#delete row using defailt index
df1=df.drop(0)
df1
####################################################
df = pd.DataFrame(technologies)
df
#delete row of index 0,3
df1=df.drop([0,3])
df1
#it will delete 0,1,2
df1=df.drop(range(0,3))
df1














