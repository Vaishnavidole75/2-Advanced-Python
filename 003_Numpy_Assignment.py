# -*- coding: utf-8 -*-
"""
Created on  Wed May 12 15:14:08 2023

@author: Vaishnavi
"""
#           ASSIGNMENT

#write numpy program to get numpy version and show numpy

import numpy as np
print(np.__version__)

#################################################

#write numpy program to test whether
#none of the elements of agiven array are zero

import numpy as np
x=np.array([1,2,3,4])
print("Original arraay:")
print(x)
print("Test if none of the element of the said array is zero:")
print(np.all(x))

x=np.array([0,1,2,3])
print("Original arraay:")
print(x)
print("Test if none of the element of the said array is zero:")
print(np.all(x))

######################################################

#write numpy program to test if 
#any of the element of the given array are non-zero
x=np.array([1,0,0,0])
print("Original arraay:")
print(x)
print("Test whether any of the element of a given  array is non zero:")
print(np.any(x))

x=np.array([0,0,0,0])
print("Original arraay:")
print(x)
print("Test whether any of the element of a given  array is non zero:")
print(np.any(x))

########################################################

#write numpy program to test a given array
#element-wise for finiteness (not infinity ornot a number)
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print("Original array")
print(a)
print("Test a given array element-wise for finiteness :")
print(np.isfinite(a))

##########################################################

#write a numpy progrm to test element wise for NaN of given array
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print("Original array")
print(a)
print("Test element-wise for NaN:")
print(np.isnan(a))

#############################################################

#write numpy program to crate an element-wise
#comparison (grether,grether_equal,less,less_equal)
#of two given array

import numpy as np
x=np.array([3,5])
y=np.array([2,5])
print("Original numbers:")
print(x)
print(y)
print("Comparison - greater")
print(np.greater(x,y))
print("Comparison - greater_equal")
print(np.greater_equal(x,y))
print("Comparison - less")
print(np.less(x,y))
print("Comparison - less_equal")
print(np.less_equal(x,y))

##############################################################

#write numpy program to create 3X3 identity matrix
import numpy as np
array_2D=np.identity(3)
print('3X3 matrix:')
print(array_2D)

##############################################################

#write a numpy program to generate random number between  0 and 1
import numpy as np
rand_num=np.random.normal(0,1,1)
print("Random number between 0 and 1:")
print(rand_num)

#############################################################

#write numpy program to create 3X4 array and iterate it
import numpy as np
a=np.arange(10,22).reshape((3,4))
print("Original array:")
print(a)
print("Each element of array is:")
for x in np.nditer(a):
    print(x,end=" ")
    print()
    
###############################################################

#write numpy program to crate a vector of length 5
#with value evenly distribution br between 10 to 50

import pandas as pd #check the line space numpy
v=np.linspace(10,49,5)
#10 is starting ,49 is ending pt,5-no in vector
print("length 10 with values evenly distruted between 10 to 50:")
print(v)

################################################################

#write numpy program to create 3X3 matrix
#with values ranging from 2 to 10

import numpy as np
x=np.arange(2,11).reshape(3,3)
print(x)

#################################################################

#write numpy program to Reverse an array
#(the first element between the last)
import numpy as np
x=np.arange(12,38)
print("Original array:")
print("Reverse array:")
x=x[::-1]
print(x)

##################################################################

#write numpy program to compute the multiplication to given matrix

import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("Original matrix")
print(p)
print(q)
result1=np.dot(p,q)
print("Result of the said matrix multiplication:")
print(result1)

##################################################################

#write numpy program to compute 
#the cross product of two given vectors

import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("Original matrix")
print(p)
print(q)
result1=np.cross(p,q)
result2=np.cross(q,p)
print("cross product of the said two vector(p,q):")
print(result1)
print("cross product of the said two vector(q,p):")
print(result2)

#################################################################

#write numpy program 
#to compute determinant of a given square array

import numpy as np
from numpy import linalg as LA
a=np.array([[1,0],[1,2]])
print("Original 2-d array")
print(a)
print("Determinant of the said 2-D array:")
print(np.linalg.det(a))

#################################################################

#write numpy program to
#to compute eigen value and eigen vector
#of a given square array
import numpy as np
m=np.mat("3 -2; 1 0")
m
print("Orginal matrix:")
print("a\n",m)
w,v=np.linalg.eig(m)
print("Eigenvalues of the said matrix",w)
print("Eigenvectors of the said matrix",v)

################################################################

#write a numpy program to compute
#the inverse given matrix
import numpy as np
m=np.array([[1,2],[3,4]])
print("Original matrix:")
print(m)
result=np.linalg.inv(m)
print("Inverse of said the matrix:")
print(result)

#################################################################
import matplotlib.pyplot as plt

# Creating a line
x = np.linspace(-5, 5, 100)
y = 2 * x + 1

# Plotting the line
plt.plot(x, y, label='y = 2x + 1')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Equation of a Line in 2D')
plt.legend()
plt.grid(True)
plt.show()


# Diagonal Matrix
diag_matrix = np.diag([2, 4, 6])

# Scalar Matrix
scalar_matrix = 3 * np.eye(3)

# Identity Matrix
identity_matrix = np.eye(3)

print("Diagonal Matrix:")
print(diag_matrix)
print("\nScalar Matrix:")
print(scalar_matrix)
print("\nIdentity Matrix:")
print(identity_matrix)
