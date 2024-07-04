# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:24:48 2023

@author: Lenovo
"""

import pandas as pd
#table1
technologies = ({
    'courses':["Spark","Puma","CSS","HTML"],
    'fee':[30000,40000,3434,5454],
    'duration':['30days','40days','50days','4days']
    })
df = pd.DataFrame(technologies)
i_lables=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=i_lables)
df1

#table2
technologies2 = ({
    'courses':["Spark","Java","CSS","GO"],
    'discount':[1000,2300,1500,43434]
    })
df = pd.DataFrame(technologies)
i_lables2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=i_lables2)
df2

#merge df1 and df2
df3=pd.merge(df1, df2)
df3
#merge df1 and df2
df4=df1.merge(df2)
df4
#####################################################33

df=pd.DataFrame({
    'Courses':['spark','pySpark','Python','pandas'],
    'Fee':[2323,3445,6767,5654]
    })

df1=pd.DataFrame({
    'Courses':['Pandas','Haddop','Hyperion','Java'],
    'Fee':[25000,25200,24500,24900]
    })
data=[df,df1]
df2=pd.concat(data)
df2
df2=pd.DataFrame({
    'Duration':['30days','50days','30days','40days'],
    'Discount':[1000,2300,1800,1200]})

df5=pd.concat([df,df1,df2])

df5.to_csv("d:/data_science/courses.csv")

df3.to_excel("d:/data_science/course.xlsx")

df=pd.read_excel("d:/data_science/course.xlsx")
df
#pandas series
#series is used to model 1Dimensional data
songs2=pd.Series([145,144,38,13],name='counts')

songs2.index

songs3=pd.Series([145,144,38,13],name='counts', index=['paul','john','george','dave'])
songs3.index
songs3
#NaN nan And null asr synonyms
songs3.mean()

george=pd.Series([10,7,1,22], index=['1968','1972','1968','1978'],name='George songs')
george

#it supporst CRUD-create read update delete

for item in george:
    print(item)
    
george['1968']=68
george['1968']

#deletion
s=pd.Series([2,3,4],index=[1,2,1])
del s[1]

#string use astype(str)
#numeric use pd.to_numeric
#integer use astype(int) Note:this will fail with nan
#datetime use pd.to_datetime

songs66=pd.Series([3,None,11,9],index=['paul','john','george','dave'],name='Counts')

pd.to_numeric(songs66.apply(str))
#giving error due to none/nan value
pd.to_numeric(songs66.apply(str),error='coerce')

songs66.fillna(-1)
songs66.dropna()

###############################################33333

songs69=pd.Series([7,16,21,39],
index=['ram','jay','sham','adi'],
name='counts')
songs69

import matplotlib.pyplot as plt
figg=plt.Figure()
songs69.plot()
plt.legend()

songs69.plot(kind='bar')
songs69.plot(kind='bar',color='b',alpha=.5)
plt.legend()

############################################
import numpy as np
data= pd.Series(np.random.rand(500),
                name='500 random')
fig1=plt.Figure()
ax=fig1.add_subplot(111)
data.hist()






