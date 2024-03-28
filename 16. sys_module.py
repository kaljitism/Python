#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
Sys Module is used by Python Programmers to access system information.
You can access functions and variables used by interpreter in runtime.
"""
print()


# In[21]:


import sys


# In[22]:


sys.stderr.write('Warning: This is Python, not linux')


# In[23]:


sys.stderr.flush()


# In[25]:


sys.stdout.write('This is just a normal text')


# In[19]:


sys.stderr.write('test')
sys.stderr.flush()
sys.stdout.write('true')


# In[26]:


print(sys.argv)


# In[ ]:




