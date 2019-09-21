#!/usr/bin/env python
# coding: utf-8

#This data visualisation was created using data from Beaches.ie.
#It was inspired by the YouTube tutorial 'Intro to Data Analysis / Visualization with Python, Matplotlib and Pandas | Matplotlib Tutorial' by YouTuber CS Dojo.
#I was able to create a data model representing reports of e coli and intestinal enterococci present in the 2019 water testing (over a 5 month period)
#The result is a graph that shows a contrast between e coli reports and intestinal entercocci reports.

# In[36]:


import pandas as pd #importing pandas module and giving it the name 'pd'.


# In[37]:


from matplotlib import pyplot as plt #importing the matplotlib library under the name 'plt'.


# In[38]:

ecoli = [-10, 41, 10, -10, 20] #a list of e coli data.
intestinalenterococci = [1, 6, 4, 2, 15] #a list of interestinal enterococci data.
plt.plot(ecoli) #plots the e coli data 
plt.plot(intestinalenterococci) ##plots the intestinal enterococci data 
plt.title ('Rocky Bay Beach Water Quality 2019') #titles the graph 'Rocky Bay Beach Water Quality 2019'
plt.xlabel('intestinal enterococci') #x axis is titled 'intestinal enterococci'
plt.ylabel('e coli') #y axis represents e coli count
plt.legend(['E coli reports', 'Intestinal Enterococci reports']) #creates a legend/key that show what the yellow and blue lines mean
plt.show() #produces graph


# In[ ]:




