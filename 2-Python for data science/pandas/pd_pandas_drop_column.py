# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:27:06 2023

@author: Lenovo
"""

#deleting columns and many operation
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
#drop fee column
df1=df.drop(["fee"],axis=1)
df1

#drop column using explicit parameter uising lables
df1=df.drop(labels=["fee"],axis=1)
df1
#alternatively u also use columns insted of lables
df1=df.drop(columns=["fee"],axis=1)
df1

#######################################3333
df = pd.DataFrame(technologies)
df
#drop column of index 1
print(df.drop(df.columns[[1]],axis=1))
print(df.drop(df.columns[[0]],axis=1))

#using inplace true,drop column
df.drop(df.columns[[0]],axis=1,inplace=True)
df

#############################################################
df = pd.DataFrame(technologies)
df
#drop two or more column using name
df.drop(["fee","duration"],axis=1)
df

##############################################################3333
df = pd.DataFrame(technologies)
df
#drop two or more column using index
df2=df.drop(df.columns[[0,1]],axis=1)
df2
##############################################################
df = pd.DataFrame(technologies)
df
#drop two or more column using list
l1=["fee","duration"]
df.drop(l1,axis=1)
df
##############################################################3333
df = pd.DataFrame(technologies)
df
#drop two or more column using inplace
df.drop(df.columns[[0,1]],axis=1,inplace=True)
df








