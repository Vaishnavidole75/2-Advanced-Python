# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 13:20:40 2023

@author: Vaishnavi
"""

import pandas as pd
technologies={
    'Courses':['spark','a','b','c','d','e','f'],
    'Fee':[100,2,300,4000,500,560,67],
    'Duration':['12days','12days','12days','12days','12days','12days','12days'] ,
    'Discount':[12,23,43,45,12,23,45]
    }
df=pd.DataFrame(technologies)
print(df)
# Drop Column by Name
# Drops "Fee" column
df2 = df.drop(["Fee"], axis = 1)
print(df2)

# Explicitly using parameter name 'labels'
df2 = df.drop(labels=["Fee"], axis = 1)

# Alternatively use columns instead of labels.
df2 = df.drop(columns=["Fee"], axis = 1)
###########################
# Drop column by index.
print(df.drop(df.columns[1], axis = 1))

df = pd.DataFrame(technologies)

#drop coloumns from list of colimns
import pandas as pd
df=pd.DataFrame(technologies)
lisCol=["Courses","Fee"]
df2=df.drop(lisCol,axis=1)
print(df2)

##################################3
import pandas as pd
technologies={
    'Courses':['spark','a','b','c','d','e','f'],
    'Fee':[100,2,300,4000,500,560,67],
    'Duration':['12days','12days','12days','12days','12days','12days','12days'] ,
    'Discount':[12,23,43,45,12,23,45]
    }
df=pd.DataFrame(technologies)
print(df)

#to count the length of rows( rows=0)
rows_count =len(df.index)
rows_count

rows_count=len(df.axes[0])
rows_count
# to count rows
df=pd.DataFrame(technologies)
rows_count=df.shape[0]
rows_count=df.shape[1]
print(rows_count)
#####################################

#apply() function on column

import pandas as pd
import numpy as np 
data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }
df=pd.DataFrame(data)
df

#For addition opertion using apply() method
def add_3(x):
    return x+3
df2=df.apply(add_3)
df2

#using apply function on single column

def add_4(x):
    return x+4
df["B"] =df["B"].apply(add_4)
df["B"]

#need to enterd double square bracket

#Apply to multiple column

df[['A','B']]=df[['A','B']].apply(add_4)
df

#Using lambdA function on multiple column
#imp  

df2=df.apply(lambda x:x+10)
df2

#on single column usign lambda function on DataFrame

df["A"]=df["A"].apply(lambda x:x-2)
df


###Using transform()  method
def add_2(x):
    return x+2
df2=df.transform(add_2)
df2

#map method() using lambda function
df["A"]=df["A"].map(lambda x:x/2)
df

df2=df.map(lambda x:x+10)
df2
#################################
#numpy package functions
#IT Is feature of numpy
import Numpy as np
df["C"]=df["C"].apply(np.square)
df

#DIRECTLY using np as numpy method
#it is feature of pandas
df["B"]=np.square(df['B'])
df

########################

#using groupby() method
import pandas as pd
technologies={
    'Courses':['spark','a','b','c','a','b','c'],
    'Fee':[100,200,300,200,500,560,67],
    'Duration':['12days','12days','12days','12days','12days','12days','12days'] ,
    'Discount':[12,23,43,45,12,23,45]
    }
df=pd.DataFrame(technologies)
print(df)



#using groupby() summation of courses column
#every time we have to use .sum() method
df2=pd.groupby(['Courses']).sum()
df2

#for 2column

df2=df.groupby(['Courses','Duration']).sum()
df2


#
df2=df.groupby(['Courses','Duration']).sum().reset_index()
df2

###################
import pandas as pd
technologies={
    'Courses':['spark','a','b','c','d','e','f'],
    'Fee':[100,2,300,4000,500,560,67],
    'Duration':['12days','12days','12days','12days','12days','12days','12days'] ,
    'Discount':[12,23,43,45,12,23,45]
    }
df=pd.DataFrame(technologies)
print(df)
#to print name of columns
df.columns

#2nd another way to print of column name
column_headers= list(df.columns.values)
print("the column header",column_headers)

#3rd way
column_headers=list(df.columns)
column_headers

#4th way
column_headers=list(df)
column_headers

######################################3333####################
#sudffel in DataFrame

import pandas as pd
technologies={
    'Courses':['spark','a','b','c','d','e','f'],
    'Fee':[100,2,300,4000,500,560,67],
    'Duration':['12days','12days','12days','12days','12days','12days','12days'] ,
    'Discount':[12,23,43,45,12,23,45]
    }
df=pd.DataFrame(technologies)
print(df)

###shuffling on DataFrame rows

df1=df.sample(frac=1)
df1

#create a new dataFrame starting from zero
df1=df.sample(frac=1).reset_index()
df1

#To getting original dataframe and want old datafram for that drop=True
df1=df.sample(frac=1).reset_index(drop=True)
df1
###############################################################


import pandas as pd
technologies={
    'Courses':['spark','a','b','c','d','e','f'],
    'Fee':[100,2,300,4000,500,560,67],
    'Duration':['12days','12days','15days','18days','19days','11days','12days'] ,
    'Discount':[12,23,43,45,12,23,45]
    }

index_label=['r1','r2','r3','r4','r5','r6','r7']
df1=pd.DataFrame(technologies,index=index_label)


technologies2={
    'Courses':['spark','a','b','c','d','e','f'],
    'Discount':[12,23,43,45,12,23,45]
    }
    
index_label=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies2,index=index_label)
