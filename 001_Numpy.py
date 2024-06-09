# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:09:28 2023

@author: Vaishnavi
"""

#          ARRAY NUMPY
#pip install numpy
#using conda=>conda install numpy

#open scource
#homogenous= data type must be same in list
#consist multidimensional array
#objects and a collection of routines 

#################################################
#creating numpy array 
import  numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
################
#create multidimensional array
import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8],[4,6,7,8]])
print(arr)
#####################
#use of ndmin parameter to sepcify how many dimensios
#you need to create arraay
arr =np.array([1,2,3,4],ndmin=2)
arr
#####
a=np.array([2,3,45,8],ndmin=3)
a
################
#make complex data type of given array
arr=np.array([1,2,3,4],dtype=complex)
arr

###############
#find dimension of array
#note= to check the dimension of array we use ndim
arr=np.array([[1,2,3,4],[3,4,56,6],[23,4,5,6]])
print(arr.ndim)
print(arr)
##############
#find the size of array
#arr.itemsize
arr=np.array([2,4,5,5])
print("Size of array:",arr.itemsize)
################
#to check the data type of array
arr=np.array([2,3,4])
print(arr.dtype)
#############3
#to check the size and shape of array
arr=np.array([[1,2,3],[3,4,5]])

print("shape of array is:",arr.shape)
print("size of array is:",arr.size)
#my way
a1=arr.shape
a1
a2=arr.size
a2
##################
#                       INDEXING

#arange() => create sequence of integer using arange()
#step is 3: then => 0  3 6 9 12 15 18

#
arr=np.arange(11)
arr
print(arr[2])
####
print(arr[-2])
###
print([-5])
#####################
#multidimensional array indexing
#access multi-dimensional  array element
#using array indexing
arr=np.array([[1,2,3,4],[4,5,6,7]])
arr
arr.shape

########################
#accessing element 
print(arr[1,1])
###
arr[0,3]
###
print(arr[1,-1])
########################################3
#access element using slicing
#start ,stop ,step

arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]
x
########
#Accessing element  start -2 end 3 and step -1
x=arr[-2:3:-1]
x
#####
x=arr[-2:10]
x
#################################################

#               Slicing array

#for multi dimensional numpy array

#R.R
multi_arr=np.array([[10,20,30,30,40],
                    [20,40,70,80,90],
                    [10,20,30,40,60],
                    [10,20,30,50,70]
                    ])
multi_arr
######
#Accessing 1 row and 2 column
multi_arr[1,2]
#R.R
#Accessing 1 row and all columns
multi_arr[1,:]
multi_arr[:,1]

#columns from 0 to 3 and in all selected rows
#R.R
x=multi_arr[:3,::2]
x
#######
##################################################3
#Integer Array indexing

arr=np.arange(35).reshape(5, 7)
arr
#it will print  5 rows and 7 column
###################################################

#           BOOLEN ARRAY OF INDEXING

#here we have to pass true or false to access the rows and column
arr=np.arange(12).reshape(3,4)
print(arr)
#
rows=np.array([False,True,True])
wanted_rows=arr[rows, :]
wanted_rows
####################################################

        #convert Numpy array to python list
#
#tolist() method is used in converting

#convert one dimendimensional to array of list
########
array=np.array([10,20,30,40])
array
print(type(arr))
######

#convert array to list

lst=array.tolist()
lst
print(type(lst))
############################
#Convert multidimensional array to list

array=np.array([[10,20,30,40],
                [50,60,70,80],
                [60,70,80,80]
                ])
array
type(array)
#convert it
lst=array.tolist()
print('list is:',lst)
type(lst)
##############################################

#numpy privide us with two function to use
#when converting a list into a array

#numpy.array()
#numpy.asarray()

#numpy.array() : using numpy.array()
#this function of the company

#create list
list=[10,2,3,4]
#convert array
array=np.array(list)
array

#######
#numpy.asarray()

#use asarray()=> this funtion calls

list=[20,30,40,50]
array=np.asarray(list)
print("Array",array)
print(type(array))
##########################################################

#               Array Properties

#  array.shape
#  array.size
#   array.resize
#   array.reshape


arr=np.array([1,2,3])
arr.shape
print(arr)
################
#Resize of array
array=np.array([[1,2,3],[2,3,4]])
array.shape=(3,2)
array
#####################
#Reshape of array
array=np.array([[1,2,3],[2,3,4]])
array.reshape=(3,2)
array
#####
#######################################################


