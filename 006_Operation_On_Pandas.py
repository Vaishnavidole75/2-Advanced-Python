# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 14:26:42 2023

@author: Vaishnavi
"""

#To check the version of pandas

import pandas as pd 
pd.__version__
#########################
#Create using constructor
#create pandas DataFrame from list
import pandas as pd
technologies=[["spark",2000,"30days"],
              ["pandas",2000,"40days"],
              
              ]
df=pd.DataFrame(technologies)
print(df)
#####################
#for labeling the dataframe in pandas
#write this code in ready refernce material
column_names=["courese","fees","Duration"]
row_label=("a","b","c")
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)
##############
#check the datatypes of code
df.dtypes
#############
types={'courses':str,'fee':float,'Duration':str}
df.dtypes
###############
##create DataFrame from dictionary
technologies={
    "courses":["spark","pyspark","hadoop"],
    'fee':[30000,4000,5000],
    'Duration':['30days','40days','50days'],
    ' Discount':[1000,2500,1500]  
    }
df=pd.DataFrame(technologies)
df
###############
#
import pandas as pd
df=pd.read_csv('data_file.csv')

#Create Dataframe to csv
import pandas as pd
df.to_csv('c:/1-python/data_file.csv')
#############
#Create DataFrame from csv absolute path(check the path name is right or wrong)
import pandas as pd
df=pd.read_csv('data_file.csv')
#####################
#create dataframe from csv file using relative path
import pandas as pd
df = pd.read_csv('c:/1-python/data_file.csv')
############################################
#create DataFrame with none /null to work with example
import pandas as pd
import numpy as np
technologies=({
    'courses':["spark","hadoop","python","spark",None,"z","x","a"],
    'fee':[2200,24000,23000,np.nan,1500,3400,56000,12000],
    'Duration':['30days','40days','40days','40days','40days','40days','40days','40days']
            
     })
row_label=['r1','r2','r3','r4','r5','r6','r7','r8']
df=pd.DataFrame(technologies,index=row_label)
print(df)
######################3
#DataFrame properties
df.shape
#(8,4)
df.size
#32
df.columns

df.columns.values
df.index
df.dtypes
##############################################
#Accessing for single element
df['fee']
#Accessing column content more contetnt element
df[['fee','Duration']]
###########
#accessing sertain rows and columns items
df2=df[6:]
df2

df3=df[:3]
df3

df4=df[:2]
df4
##############3
#accessing certain column  'Duration
df['Duration'][3]
##################
#subtracting specific value from a column
df['fee']=df['fee']-500
df['fee']
##################
###describe dataframe
df.describe()
########3
#rename dataframe columns

df = pd.DataFrame(technologies,index=row_labels)
################
#assign new header by setting new column names
df.colmuns["A","b","c","d"]
df
####################
#rename column name  using rename() method

