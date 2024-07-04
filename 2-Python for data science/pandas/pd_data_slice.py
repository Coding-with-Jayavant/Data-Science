# -*- coding: utf-8 -*-
"""
Created on Thu May  4 08:48:12 2023

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

#give lables to row
row_lables=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_lables)
print(df)

###############################33
#selct specific row and column first(:) for row and second(:) for column
#df.iloc[st_row:end_row,st_col:end_col]
df.iloc[0:2,0:2]
df.iloc[:,0:2] #slicing the df usinf iloc and loc
 
df.iloc[0:2,:]
df.iloc[0,:]
###################################3
df3=df.iloc[1:6,1:2] #access single element
df3

df.iloc[2]
#######################################
df1=df.iloc[[2,3,6]] #select specific number of rows
df1

df.iloc[:,:1] #acces of before 1 all element
df.iloc[1:]  #access 1 to next all element
df.iloc[-1:]#acess last elemt

df.iloc[:-1]

df.iloc[::2]#it select rows which having 2-2 diffence between them

########################################################3
#loc

df = pd.DataFrame(technologies)
df
#give lables to row
row_lables=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_lables)
print(df)

#select row using loc r2 row selected
df2=df.loc['r2']
df2
df3=df.loc[['r2','r4','r1']] #select specific row using row
df3
df4=df.loc['r1':'r6':2] #access element with 2-2 gap
df4
###########################################################
df = pd.DataFrame(technologies)
df
#give lables to row
row_lables=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_lables)
print(df)

#select  random column
df2=df.loc[:,["courses","duration"]]
df2
#it will print cources to duration column with all row
df3=df.loc[:,"courses":"duration"] 
df3

#it will print all clolumn upto duration and all rows

df4=df.loc[:'r0',"fee"]
df4

df4=df.loc[:,"duration":]
df4
###############################333
#select specific row
df2=df.query("courses=='Spark'")
df2
df2=df.query("courses!='Spark'")
df2

