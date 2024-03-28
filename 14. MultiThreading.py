#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Hello:
    def run(self):
        for i in range(5): print("Hello")
            
class Hi:
    def run(self):
        for i in range(5): print("Hi")


# In[9]:


h1 = Hello()
h2 = Hi()


# In[10]:


h1.run()
h2.run()


# In[11]:


from threading import *


# In[12]:


class Hello(Thread):
    def run(self):
        for i in range(5): print("Hello")
            
class Hi(Thread):
    def run(self):
        for i in range(5): print("Hi")


# In[13]:


h1 = Hello()
h2 = Hi()


# In[14]:


h1.run()
h2.run()


# In[20]:


class Hello(Thread):
    def run(self):
        for i in range(5): print("Hello")
            
class Hi(Thread):
    def run(self):
        for i in range(5): print("Hi")


# In[21]:


t1 = Hello()
t2 = Hi()


# In[22]:


t1.start()
t2.start()


# In[23]:


class Hello(Thread):
    def run(self):
        for i in range(500): print("Hello")
            
class Hi(Thread):
    def run(self):
        for i in range(500): print("Hi")


# In[24]:


t1 = Hello()
t2 = Hi()


# In[25]:


t1.start()
t2.start()


# In[26]:


from time import sleep


# In[33]:


class Hello(Thread):
    def run(self):
        for i in range(500): 
            print("Hello")
            sleep(1)
            
class Hi(Thread):
    def run(self):
        for i in range(500): 
            print("Hi")
            sleep(1)


# In[31]:


t1 = Hello()
t2 = Hi()


# In[32]:


t1.start()
sleep(0.2)
t2.start()


# In[ ]:




