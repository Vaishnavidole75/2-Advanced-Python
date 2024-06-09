# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:19:08 2023

@author: Vaishnavi
"""
#               OPERTIONS USING NUMPY

#                   NUMPY

#To install numpy  follow below command
#pip install numpy

###################################################


#create array
from numpy import array
#create array
l=[1.0,2.0,3.0,4.0]
a=array(l)
#Display array
print(a)
#Display array shape
print(a.shape)
#crate array
from numpy import array
#create array
l=[1.0,2.0,3,0]
a=array(1)
#display array
print(a.shape)

from numpy import empty
a=empty([3,3])
a

#create zero array
from numpy import zeros
a=zeros([3,5])
a


#create one array
from numpy import ones
a=ones([5])
a
#################################
from numpy import vstack
#vstack=vertical stack
#create first array
#element will arrNGng vertically
a1=array([1,2,3])
a1
#create second array
a2=array([4,5,6])
#create vertical stack
a3 =vstack((a1,a2))
print(a3)
print(a3.shape)
##################################
#create array with hstack
#hstack= horizontal stack
#element arrange horizontally
from numpy import array
from numpy import hstack

#frist array
a1=array([1,2,3])
a1
#create second array
a2=array([4,5,6])
a2
#create horizontal stack
a3=hstack((a1,a2))
a3
print(a3.shape)
#############################################
#two dimensional list of lists to array
#ceate 2dimensional array
from numpy import array
#list of data
data=[[11,22],
      [33,44],
      [55,66]]
data
#array od data
data=array(data)
print(data)
print(type(data))
######################
#index a one-dimensional array
from numpy import array
#define  array
data=array([11,22,33,44,55])
print(data[0])
print(data[4])
###########################
#index array out of bounds
from numpy import array
#define array

data=array([11,22,33,44,55])
print(data[5])
#o/p error
###############################
from numpy import array

data=array([11,22,33,44,55])





###############
from numpy import array
data=array([
    
[11,22],
[33,44]
[55,66]])
print(data[0,])
#o/p [11,22


#neagative slicing of one dimensional array
from numpy import array
data=array([11,22,333,44,55])
print(data[-2:])

##############################################3
#spilt input and output data
#In machine learning capital X is used for input
#small y is used for output
from numpy import array

data=array([
    [11,222,33],
    [44,55,66],
    [77,88,99]])

X,y=data[:, :-1],data[:,-1]
X,y
print(X)
print(y)
#data [;,:-1] all rows and all columns
#expected rows and last column
#data[;,-1] taking all rows (:)
#but keeping  thelast  column(-1)

##############################################
#broadcast scaler to one dimensional array
from numpy import array
#define array
a=array([1,2,3])
a
#define scaler
b=2
b

#broadcast
c=a+b
c
###########################
#vector  addtiton
from numpy import array

#define first array
a=array([1,2,3])
a

#define second array
b=array([1,2,3])
b
#add vector
c=a+b
c
################################
#vector subtraction
from numpy import array

#define first array
a=array([1,2,3])
a

#define second array
b=array([1,2,3])
b
#sub vector
c=a-b
c
########################################
#vector multiplication
from numpy import array

#define first array
a=array([1,2,3])
a

#define second array
b=array([1,2,3])
b
#add vector
c=a*b
c
###############################
#vector division
from numpy import array

#define first array
a=array([1,4,3])
a

#define second array
b=array([1,2,3])
b
#add vector
c=a/b
c
######################################
#vector L1 norm
#L1 norm -The L1 norm of a vector is calculated by summing up the absolute values of its components.
#L2 =The L2 norm of a vector is calculated by taking the square root of the sum of the squares of its components.

from numpy import array 
from numpy.linalg import norm

a=array([1,2,3])
a
#calculate norm
l1= norm(a,1)
l1

########
#L2 norm
from numpy import array 
from numpy.linalg import norm

a=array([1,2,3])
a
#calculate norm
l2= norm(a)
l2

b=array([1,2,-3,-4])
b

l1=norm(b,1)
l1

l2=norm(b)
l2
#############################################
#Triangular  matrices
#Below Diagonal matrix => Upper (triu) matrix
#Above Diagonal Matrx  => Lower (tril) matrix
#in below Diagonal matrix= 1,5,9
from numpy import array
from numpy import tril
from numpy import triu

M=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
M
#lower Trinagular matrix
'''
In a lower triangular matrix, all the entries 
above the main diagonal 
(including the main diagonal itself) are zero.
Only the entries below the main diagonal are
 non-zero.
'''
lower=tril(M)
lower


##lower Trinagular matrix
'''
In an upper triangular matrix, all the entries
 below the main diagonal 
 (including the main diagonal itself) are zero.
Only the entries above the main diagonal
 are non-zero.

'''
upper=triu(M)
upper
##################################
#Diagonal Matrix=the main diagonal consists of the elements where the row index is equal to the column index.
from numpy import array
from numpy import diag
#define square matrix
M=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
M
#extract diagonal vector
d=diag(M)
d
#Extract diagpnal from vector
D = diag(d)
D

#############################
#identity matrix=In which all elements of the main diagonal are ones, and all other elements are zeros.
import numpy as np

# Specify the size of the identity matrix (n x n)
n = 3

# Create the identity matrix using np.eye()
I= np.eye(n)

print("Identity Matrix:")
print(I)

#################################3
#orthogonal matrix
from numpy import array 
from numpy.linalg import inv
#Define Orthogonal matrix
Q=array([
    [1,0],
    [0,-1]])
Q
#inverse equivalence
V=inv(Q)
print(Q.T)
print(V)
#identity Euivalance
I=Q.dot(Q.T)
print(I)
