# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 09:09:05 2023

@author: mukta
"""


#create dataframe from dictionary
import pandas as pd

technologies={
    'Courses':["spark","pyspark","Hadoop"],
    'Fee':[2200,3400,5400],
    'Duration':['30days','34days','36days'],
    'Discount':[100,400,500]
    }

df=pd.DataFrame(technologies)
df

################################

#convert dataframe to csv

df.to_csv('data_file.csv')   #relative path

################################

#create dataframe from csv

df=pd.read_csv('data_file.csv')

#################################

#pandas dataframe- basic operation
#create dataframe from  none/null to work with example

import pandas as pd
import numpy as np
technologies=({
    'Courses':["spark","pyspark","Hadoop","python","pandas","None","sparks","python"],
    'Fee':[2200,3400,5400,1209,np.nan,4372,4573,3455],
    'Duration':['30days','34days','36days','72days','10days','60days','90days','78days'],
    'Discount':[100,400,500,700,200,500,600,900]
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
df

######################################

#Dataframe properties
df.shape
#(8,4)
###############

df.size
#32
###############


df.columns
###########

df.columns.values
###########

df.index
###########

df.dtypes
###############################

#Accessing one column contents
df['Fee']
#######################

df.info
########################

#Accessing two column
df[['Fee','Duration']]
#################

#select certain rows and assign it to another dataframe
df2=df[6:]
df2
############################

#Accessing certain value from column duration
df['Duration'] [3]
############################

#subtracting specific value from a column
df['Fee']=df['Fee']-500
df['Fee']
#############################

#pandas to manipulate dataframe
#describe dataframe
#describe dataframe for all numberic columns
df.describe()
#it will show 5 numbers summary

###############################

#rename() - Rename pandas dataframe columns
df=pd.DataFrame(technologies, index=row_labels)
df
###############################

#Assign new header by setting new column names
df.columns=['A','B','C','D']
df
##############################

#Rename column Names using rename() method
df=pd.DataFrame(technologies, index=row_labels)
df.columns=['A','B','C','D']
df
df2=df.rename({'A':'c1','B':'c2'}, axis=1)   ##column vr apply hot mnum axis=1
df2
df2=df.rename({'C':'c3','D':'c4'}, axis='columns')
df2
df2=df.rename(columns={'A':'c1','B':'c2'})
df2

##############################

df2=df.rename({'A':'c1','B':'c2','C':'c3','D':'c4'}, axis=1)
df2

###############################

#Drop dataframe rows and column
df=pd.DataFrame(technologies,index=row_labels)
df
###############################

#Drop rows by labels
df1=df.drop(['r1','r2'])
df1
################################

#Delete rows by position / index
df1=df.drop(df.index[1,2])
df1
###############################

#Delete rows by index range
df1=df.drop(df.index[2:])
#############################

#when u have default index for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1
df=pd.DataFrame(technologies)
df1=df.drop([0,3])   #it will delete rows0 n row3
df1=df.drop(range(0,2))  #it will delete 0 and 1
################################

#Droping of columns
import pandas as pd
technologies=({
    'Courses':["spark","pyspark","Hadoop","python","pandas","None","sparks","python"],
    'Fee':[2200,3400,5400,1209,np.nan,4372,4573,3455],
    'Duration':['30days','34days','36days','72days','10days','60days','90days','78days'],
    'Discount':[100,400,500,700,200,500,600,900]
    })
df=pd.DataFrame(technologies)
df

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

########################################

#drop columns from list of columns
df=pd.dataFrame(technologies)
lisCol=["Courses","Fee"]
df2=df.drop(lisCol,axis=1)
df2
###########################################

#

import pandas as pd
import numpy as np
technologies=({
    'Courses':["spark","pyspark","Hadoop","python","pandas","None","sparks","python"],
    'Fee':[2200,3400,5400,1209,np.nan,4372,4573,3455],
    'Duration':['30da\ys','34days','36days','72days','10days','60days','90days','78days'],
    'Discount':[100,400,500,700,200,500,600,900]
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
df

#df.iloc[start row:end row, start column:end column]

df=pd.DataFrame(technologies, index=row_labels)
#Below are quick example
df2=df.iloc[:, 0:2] # : indicated all rows and column upto 2
df2

######################################

df2=df.iloc[0:2, :] #in this 0:2 show 0 and 1 rows and : show all coumns
df2

######################################

df3=df.iloc[1:2, 1:3] 
df3

#######################################

df3=df.iloc[:, 1:3]   # : show all rows and 1:3 show 1 and 2 columns
df3
########################################

df2=df.iloc[[2,3,6]]  #select rows by index list
df2
df2=df.iloc[1:5]      #select rows by integer index range means select rows 1 to 4 
df2
df2=df.iloc[:1]        #first rows
df2
df2=df.iloc[:3]        #select first 3 rows
df2
df2=df.iloc[-1:]       #select last rows
df2
df2=df.iloc[-3:]       #select last 3 rows
df2
df2=df.iloc[::2]       #select alternate rows
df2

################################################

#select rows by index labels
df2=df.loc['r2']      #select rows by index means select r2 row
df2
df2=df.loc[['r2','r3','r6']]  #select r2, r3, r6 rows
df2
df2=df.loc['r1':'r5']  #select rows from r1 to r5
df2
df2=df.loc['r1':'r5':2]  #select alternate rows
df2

##################################################

import pandas as pd
import numpy as np
technologies=({
    'Courses':["spark","pyspark","Hadoop","python","pandas","None","sparks","python"],
    'Fee':[2200,3400,5400,1209,np.nan,4372,4573,3455],
    'Duration':['30days','34days','36days','72days','10days','60days','90days','78days'],
    'Discount':[100,400,500,700,200,500,600,900]
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
df

#select multiple columns
df2=df.loc[:, ["Courses","Fee","Duration"]]
df2
#########################

#select random columns
df2=df.loc[:, ["Courses","Fee","Discount"]]
df2
############################

#select column between two columns
df2=df.loc[:, 'Fee':"Discount"]
df2
#############################

#select column by range
df2=df.loc[:,"Duration":]
df2
#########################

#select all xolumns upto duration
df2=df.loc[::, "Duration"]
df2