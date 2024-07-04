# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:07:59 2023

@author: Lenovo
"""

import matplotlib.pyplot as plt
import seaborn as sns
#import pandas as pd
#pandas only used for read csv file
#but here dataset present in a seaborn library

#for list dataset internet should be on
sns.get_dataset_names()   #list of datasets
df = sns.load_dataset('iris')
df.describe()
df.columns

###########################################################
#countplot
sns.countplot(x='sepal_length',data=df)

sns.countplot(x='sepal_length',hue='petal_length',data=df)


##########################################################
#kdeplot
sns.kdeplot(x='sepal_length',data=df,color='black')

##########################################################
df.columns

sns.displot(x='sepal_width',kde=True,data=df) 
sns.displot(x='sepal_length',kde=True,bins=9,data=df) 
sns.displot(x='petal_length',kde=True,bins=9,data=df,hue=df['species'],palette='Set1') 
########################################################

#histogram
plt.hist(df.sepal_length)
plt.hist(df.sepal_width)
plt.hist(df.petal_length)
plt.hist(df.petal_width)
####################################################

#find corelation using scatterplot
sns.scatterplot(x='sepal_length',y='sepal_width',data=df )

#box plot
plt.boxplot(df.sepal_length)
plt.boxplot(df.sepal_width)
plt.boxplot(df.petal_length)
plt.boxplot(df.petal_width)

##########################################################

#jointplot
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg')
sns.pairplot(data=df)
##########################################################
#generating heatmap for correlation

corr = df.corr()
sns.heatmap(corr)
############################################3
df.columns
#skewness shows the direction of outliers
sepal_length=df['sepal_length'].tolist()
print("skewness of sepal_length",skew(sepal_length))
print(skew(sepal_length,axis=0,bias=True))

#kurtosis of sepal_width
sepal_width=df['sepal_width'].tolist()
print(kurtosis(sepal_width,axis=0,bias=True))








