#!/usr/bin/env python
# coding: utf-8

# In[1]:


nums = [1, 2, 3, 4, 5]


# In[2]:


nums[1]


# In[4]:


nums[3]


# In[9]:


for num in nums:
    print(num)


# In[10]:


nums = [1, 2, 3, 4, 5]
it = iter(nums)

print(it)


# In[11]:


nums = [1, 2, 3, 4, 5]
it = iter(nums)

print(it.__next__())


# In[17]:


nums = [1, 2, 3, 4, 5]
it = iter(nums)

print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())


# In[18]:


nums = [1, 2, 3, 4, 5]
it = iter(nums)

print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

print(it.__next__())


# In[31]:


class TopTen:
    
    def __init__(self):
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        val = self.num
        self.num += 1
        return val


# In[32]:


values = TopTen()


# In[33]:


print(values.__next__())


# In[34]:


print(values.__next__())


# In[30]:


print(values)


# In[35]:


for i in values:
    print(i)


# In[39]:


class TopTen:
    
    def __init__(self):
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num < 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


# In[40]:


values = TopTen()


# In[41]:


for i in values:
    print(i)


# In[ ]:




