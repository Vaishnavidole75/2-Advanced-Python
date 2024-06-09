# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 15:26:42 2023

@author: Vaishnavi
"""

#               PANDAS DATAFRAME
#null is not allow
#it is immutable,hitrogrneous
# 2 dimensinal
#it hvae labeled axes rows and column

#check the version of pandas
import pandas as pd
pd.__version__
############

#  imp
#create using constructor
#create pandas dataframe using list in list
import pandas as pd
technologies=[['spark',2000,'30days'],
              ['pandas',2000,'40days']
              ]
df=pd.DataFrame(technologies)
df

#in above program we doesn't assgin labels to column
#indexes  is assign by defalut to column and rows (i.e  0,1,2) 
#both rows and columns are called index

################
column_names=["courses","fee","Discount"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
df
###df.dtypes to check type of data
df.dtypes
#########################################
#professinal way to create dataframe
import pandas as pd
technologies={
    'Courses':['spark','hadoop','pyspark','python','java'],
    'Fee':[80000,90000,5000,6000,3400],
    'Duaration':['30days','20days','50days','56days','20days'],
    'Discount':[11.8,78.8,78.9,76.8,56.7]  
    }
df=pd.DataFrame(technologies)
print(df.dtypes)

####################################################

#       DATA PROCESSING 
#v.v.imp
# all R.R
#for string .astype(str)
#numeric => pd.to_numeric()
#integer => .astype(int)
#############################
#convert object to string
df2=df.convert_dtypes()
df2.dtypes
#change all columns to same type
df=df.astype(str)
df.dtypes
#change type for one or multiple columns
df= df.astype({"Fee":int,"Discount":float})
df.dtypes
#convrt data type for all column in a list

df= pd.DataFrame(technologies)
df.dtypes
cols=['Fee','Discount']
df[cols]=df[cols].astype('float')
df.dtypes

#ignore error 

df=df.astype({"Courses":int},errors='ignore')
df.dtypes
#genearte error
df=df.astype({"Courses":int},errors='raise')
#convert feed column to numeric type
df=df.astype(str)
df


import pandas as pd
technologies={
    'Courses':['spark','hadoop','pyspark','python','java'],
    'Fee':[80000,90000,5000,6000,3400],
    'Duaration':['30days','20days','50days','56days','20days'],
    'Discount':[11.8,78.8,78.9,76.8,56.7]  
    }
df=pd.DataFrame(technologies)
print(df.dtypes)

df1=df.astype(str)
print(df1.dtypes)


