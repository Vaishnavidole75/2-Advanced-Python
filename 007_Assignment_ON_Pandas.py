# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 14:05:40 2023

@author: Vaishnavi
"""
#             ASSIGNMENT
#python program to create series &display one dimensional array line
#containing an array of data
import pandas as pd
ds=pd.Series([1,2,3,4,5])
ds
#####################
#write a python program to convert a panda module series
#to python list and it's type

#R.R 
import pandas as pd
ds=pd.Series([1,2,3,4,5])
print("pandas series and type")
ds
type(ds)
print("Convert pandas seires to python list")
print(ds.tolist())
print(type(ds.tolist()))
#################################
#write python program to add,subtract,multiple and
import pandas as pd
ds1=pd.Series([1,2,3,4,5])
ds2=pd.Series([2,4,6,8,7])
#Addition
ds=ds1+ds2
print("Addtion of Sereies",ds)
ds=ds1-ds2
print("Subtraction of Sereies",ds)
#Multiplication
ds=ds1*ds2
print("Multiplication of Sereies",ds)
#division
ds=ds1/ds2
print("Division of Sereies",ds)
############################################

#Write a python program to compare element of series

import pandas as pd
ds1=pd.Series([1,2,3,4,5])
ds2=pd.Series([2,4,6,8,7])

print("Series 1:")
ds1

print("Series 2:")
ds2

print("Compare TWO SERIES:")

print("Equals",ds1==ds2)
print('greater than:',ds1>ds2)
print('Less than:',ds1<ds2)
########################################
#write python program to convert into dictionary to A pandas series

import pandas as pd
d1={'a':100,'b':200,'c':233}
print("original dictionary is:",d1)

new_series=pd.Series(d1)
print("Converted Series is:")
new_series
####################################33
#write a python program to convert Numpy array to pandas series

import numpy as np
import pandas as pd

n_a=np.array([10,20,30,40,50])
print("NumPy Array is:")
n_a

new_series=pd.Series(n_a)
print("Converted Series is:")
new_series
#####################################################

#write a program to change the data type of given column or a series

import pandas as pd

s1 =pd.Series(['100','200','300','python','300.12','400'])
print("Original Series is:",s1)

print("Change the given data type into numeric type")

s2=pd.to_numeric(s1,errors='coerce')
s2
#############################################

#Write a python program to convert the first column of dataframe as a series

import pandas as pd

d={'col1':[1,2,3,4],
   'col2':[5,6,7,8],
   'col3':[9,10,12,11]
   }
df=pd.DataFrame(d)
df

s1=df.iloc[:,0]
print("\n First column as a series")
s1
type(s1)

###############################################

import pandas as pd

s= pd.Series([
    ['a','b','c'],
    ['d','e','f'],
    ['g','g','h']])
print(s)

s1=s.apply(pd.Series)
s2=s1.stack()
s3=s2.reset_index(drop=True)
s3
#above code in single line
import pandas as pd

s= pd.Series([
    ['a','b','c'],
    ['d','e','f'],
    ['g','g','h']])
print(s)

s=s.apply(pd.Series).stack().reset_index(drop=True)
s

#Stack() is used to stack the prescribed level(s) from columns to index
#################################################################

