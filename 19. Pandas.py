#!/usr/bin/env python
# coding: utf-8

# # Create Pandas Series

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd


# In[3]:


a = pd.Series([1,2,3,4,5])


# In[4]:


a


# In[5]:


type(a)


# In[6]:


a[2]


# In[7]:


a = pd.Series(['a','b','c'])


# In[8]:


a


# In[9]:


a = pd.date_range(start = '01-01-2019', end = '24-10-2019')


# In[10]:


a


# In[11]:


type(a)


# # Pandas dataframe

# In[12]:


name = ['Shakti', 'Hemanka', 'Rajeshwari', 'Akshaya', 'Fenil']


# In[13]:


domain = ['NLP', 'Reinforcement Learning', 'Computer Vision', 'Analytrics', 'Automation']


# In[14]:


experience = [2, 3, 4, 5, 6]


# In[15]:


dct = {'Name': name, 'Domain': domain, 'Experience': experience}


# In[16]:


data = pd.DataFrame(dct)


# In[17]:


data


# In[ ]:





# In[18]:


zipped = list(zip(name, domain, experience))


# In[19]:


zipped


# In[20]:


data = {'Name':name,
       'Domain':domain,
       'Experience':experience}


# In[21]:


df = pd.DataFrame(data)


# In[22]:


df


# In[ ]:





# In[23]:


import numpy as np


# In[24]:


np.random.randint(low=10, high=100, size=10)


# In[25]:


np.random.choice([1, 2, 3, 4, 5, 6], 5)


# In[ ]:





# In[112]:


temp = np.random.randint(low = 20, high =100, size = [20,])
name = np.random.choice(['Shakti', 'Hemanka', 'Rajeshwari', 'Akshaya', 'Fenil'], 20)
random = np.random.choice([10,11,13,12,14], 20)


# In[113]:


temp


# In[114]:


name


# In[115]:


random


# In[116]:


a = list(zip(temp, name, random))


# In[117]:


a


# In[118]:


df = pd.DataFrame(data = a, columns=['temp','name','random'])


# In[119]:


df


# In[124]:


df.head()


# In[128]:


df.tail()


# In[36]:


type(df)


# In[37]:


df.info()


# In[38]:


df.shape


# In[39]:


df.describe()


# In[129]:


df['name'].head()


# In[41]:


temp = np.random.randint(low = 20, high =100, size = [20,])
name = np.random.choice(['Divya', 'SSS', 'Ajay', 'Vinay', 'Satish'],20)
random = np.random.choice([10,11,13,12,14],20)


# In[42]:


df = pd.DataFrame({'temp':temp, 'name':name, 'random':random})


# In[43]:


type(df)


# In[44]:


df.head(5)


# In[45]:


df.tail()


# In[46]:


df.shape


# In[47]:


df.columns


# In[48]:


df.name


# In[49]:


df['name']


# In[50]:


df.info()
# row = Instances / data points/ data instances
# columns = Attributes or features


# In[51]:


df.describe()


# In[52]:


df['temp'].describe()


# In[53]:


df.info()


# In[54]:


df.values


# In[55]:


df


# In[132]:


df.set_index('temp', inplace=True)


# In[133]:


df


# In[134]:


df.sort_index(axis=0, ascending=True)


# In[59]:


df.sort_values(by='random', ascending = True)


# In[60]:


df.drop(['random'], axis=1)


# In[61]:


df


# In[62]:


df.iloc[1:11, :]


# In[63]:


df.iloc[10:16, :]


# In[64]:


df.iloc[:, 1]


# In[65]:


df.iloc[5:11, 0]


# In[66]:


df.iloc[10:18, 1]


# In[67]:


df.iloc[5:10, 0:2]


# In[68]:


df.iloc[[9, 10], 1:2]


# In[69]:


# iloc = index location
# loc = location - index or name


# In[ ]:





# In[70]:


df = pd.DataFrame({'temp':temp, 'name':name, 'random':random})


# In[ ]:





# In[71]:


df.head()


# In[72]:


df.loc[4,:]


# In[73]:


df.loc[[1, 2, 5, 7, 12]]


# In[74]:


df.loc[[7, 2, 15, 19, 4], ['name','random']]


# In[75]:


df.loc[df.random > 12]


# In[76]:


df.loc[(df.random > 13) | (df.random == 10),:]


# In[136]:


# Merging & concat
d1 = pd.DataFrame([['a', 1], ['b', 2]],columns=['col1', 'number'])
d2 = pd.DataFrame([['c', 3, 'lion'], ['d', 4, 'tiger']],columns=['letter', 'number', 'animal'])


# In[137]:


d1


# In[138]:


d2


# In[140]:


pd.concat([d1,d2], axis =0)


# In[81]:


pd.concat([d1,d2], axis =0, ignore_index=True)


# In[82]:


pd.concat([d1,d2], axis = 1)


# In[141]:


d1 = pd.DataFrame({
    "city" : ["lucknow","kanpur","agra","delhi"],
    "temperature" : [32,45,30,40]
})


# In[142]:


d1


# In[143]:


d2 = pd.DataFrame({
    "city" : ["delhi","lucknow","kanpur"],
    "humidity" : [68,65,75]
})


# In[144]:


d2


# In[145]:


df = pd.merge(d1,d2, on='city')


# In[146]:


df


# In[89]:


pd.merge(d1,d2, on=['city'], how ='outer')


# In[90]:


# pd.merge(d1, d2, on =['city'], how='left')


# In[91]:


# dataset from https://github.com/codebasics/py/blob/master/pandas/6_handling_missing_data_replace/weather_data.csv

# CSV - Comma separated Values


# In[92]:


df1 = pd.read_csv("weather_data.csv")


# In[93]:


df1 


# In[94]:


df1.info()


# In[95]:


df1.describe()


# In[96]:


df1.shape


# In[97]:


"""
csv
xl
matlab
hd5y
json
"""


# In[98]:


get_ipython().system('pip3 install openpyxl')
df1.to_excel('df_xl.xlsx', sheet_name = 'weather_data', index=False)


# In[99]:


get_ipython().system('pip3 install xlrd')
df2 = pd.read_excel('df_xl.xlsx')


# In[100]:


df2


# In[101]:


df2.to_csv('file.csv')


# In[102]:


df2.to_csv('file_noindex.csv', index = False)


# In[147]:


df_group = df2.groupby("event")


# In[148]:


df_group


# In[105]:


for entries in df_group:
    print(entries)


# In[106]:


df_group.get_group('Rain')


# In[107]:


df_group.describe()


# In[108]:


def hot_temp(x):
    return x > 30


# In[109]:


df2['hot_temp'] = df2['temperature'].apply(hot_temp)


# In[110]:


df2


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




