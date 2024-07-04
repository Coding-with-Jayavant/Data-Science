# -*- coding: utf-8 -*-
"""
Created on Tue May  9 08:20:19 2023

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

#pandas join,by default it will join the table left join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
df3

###################################

#pandas inner join dataframe
#it will just join two tables similar content
df4=df1.join(df2,lsuffix="_left",rsuffix="_right",how="inner")
df4

###################################

#pandas left join dataframe
#it will take all content from left table
# and from right it will take tables similar content
df5=df1.join(df2,lsuffix="_left",rsuffix="_right",how="left")
df5
###################################

#pandas right join dataframe
#it will take all content from right table
# and from left it will take tables similar content
df6=df1.join(df2,lsuffix="_left",rsuffix="_right",how="right")
df6

#pandas join it u[;sed to join two indexes in df if their
#is no explt mention on column
################################33
#inner join another method
df7=df1.set_index('courses').join(df2.set_index('courses'),how='inner')
df7













