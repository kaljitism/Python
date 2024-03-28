#!/usr/bin/env python
# coding: utf-8

# In[11]:


with open("data.txt", 'r') as file:
    print(file.read())


# In[12]:


with open("data.txt", 'r') as file:
    print(file.readline())


# In[13]:


with open("data.txt", 'r') as file:
    print(file.readline(), end='')
    print(file.readline())


# In[14]:


with open("newData.txt", 'w') as file:
    file.write("This is the new file, I just created\n Dont you think I am awesome?\n I can create files using Python\n Can you?")


# In[15]:


with open("newData.txt", 'r') as file:
    print(file.read())


# In[16]:


with open("newData.txt", 'a') as file:
    file.write("I can append as well!")


# In[ ]:




