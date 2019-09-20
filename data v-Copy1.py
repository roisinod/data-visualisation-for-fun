#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd


# In[37]:


from matplotlib import pyplot as plt


# In[38]:


ecoli = [-10, 41, 10, -10, 20]
intestinalenterococci = [1, 6, 4, 2, 15]
plt.plot(ecoli)
plt.plot(intestinalenterococci)
plt.title ('Rocky Bay Beach Water Quality 2019')
plt.xlabel('intestinal enterococci')
plt.ylabel('e coli')
plt.legend(['E coli reports', 'Intestinal Enterococci reports'])
plt.show()


# In[ ]:




