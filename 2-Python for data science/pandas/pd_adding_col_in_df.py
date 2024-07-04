# -*- coding: utf-8 -*-
"""
Created on Thu May  4 17:27:54 2023

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

#adding one column into df
tutors=['a','b','c','d','e','f','k']
df2=df.assign(TutorS=tutors)
print(df2)

#add two column in df
tutors=['a','b','c','d','e','f','k']
mnc=['1','2','3','4','5','5','6']
df3=df.assign(MNCcomp=mnc,Tutorss=tutors)
df3
############################################
#derive new column using existing column
df = pd.DataFrame(technologies)
df
#new column will created on performing operation on previous col
df2=df.assign(discount_percent=lambda x: x.fee * x.discount/100)
df2
################################################
#append column
#add new column
mnc=['1','2','3','4','5','5','6']
df["MNC"]=mnc
df

#add new column at specific position
mnc=['1','2','3','4','5','5','6']
df.insert(3, "M", mnc)
df

############################################
#rename colomn
import pandas as pd

technologies = ({
    'courses':["Spark","PySpark","Puma","DSML","HTML","CSS","JAVA"],
    'fee':[20000,30000,40000,3434343,54545454,5454545,60000],
    'duration':['30days','40days','50days','4days','5days','11days','90days'],
    'discount':[1000,2300,1500,43434,434343,343434,3434]
    })
df = pd.DataFrame(technologies)
df
df.columns
#rename column
df.rename(columns={"courses":"COR"})
#df.rename(columns={"courses":"COR"},{"fee":"COR"})
#rename method 2
df.rename({"courses":"COR"},axis="columns")
#rename method 3
df.rename({"courses":"COR"},axis=1)
#rename method 4
df.rename({"courses":"COR"},axis="columns",inplace=True)
df














