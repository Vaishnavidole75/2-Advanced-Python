# -*- coding: utf-8 -*-
"""
Created on Fri May 12 16:54:36 2023

@author: Vaishnavi
"""

#        1           MATPLOTLIB

#To install library - pip install matplotlib
#Used in data visulasation
#Provide GUI Toolkit  like Tkinter, wxPython, Qt, or GTK.

######################################################
#plot a graph
import matplotlib.pyplot as plt

plt.plot([1,3,2,4])
plt.show()
#O/P - Line graph
######

import matplotlib.pyplot as plt
plt.plot([1,3,5,2])
plt.grid(True)    #Adding Grid on graph

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title("GRAPH") #Add title
plt.legend()
plt.show()  #TO see graph every time need to call plt.show() method
#####################

import matplotlib.pyplot as plt
x=range(1,5)

plt.plot(x,[xi*2 for xi in x],label='slow')
#here= line start from 2 and then (1,2),(2,4),(3,6),(4,8)
#therefore last is 8 came so line sart from 2 & grow uptill 8

plt.plot(x,[xi*4 for xi in x],label='high')
#here is also same line start from 4 and end at 16
plt.show()
plt.grid(True)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("GRAPH")
plt.legend()
plt.show()
#################################################

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,4)
plt.plot(x,x*2,label='TWO')
plt.plot(x,x*3, label='THREE')
plt.show()


############################33333
#Multiline plot

import matplotlib.pyplot as plt
import numpy as np
s=np.arange(1,6)
plt.plot(s)
plt.show()
x=range(1,5)

plt.plot(x,[xi*1.5 for xi in x])

plt.plot(x,[xi*3.0 for xi in x])

plt.plot(x,[xi/3.0 for xi in x])

plt.show()
###############################
#Add Grid ,axes, and labels

#Adding Grid =>  
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,5)

plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)

plt.grid(True)
plt.show()
#######################################

#Add labels
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,5 )
#
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)

plt.axis()
plt.axis([0,5,-1,13])
plt.show()
 #here  graph will start from 1
###################################

#R.R important
#Adding labels
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])

plt.xlabel('This is a x-axis')

plt.ylabel('This is y-axis ')

plt.show()

##################################
#Adding title
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])

plt.xlabel('x-axis')

plt.ylabel('y-axis ')

plt.title('Simple Plot')
plt.show()
############################################3
#
import matplotlib.pyplot as plt
import numpy as np
plt.plot([1,3,5,4,2,1])
plt.show()
plt.xlabel('This is x-axis')
plt.ylabel('This is y-axis')
plt.show()
##########################################
# Adding legend 
#
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,label='Normal')
#plt.plot(x,x*1.5,label='n')
plt.plot(x,x*3.0,label='slow')

plt.plot(x,x/3.0,label='fast')
plt.legend()
plt.show()

##############################################
#               Control Colors

'''Color Abrivation
b blue
c cyan
g green
k black
m magenta
r red
w white
y yellow'''

import matplotlib.pyplot as plt
import numpy as np

y=np.arange(1,3)
plt.plot(y,'y')
plt.plot(y+1,'m')
plt.plot(y+2,'c')
plt.show()  
#specifying styles in multiple plots
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y',y+1,'m',y+2,'c');
plt.show()

############################################################

'''style abrivation

- solid line
: dotted line
 dash line
###########
'''
#################################
#                   Control line styles

import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3)
plt.plot(y,'--',y+1,'-.',y+2,':')
plt.show()
###
import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3)
plt.plot(y,'y');
plt.plot(y+1,'m');
plt.plot(y+2,'c');
plt.show()
##########################
#specifying the styles in multiline plots
import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3)
plt.plot(y,'y',y+1,'m',y+2,'c');
plt.show()
########################
#               
import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3)
plt.plot(y,'--',y+1,'-.',y+2,':');
plt.show()
###################################################

#############    Markers        ###########33333
import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3,0.2)
plt.plot(y,'x',y+0.5,'o',y+1,'D',y+1.5,'^',y+2,'s')
plt.show()
########

import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3,0.5 )

plt.plot(y,'x',y+0.5,'o',y+1,'D',y+1.5,'^',y+2,'s');
plt.show()
####################################################
#
#               Plotting histogram

import matplotlib.pyplot as plt
import numpy as np

y=np.random.randn(1000)

#plt.hist=>
plt.hist(y);
plt.show()
###

import matplotlib.pyplot as plt
import numpy as np

a=np.random.randn(100)
b=np.random.randn(100)
plt.scatter(a,b)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
plt.bar([1,2,3],[4,5,6])
plt.show()

###############

import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(100)
plt.hist(x)
plt.show()

########################################################
#               
#                   Bar Plot
import matplotlib.pyplot as plt
plt.bar([1,2,3],[4,5,6])
plt.show()

import matplotlib.pyplot as plt
plt.bar([1,2,3],[4,5,6]);
plt.show()
#On X-axis 1,2,3 and y-axis 4,5,6 likewise

###############################################################

#               SCATTER Plot

#To show Realtion bet 2 entity we used scatter plot
#also known as BI-Varient analysis
#it usually represent by 2 variable

import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()
#
size=50*np.random.radn(1000) 
colors=np.random.radn(1000)
plt.scatter(x,y,s=size,c=colors);
plt.show()
#################################################
#Adding Text
X= np.linspace(-4,4,1024)
Y= .25 *(X+4.)*(X+1.)*(X-2.)
plt.text(-0.5,-0.25, 'brackmard minimum')
plt.plot(X,Y, c='b')
plt.show()

#################################################
#
import matplotlib.pyplot as plt
import numpy as np
a=np.random.randn(200)
#plt.hist(a)
plt.bar([1,2,3],[4,5,6])
plt.show()

################
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3])
y=np.array([4,5,6])
plt.scatter(x,y)

##############3

import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x, y)
plt.show()
    
################################
##############  Bar Graph  ########
#univeriable analaysis
'''
the bar() functin is used to generate bar charts in matplotlib
the function expects two list of values '''

import matplotlib.pyplot as plt
plt.bar([1,2,3],[3,2,5]);
plt.show()
###############################################
##########Scatter##################
import matplotlib.pyplot as plt
import numpy as np
x = np.random.random(1000)
y = np.random.random(1000)
plt.scatter(x,y)
plt.show()
##################################
######Addining color########
size = 50*np.random.randn(1000)
colors = np.random.rand(1000)
plt.scatter(x,y,s=size,c=colors);
plt.show()
#################################3
####Adding Text in graph############
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4,4,1024)
y = .25 *(x+4.) * (x+1.)*(x-2.)
plt.text(-0.5,-0.25,'Vaishnavi Dole')
plt.plot(x,y, c= 'k')
plt.show()

###########################################################33333
