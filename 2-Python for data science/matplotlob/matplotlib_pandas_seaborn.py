# -*- coding: utf-8 -*-
"""
Created on Thu May 25 23:13:26 2023

@author: Lenovo
"""

import pandas as pd
import matplotlib as plt
df=pd.read_csv(r"C:\Users\Lenovo\Downloads\Data_Science_Attendance_Sheet2.csv")

df.head()
df.columns

#Q.1 Rename your name column
l={'Jaywant Warkhade':'Jayavant'}
df=df.rename(columns=l)
df.columns

#Q. 2 Convert your column into list
lst=list(df['Jayavant'])

#Q. 3 From the derived list,find out how for how many days,you appeared 0,1,2,3,4,5,7 sessions
#Q.4 Generate a bar graph of your attendance
plt.figure(df['Jayavant'])
#Q.5 Generate 5 number summary using describe() and illustrate the minimum number of sessions ,max
#number of sessions and mean number of sessions you did during the training

#Q.6 Generate box plot using seaborn for your column and write the inference
import seaborn as sns
sns.boxplot(df.Jayavant)

#Q.7 Generate joint plot using seaborn for your column and write the inference
df.columns
sns.jointplot(x='datum', y='Jayavant',data=df,kind='reg')

#Q. 8 From complete dataframe, find out how many are regular students, how many are moderate and
#how many are poor in attendance.
#Given the data sheet of marksheet.csv ,answer the following questions
#Q.9 Out of functions, list and dictionary ,in which area you are strong and weak?
#Q.10 How many students have shown very good performance and how many have shown poor
#performance?
#Given the document AI_jobs_in_2024.docx,attempt following questions
#Q.11 Open the given file in read mode
with open("quize.txt") as f: 
    r=f.read()
    print(r)
    
#Q.12 Remove the numbers from the text
#Q.13 How many companies were surveyed ,extract using text processing
#Q.14 How many companies are willing to shift in AI domain,extract using text processing.
#Q.15 How many millions jobs are expected to create in 2024 in field of AI
#Q.16 Convert numbers into words










