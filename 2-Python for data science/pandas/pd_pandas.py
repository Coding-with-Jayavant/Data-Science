# -*- coding: utf-8 -*-
"""
Created on Wed May  3 08:23:49 2023

@author: Lenovo
"""

#Morning Session

#
import pandas as pd
#create df using list
technologies = [["spark",20000,"30days"],
                ["pandas",300000,"40days"]]
                
df = pd.DataFrame(technologies)
print(df)

column_name = ["courses","fee","duration"]
row_label = ['a','b']
df = pd.DataFrame(technologies,columns = column_name,index = row_label)
print(df)
#We are checking the data types of Data Frame
df.dtypes

#create df using dict
types = {'courses':str,'fee':float,'duration':str}
newdf = df.convert_dtypes(types)
df.dtypes

technologies = {
    'index':[1,2,3,4],
    'courses':["Spark","PySpark","Puma","Hadoop"],
    'fee':[20000,30000,40000,3500],
    'duration':['30days','40days','50days','35days'],
    'discount':[10.00,23.00,15.00,15]
    
    }
df = pd.DataFrame(technologies)
df
df.dtypes #data types
df1=df.convert_dtypes()
df1

df=df.astype(str) #convert all column type into str
print(df.dtypes)

df=df.astype({'index':int,'discount':float}) #convert specific column type 
print(df.dtypes)

#Convert the data frame to csv file(excel file)
df.to_csv('data_file.csv')
df.describe()
#We can also create the file by passing the absolute path
#to the file using python
df.to_csv(r"D:\Data_Science\advanced\bank_data.csv")
df

###################################################################
df = pd.DataFrame(technologies) #convert specific column data type
df
cols=['courses','duration']
df[cols]=df[cols].astype('str')
df.dtypes

df=df.astype({'fee':int})
df.dtypes

df=df.astype({'courses':int},errors="raise") 
df.dtypes