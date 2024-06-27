# -*- coding: utf-8 -*-
"""
Created on Fri May 12 16:54:36 2023

@author: Vaishnavi
"""

###############################################################################################################

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np 

sns.__version__
###############################################################################################################

sns.get_dataset_names()   #list of datasets
df = sns.load_dataset('titanic')

df

df.head()

df.columns

df['pclass']
###############################################################################################################

sns.countplot(x='sex',data=df)

sns.countplot(x='sex',hue='survived',data=df)
sns.countplot(x='sex',hue='pclass',data=df,palette='Set1')
plot = sns.countplot(x='sex',hue='age',data=df,palette='Set2')

###############################################################################################################

sns.kdeplot(x='age',data=df,color='black')

sns.displot(x='age',kde=True,bins=21,data=df,hue=df['pclass'], palette='Set1') #bins is the number of bars

###############################################################################################################

df = sns.load_dataset('iris')

df
df.columns

sns.displot(x='petal_length',kde=True,bins=9,data=df,hue=df['species'],palette='Set1') 

sns.displot(x='sepal_length',kde=True,bins=9,data=df) 

sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')

sns.scatterplot(x='petal_length',y='sepal_length',data=df,hue='species')
###############################################################################################################

'''
in between 0-2 (petal length): setosa
in between 3-5 (petal length): versicolor
in between 5-7 (petal length): verginica

in between 1-6 (sepal length): setosa
in between 4.7-7.2 (sepal length): versicolor
in between 4.7-8.0 (sepal length): verginica
'''

###############################################################################################################

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg')

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='kde')

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='hist')

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='scatter')

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='resid')

#######################################################################################################################

sns.pairplot(data=df)

###############################################################################################################

#generating heatmap for correlation

corr = df.corr()
corr

sns.heatmap(corr)

###########################################################################################################################################################################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

###############################################################################################################

#reading file
cars = pd.read_csv('cars.csv')
cars

###############################################################################################################

sns.boxplot(cars)

min(cars.Index)
max(cars.Index)

cars.describe()

###############################################################################################################

plt.hist(cars.speed)   
plt.hist(cars.dist)    #distance is right skewed

#kernel density
sns.displot(x='speed',kde=True,bins=5,data=cars)
sns.displot(x='dist',kde=True,bins=5,data=cars)
sns.displot(x='speed',kde=True,bins=5,hue=cars.dist,data=cars,palette='Set2')

###############################################################################################################
plt.bar(cars.speed,cars.dist)

cars.speed
sns.kdeplot(x='speed',data=cars)

sns.countplot(x='speed',data=cars)

sns.countplot(x='speed',hue='dist',data=cars)

cars.groupby('speed').count()
cars

sns.scatterplot(x='speed',y='dist',hue='Index',data=cars)

###############################################################################################################

'''
RUGHT SKEW:
    in right skew data the graph is more populated to the left i.e we see depression towards right
    higher values to left and lower values to the right
    
LEFT SKEW:
    in left skew data the graph is more populated to the right i.e we see depression towards left
    higher values to right and lower values to the left
'''

#when there are outliers we need to calculate 'median'
###############################################################################################################

sns.boxplot(cars.speed)
sns.boxplot(cars.dist)

#first box for mean/median

###############################################################################################################

corr = cars.corr()
corr
sns.heatmap(corr)

###############################################################################################################

speed from scipy.stats import skew
from scipy.stats import kurtosis

###############################################################################################################

l = [skew(speed),skew(dist),kurtosis(speed),kurtosis(dist)]
l

skew(speed)
sk= cars.speed.tolist()
dist = cars.dist.tolist()

###############################################################################################################

ew(dist)

kurtosis(speed)
kurtosis(dist)

skew(dist)
skew(dist,axis=0,bias=True)
skew(dist,axis=1,bias=True)
skew(dist,axis=0,bias=False)



























