# -*- coding: utf-8 -*-
"""
Created on Sat May 27 13:28:00 2023

@author: Lenovo
"""


import pandas as pd
df=pd.read_excel(r"D:\DATA SCIENCE\Data_Science\practice\Coca_Rating_Ensemble (1).xlsx")
df.head()
df.dtypes
df.columns


#convert dtypes
df.convert_dtypes
df=df.astype(str)
df.dtypes

#convert specific column type 
df=df.astype({'REF':float,'Rating':float,'Cocoa_Percent':float}) 
print(df.dtypes)
df.head()

df.columns
col=['Company', 'Name', 'Company_Location', 'Bean_Type', 'Origin']
df2=df[col].astype(str)
df2.dtypes

#change single col dtypes
df3=df.astype({'REF':int})
df3.dtypes

df.shape
df.columns
df.info()
df.describe()
df.index

#accessing one col.
df4=df['Name']
df4
df4.head()

#accesing two col
df5=df[['Name','REF']]
df5

df.head()
df['REF']=df['REF']-1000
df['REF']

#rename the columns
df6=df.rename(columns=({'REF':'reference'}))
df6.head()

#rename using axis=1
df7=df.rename({'Name':'NAM','Rating':'Ratinggg'},axis=1)
df7

#rename using axis=1
df8=df.rename({'Company':'com','Rating':'Ratinggg'},axis='columns')
df8

#drop col
df10=df.drop(['Rating'],axis=1)
df10

#drop col using lables
df11=df.drop(labels=['REF'],axis=1)
df11

#drop col using index
#here REF col drop
print(df.drop(df.columns[1],axis=1))

#drop two or more col
df12=df.drop(['Bean_Type','Origin'],axis=1)
df12

#drop two or more col using index
df13=df.drop(df.columns[[0,1]],axis=1)
df13

#drop col from list of columns
df.columns
lst=['Company', 'Name', 'REF', 'Review']
df14=df.drop(lst,axis=1)
df14

#slicing of df
df.columns
df15=df.iloc[:5,0:2]
df15

##########################################################3
#------------------------------------------------------
import pandas as pd
df1=pd.read_csv(r"D:\Data_Science\practice\Computer_Data.csv")

df1.head()
df1.shape
df1.describe()
df1.columns

#######################33

#accesing the col
df1['speed']

#accesing the col
g=df1[['price','hd','screen']]
g.head()

#######################################
#rename the col
df1.rename({'price':'PRICE'},axis=1)

#####################################
#drop the col
df4=df1.drop(['speed','hd'],axis=1)
df4

#####################################3
#accesing specific cell/row using iloc
df2=df1.iloc[1:5,:4]
df2

df1.head(10)
#accesing the single cell
#[start_R:end_r,start_c:end_c]
df3=df1.iloc[3:4,3:4]
df3

df1.iloc[:1] #acces of before 1 all element
df1.iloc[1:]  #access 1 to next all element
df1.iloc[-1:]#acess last elemt

df1.iloc[:-1]

df1.iloc[::2]#it select rows which having 2-2 diffence between them
df1.iloc[::5000]#it select rows which having 500 diffence between them

###################################
#select row using loc function
df1.loc[:5,['price']]
df1.loc[:5,['price','speed']]
df1.loc[:5:2]
df1.loc[:10,['price']]

#############################3

#select specific row
df6=df1.query("price==1595")
df6

#it will print cources to duration column with all row
df7=df1.loc[:,"speed":"ram"] 
df7
#############################################

#square of col speed using in numpy
# apply on single col
import numpy as np
df1['speed']=df1['speed'].apply(np.square)
df1

######################################################

#data visualization using matplotlib
import seaborn as sn
import matplotlib.pyplot as plt
#boxplot
a=sn.boxplot(df1['price'])
sn.histplot(df1[['price','hd']])

plt.hist(df1.hd)
df1
########################################
technologies = [["spark",20000,"30days"],
                ["pandas",300000,"40days"]]
                
df = pd.DataFrame(technologies)
print(df)
column_name = ["courses","fee","duration"]
row_label = ['a','b']
df = pd.DataFrame(technologies,columns = column_name,index = row_label)
print(df)

#pyplot
plt.pie(df['fee'])
df1.plot()
##########################################################
#-----------------------------------------------------

#file 3 
d2=pd.read_csv(r"D:\Data_Science\practice\emp_data.csv")
d2.head()
d2.describe()

d2.columns

#rename the col
d2=d2.rename({'Salary_hike':'SAL_HIKE','Churn_out_rate':'churn_rate'},axis=1)
d2

#drop col
d3=d2.drop(['churn_rate'],axis=1)
d3

#access one col
d2['SAL_HIKE']

#change dtype of col
d2=d2.astype({'SAL_HIKE':float})
d2.dtypes

#change dtype of both the col
d2=d2.astype({'SAL_HIKE':float,'churn_rate':str})
d2.dtypes

#slicing of dataset
#iloc(st_r:end:r,st_c:end:c)
d2.iloc[:5,:1]
d2.iloc[:1] #acces of before 1 all element
d2.iloc[1:]  #access 1 to next all element
d2.iloc[-1:]#acess last elemt

d2.iloc[:-1]

d2.iloc[::2]#it select rows which having 2-2 diffence between them
d2.iloc[::5000]#it select rows which having 5000 diffence between them

###################################
#select row using loc function
d2.loc[:5,['SAL_HIKE']]
d2.loc[:5,['SAL_HIKE','churn_rate']]
d2.loc[:5:2]
d2.loc[:10,['churn_rate']]


########################################################
import pandas as pd
df3=pd.read_csv(r"D:\Data_Science\practice\Diabetes.csv")

df3
df3.columns

#rename col
df3=df3.rename({' Number of times pregnant':'freq_pregnant',
            ' Plasma glucose concentration':'glucose concentration',
            ' Body mass index':'Body mass',
            ' Diabetes pedigree function':'fun'},axis=1)

df3.columns

#dtype
df3.dtypes

df4=df3.astype({'freq_pregnant':str}).dtypes
df4

#drop col
df5=df3.drop([' Triceps skin fold thickness'],axis=1)
df5.columns

#slicing of dataset
df3.iloc[:10:2,:3]
df3.iloc[-1:,1:3]

#access specing row in specific col
df3.loc[:4,['freq_pregnant']]
df3=df3.astype({'freq_pregnant':int})
#use of query
df7=df3.query("freq_pregnant==6")
df7
df3.dtypes

#access the specific col
df3['freq_pregnant']

#drop a row
df9=df3.drop(df3.index[1])
df9
##################################################

d4=pd.read_csv(r"D:\Data_Science\practice\ethnic diversity.csv")

d4.columns
d4=d4.rename(columns={'Employee_Name':'name','EmpID':'ID'})
d4

#convert dtypes
d4.dtypes
#convert all col dtypes
d4.astype(str).dtypes

#labling of all the row

l=[f'r{i}' for i in range(len(d4))]
l

x=d4.set_axis(l)
x

x.loc[:'r5']
#accesing the specific row
x.loc[['r3','r4','r5']]

x.query("Position=='Administrative Assistant' and ID==1211050782")


x.head()























