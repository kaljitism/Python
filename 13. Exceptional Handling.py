#!/usr/bin/env python
# coding: utf-8

# There are 3 types of errors:
#     1. Compile Time Error - Syntactical Error
#     2. Logical Error - Wrong Output
#     3. Run Time Error - Interrupt due to certain condition or control flow while execution

# In[1]:


def div(a, b):
    return a/ b


# In[2]:


div(10, 5)


# In[3]:


div(23, 46)


# In[4]:


div(6, 0)


# In[9]:


def div(a, b):
    try: 
        return a/ b
    
    except Exception as e:
        print(e, "not allowed")


# In[10]:


div(5, 10)


# In[11]:


div(5, 0)


# In[12]:


def div(a, b):
    try: 
        return a/ b
    
    except ZeroDivisionError as e:
        print(e, "not allowed")


# In[13]:


div(10, 2)


# In[14]:


div(10, 0)


# In[18]:


def div(a, b):
    try: 
        return a/ b
    
    except ZeroDivisionError as e:
        print(e, "not allowed")
        
    finally:
        print("Task Completed")


# In[19]:


div(10, 5)


# In[20]:


div(10, 0)


# In[22]:


div('a', 10)


# In[32]:


def div(a, b):
    try: 
        return a/ b
    
    except ZeroDivisionError as z:
        print(z, "not allowed")
        
    except TypeError as t:
        print(t, "not allowed")
        
    except Exception as e:
        print("Not Found")
        
    finally:
        print("Task Completed")


# In[33]:


div('a', 10)


# In[34]:


div(23, 0)


# In[ ]:




