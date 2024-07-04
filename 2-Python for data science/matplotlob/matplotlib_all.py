# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 08:41:15 2023

@author: Lenovo
"""

#write pythhon program  to draw line using matplotlob
import matplotlib.pyplot as plt
x= range(1,50)
y= [value *3 for value in x]

#to print range of number we rquired astrict function
print("value of x:")
print(*range(1,50))

print("Values of y(thrice of x):")
print(y)

#draw line using matplotlib
plt.plot(x,y)

#give the lable to the plot
plt.title("line plot")

#labling the 
plt.xlabel("x-axis")
plt.ylabel("y-axis")

#####################################
#operarions like labling , title
a=[1,2,3]
b=[2,4,1]
plt.plot(a,b)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("line graph")
plt.show()

#################################33
#write python program to draw line chart of the financial data
import pandas as pd

df=pd.read_csv(r"D:\Data_Science\practice\fdata.csv")
df.plot()
plt.show()

#########################################################
df1=pd.read_csv(r"C:\Users\Lenovo\Downloads\Data_Science_Attendance_Sheet2.csv")
df1.plot()
plt.show()

'''x1=df1['datum']
x2=df1['Jaywant Warkhade']
#datum,Jaywant Warkhade
plt.plot(x2,x1)'''

d=df1.drop('year',axis=1)
d=d.drop('month',axis=1)
d=d.drop('weekday',axis=1)
d=d.drop('datum',axis=1)

d=d[:-1]
d.plot()
###############################

#write python program to plot 2 or more plot with legends

a1=[10,20,30]
b1=[20,30,40]

#line 2 points
a2=[10,20,30]
b2=[40,30,20]















