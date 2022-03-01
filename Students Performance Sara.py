#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


df = pd.read_csv('StudentsPerformance.csv')
df.head()


# In[4]:


df.info()


# In[9]:


df.isnull()


# In[10]:


df.isnull().sum()


# In[7]:


df['test preparation course'].isnull().sum()


# In[8]:


df['reading score'].isnull().sum()


# In[ ]:




