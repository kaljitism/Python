#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
It is used for Directory Operations, like changing path and all..
Making Folders, Changing them, Moving them around.
"""


# In[8]:


import os


# In[9]:


curDir = os.getcwd()


# In[10]:


curDir


# In[11]:


os.mkdir('NewDir')


# In[6]:


os.rename('NewDir', 'NewDir2')


# In[7]:


os.rmdir('NewDir2')

