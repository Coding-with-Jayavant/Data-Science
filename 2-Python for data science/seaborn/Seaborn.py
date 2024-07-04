# -*- coding: utf-8 -*-
"""
Created on Sat May 13 15:22:14 2023

@author:Lenovo
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv("D:\Data_Science\jupytor_nb\car.csv")
df
df.describe()
df.info
plt.hist(df[['speed','dist']])
plt.boxplot(df['speed'])
df.columns
sns.displot(df['speed'],kde=True)
#almost car treavel between 10 to 15 speed left skewd
sns.displot(x='dist',kde=True,data=df)
#almost car treavel between 20 to 60 distance rigth skewd
sns.histplot(df['speed'])
plt.hist(df['speed'])
#boxplot used for finding outlier
sns.boxplot(df.speed)
#no outlier is in data
#mean speed of all cars are 15
#the minimum speed is 5km
plt.hist(df.dist)
plt.boxplot(df.dist)
#their are one oulier in dist column

#convert speed col into list
speed=df['speed'].tolist()
speed
print("skewness of speed",skew(speed))
#convert dist col into list
dist=df['dist'].tolist()
dist
print("skewness of dist",skew(dist))
print(skew(dist,axis=0,bias=True))
#it signifies that distibution is posi
print(kurtosis(dist,axis=0,bias=True))
#it is playkurtic it means it produce

#Skewness tells us the direction of outliers

#count plot
sns.countplot(df['speed'])

sns.countplot(x='speed',hue='dist',data=df)

#kdeplot
#kernel density
sns.kdeplot(x='speed',data=df,color='red')

#it will shows speed is increase and distance is also increase
#speed and diatanc both are dependent
sns.scatterplot(x='speed',y='dist',data=df )
#in plot we can observ that
#avg of speed of car treavel between 10 to 15 speed

#jointplot used to show corelation
sns.jointplot(x='speed', y='dist',data=df,kind='reg')

#pair plot
sns.pairplot(df)

#find corelation factor using heatmap
corr=df.corr()
sns.heatmap(corr)

plt.scatter(df['speed'], df['dist'])


