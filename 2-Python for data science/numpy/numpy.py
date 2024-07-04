import numpy as np
arr1 = np.arange(4)
 
print('First array:')
print(arr1)
import numpy as np
print(np.__version__)

print(np.show_config())

#program to add function
import numpy as np
import sys
np.info(np.add,output=sys.stdout)
print(np.info(np.dot,output=sys.stdout))
print(np.info(np.transpose,output=sys.stdout))

x=np.array([1,2,3,4,5])
print("original array :",x)

print("test if none of the elemnets of the said array is zero:")
print(np.all(x))

################################################
#programm to check given array is non zero
y=np.array([1,0,0,5,0])
print("if the any of the element of the given array is non-zero")
print(np.any(y))

#test given array element for finite or not

a=np.array([1,0,np.nan,np.inf])
print("original array :",a)
print("test a given array elemnt wise for finiteness :")
print(np.isfinite(a))

###################################################3

#checking of iscomplex
v=np.array([1+1j , 1+0j ,4.5,3])
print("original array:",v)
print("checking the colex number :")
print(np.iscomplex(v))

print("checking the real number :")
print(np.isreal(v))

#checking the scalar value
print(np.isscalar(3.5))
#True
print(np.isscalar([3.5]))
#False
#######################################################3

#it is 2d array because of square 
lst=[[1,2,3],[4,5,6],[5,3,2]]
lst
"""
array([[1, 2, 3],
       [4, 5, 6],
       [5, 3, 2]])
"""
k=np.array(lst)
k

#check dimenesion
k.ndim

#check shape row*col
k.shape

#total number of element
k.size
#Out[21]: 9

#access elemnt in 2 row and 3 col
k[1,2]
#Out[22]: 6

k[1][2]
#Out[23]: 6

#access first elemnt
k[0][0]
#or both are same
k[0,0]

k[0][0:2]
#Out[26]: array([1, 2]

#access the element on fir and second row in second col
k[0:2,2]
#Out[27]: array([3, 6])
 ###########################################

x=np.array([[1,0],[0,1]])
x
"""
# Out[30]: 
# array([[1, 0],
#        [0, 1]])
# """
y=np.array([[2,1],[1,2]])
y
"""
# Out[32]: 
# array([[2, 1],
#        [1, 2]])
# """

#add x and y

c=x+y
c
"""
# array([[3, 1],
#        [1, 3]])

# """

#multiply x and y

m=x*y
m
"""
 array([[2, 0],
        [0, 2]])
 """
#########################################

#calculate dot product
d=np.dot(x,y)
d
"""
# Out[39]: 
# array([[2, 1],
#        [1, 2]])
# """
##############################################
#calcutate transpose of matrix
#transpose - rows are converted into col and col converted into row
c=np.array([[1,1],[2,2],[3,3]])
c
c.T
"""
Out[41]: 
# array([[1, 2, 3],
#        [1, 2, 3]])
# """
# #####################################################3

#write a numpy program to get the minimum and miximum value
import numpy as np
x=np.arange(4).reshape((2,2))
print("Original matrix :",x)
"""
# Original matrix : 
#  [[0 1]
#  [2 3]]
# """
print("Max value along the second(veritical) axis:")
print(np.max(x,1))
#[1 3]


print("min value along the second axis:")
print(np.amin(x,1))
#[0 2]

print("Max value along the second axis:")
print(np.amax(x,0)) #it will access horizontal axis
#[2 3]

print("min value along the second axis:")
print(np.amin(x,0))
#[0 1]

# ############################3






















