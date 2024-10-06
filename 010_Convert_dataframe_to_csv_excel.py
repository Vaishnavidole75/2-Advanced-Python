# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 09:25:27 2023

@author: Vaishnavi
"""
#         Convert Dataframe to Csv 

import pandas as pd
technologies={
    'Courses':['spark','hadoop','pyspark','python','java'],
    'Fee':[80000,90000,5000,6000,3400],
    'Duaration':['30days','20days','50days','56days','20days'],
    'Discount':[11.8,78.8,78.9,76.8,56.7]  
    }
df=pd.DataFrame(technologies)
df
##convert dataframe to csv
df.to_csv('data_file.csv')
df
#to convert dataframe to excel
df.to_excel("111newwwww.xlsx")
df
##########################
#create dataframe from csv file

df=pd.read_csv('data_file.csv')
df
##########################################################################

#pandas dataframe =>  BASIC opertion
#exploaratary data analysis
#create dataframw with none /null value and space

import pandas as pd
import numpy as np
technologies={
    'Courses':[None,'hadoop','pyspark','python','java'],
    'Fee':[80000,90000,5000,6000,3400],
    'Duaration':['30days','20days',' ','56days','20days'],
    'Discount':[11.8,78.8,78.9,76.8,56.7]  
    }
row_label=['r0','r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=row_label)
df
#Opertions
#########################################
#Dataframe Properties
df.shape
#above opertion return rows and column
########
df.size
#total rows and column
######
df.columns
#total column
df.columns.values
#total column &its value
df.index
#return index
df.dtypes
#return datatypes of column

#########################################
#Accessing one column contents
df['Fee']
#Accessing two columns contents
df[['Fee','Duaration']]
#in above code when we access 2 or more columns need to give 2 square bracket
#select certain rows and assign it to another dataframe
df2=df[4:]
df2
### my practice
fd=df[:4]
fd
#
df3=df[2:4]
df3
#
df4=df[:-2]
df4
######################
#accessing certain cell from column 'Duration'
df['Duaration'][3]
#subtracting  specific value from a column
df['Fee']=df['Fee']-500
df['Fee']
##################################################

# pandas Manipulate Dataframe

#Describe dataframe
#Describe dataframe for all numberic column
df.describe()
#it shows 5 number summary
######################################
#rename() method 
import pandas as pd

technologies={
    'Courses':[None,'hadoop','pyspark','python','java'],
    'Fee':[80000,90000,5000,6000,3400],
    'Duaration':['30days','20days',' ','56days','20days'],
    'Discount':[11.8,78.8,78.9,76.8,56.7]  
    }
row_label=['r0','r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=row_label)

#Rename the column
df.columns=['a','b','c','d']
df

#rename column name using rename() method
#imp
#axix=1=>column
#axis=0=>rows
df=pd.DataFrame(technologies,index=row_label)
df.columns=['A','B','C','D']
df
df2=df.rename({'A':'C1','B':'C2'},axis=1)
df2
df2=df.rename({'C':'C3','D':'C4'},axis="columns")
df2
df2 =df.rename(columns={'A':'C1','B':'C2'})
df2               
########################################################


#Drop column by name
#drop fee column
df2=df.drop(['Fee'],axis=1)
df2
###################################


#also use columns insted of labels'
df2=df.drop(labels=['Fee'],axis=1)
df2
###################################

#drop columns by index
print(df.drop(df.columns[1],axis=1))

df=pd.dataFrame(technologies)

####################################

#using implace=true
df.drop(df.columns[2],axis=1,inplace=True)
df
#####################################

df=pd.dataFrame(technologies)
#Drop two or more columns by lables name
df2=df.drop(["Courses","Fee"],axis=1)
df2

#######################################

#drop two or more columns by index
df=pd.dataFrame(technologies)
df2=df.drop(df.columns[[0,1]], axis=1)  #it will delete columns by 0 n 1
df2
