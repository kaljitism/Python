#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data = pd.Series([0, 1, 2, 3, 4, 5, np.nan, 6, 7, 8])


# In[3]:


data


# In[4]:


data.isnull()


# In[5]:


data.notnull()


# In[6]:


data.dropna()


# In[7]:


not_null_data = data.dropna()


# In[8]:


data_dim = pd.DataFrame([[1,2,3,np.nan],[4,5,np.nan,np.nan],[7,np.nan,np.nan,np.nan],[np.nan,np.nan,np.nan,np.nan]])
data_dim


# In[9]:


data_dim.dropna()


# In[10]:


data_dim.dropna(how='all')


# In[11]:


data_dim.dropna(axis=1, how='all')


# In[13]:


data_dim.dropna(thresh=4)


# In[14]:


data_dim.dropna(thresh=2)


# In[15]:


data_dim


# In[16]:


data_dim_fill = data_dim.fillna(0)


# In[17]:


data_dim_fill


# In[18]:


data_dim_fill = data_dim.fillna({0: 0, 1: 8, 2: 9, 3: 10})
data_dim_fill


# In[19]:


data_dim_fill = data_dim.fillna(method='ffill', limit = 2)
data_dim_fill


# In[20]:


data_dim_fill = data_dim.fillna(method='ffill', limit = 3)
data_dim_fill


# In[21]:


data_dim_fill = data_dim.fillna(axis = 1, method='ffill', limit=2)
data_dim_fill


# In[22]:


data_dim


# In[23]:


data_dim_fill = data_dim.fillna(data_dim.mean())
data_dim_fill


# In[24]:


data = pd.Series([1,2,-99,4,5,-99,7,8,-99])
data


# In[25]:


data.replace(-99, np.nan)


# In[26]:


data.replace([-99, 7.0, 8.0], np.nan)


# In[27]:


data.replace({-99: np.nan, 1.0: 0.0})


# In[28]:


data_number = pd.DataFrame({'english': ['zero','one','two','three','four','five'],
'digits': [0,1,2,3,4,5]})
data_number


# In[29]:


english_to_multiple = {
    'two': 'yes',
    'four': 'yes'
}


# In[30]:


english_to_multiple


# In[31]:


data_number['multiple'] = data_number['english'].map(english_to_multiple)


# In[32]:


data_number


# In[34]:


data = pd.Series(list('abcdababcdabcd'))
data


# In[35]:


pd.get_dummies(data)


# In[ ]:


"""
a = 0
b = 1
c = 2
d = 3
"""
"""
Methods to change categorical variables to continuous variables(numerical values)
1. Get dummies() 
    problems - data size will increase, hard to get these values in one column, multi-colinearity, linear dependence
2. Replace
    df.replace({'a':0, 'b':1, 'c':2, 'd':3})
    problem - lengthy process of typing while a lot of categories
3. Label Encoder
    It is always the best choice to convert categorical values to continuous. 
"""
# Hotdog : 0
# Pizza: 1
# Burgur : 2
# Chicken : 3


# In[37]:


# sklearn - scikit learn - Machine learning and Pre Processing Library
from sklearn.preprocessing import LabelEncoder


# In[38]:


# Label Encoder Object or Estimator
le = LabelEncoder()


# In[39]:


data = le.fit_transform(data)


# In[40]:


data


# In[ ]:


# Normalization and Standardization


# In[ ]:


#Miles driven- 100, 1000, 10000, 10000000 .. Range is 100 to 10000000
#Price- 50k - 100k


# In[ ]:


# Normalizing - Convert or Scale all these values in a range of 0 - 1.. Range will be 0 to 1
# Normalize Miles driven
# Normalize Price


# In[ ]:


# Miles driven - 0 to 1
# prices- 0 to 1

