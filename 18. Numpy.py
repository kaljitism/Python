#!/usr/bin/env python
# coding: utf-8

# # Numpy Basics

# Welcome to section of Numpy and Pandas. This is the most used Python libraries for data science. NumPy consists of a powerful data structure called multidimensional arrays. Pandas is another powerful Python library that provides fast and easy data analysis platform.
# 
# NumPy is a library written for scientific computing and data analysis. It stands for numerical python and also known as array oriented computing.
# 
# The most basic object in NumPy is the ndarray, or simply an array which is an n-dimensional, homogeneous array. By homogenous, we mean that all the elements in a NumPy array have to be of the same data type, which is commonly numeric (float or integer).
# 
# 
#  # Why Numpy?
#  convenience & speed
#  
#  Numpy is much faster than the standard python ways to do computations.
#  
# Vectorised code typically does not contain explicit looping and indexing etc. (all of this happens behind the scenes, in precompiled C-code), and thus it is much more concise.
# 
# Also, many Numpy operations are implemented in C which is basically being executed behind the scenes, avoiding the general cost of loops in Python, pointer indirection and per-element dynamic type checking. The speed boost depends on which operations you're performing.
#  
#  NumPy arrays are more compact than lists, i.e. they take much lesser storage space than lists

# In[1]:


get_ipython().system('pip install numpy')


# In[2]:


import numpy


# In[1]:


import numpy as np


# In[4]:


arr = np.array([1, 2, 3])


# In[5]:


print(arr)


# In[6]:


b = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])


# In[7]:


b


# In[8]:


b.shape


# In[9]:


arr.shape


# In[10]:


b.dtype


# In[11]:


arr.dtype


# In[12]:


a = [1, 2, 3]


# In[13]:


type(a)


# In[14]:


print(type(arr))


# In[15]:


print(type(b))


# In[16]:


lst_1 = [i for i in range(10)]
print(lst_1)


# In[17]:


lst_2 = [i+2 for i in lst_1]
lst_2


# In[18]:


sqr = [item**2 for item in range(11)]
sqr


# In[19]:


np.arange(11)


# # Performance measurement
# I mentioned that the key advantages of numpy are convenience and speed of computation.
# 
# You'll often work with extremely large datasets, and thus it is important point for you to understand how much computation time (and memory) you can save using numpy, compared to standard python lists.

# In[20]:


c = range(10000)
get_ipython().run_line_magic('timeit', '[i**3 for i in c]')


# In[21]:


c_numpy = np.arange(10000)
get_ipython().run_line_magic('timeit', 'c_numpy**3')


# Still not convinced? want to see one more intresting example

# In[22]:


l1 = range(10000)
l2 = [i**2 for i in range(10000)]


# In[23]:


#multiplying two lists elementwise
get_ipython().run_line_magic('timeit', 'list(map(lambda x, y: x*y, l1, l2))')


# In[24]:


a1 = np.array(l1)
b1 = np.array(l2)


# In[25]:


get_ipython().run_line_magic('timeit', 'a1*b1')


# In[ ]:





# so I can do everything without even writing a loop? yes... ohh wao

# # Creating Numpy array
# 
# There are multiple ways to create numpy array. Lets walk over them

# In[26]:


np.arange(1, 11)


# In[27]:


np.arange(10)


# In[28]:


np.arange(0, 10)


# In[29]:


np.arange(234, 456, 7)


# In[30]:


np.arange(20)


# In[31]:


np.arange(500, 100, -100)


# In[32]:


np.arange(0, 22, 2)


# In[33]:


np.arange(2,12,2)


# In[34]:


np.zeros((3,3), dtype=np.int32)


# In[35]:


np.zeros(1, dtype=np.int32)


# In[36]:


np.zeros((1, 1), dtype=np.int32)


# In[37]:


np.zeros((3, 3))


# In[38]:


np.zeros((5,5))


# In[39]:


a = np.array([[2, 3], [2, 4], [8, 9]])


# In[40]:


a


# In[41]:


a.shape


# In[42]:


np.zeros_like(a)


# In[43]:


np.ones((5,2), dtype=np.int32)


# In[44]:


np.eye(1, dtype=np.int32)
[1]


# In[45]:


np.eye(2)
[1, 1]


# In[46]:


np.eye(3)
[1, 1, 1]


# In[47]:


np.eye(10)
[1, 1, 1, 1, 1, 1,1....]


# In[ ]:


np.full((5, 3), 3.3, dtype=np.int32)


# In[ ]:


np.full((3,3),2.2, dtype= np.int32)


# In[ ]:


np.diag([2, 5, 68, 78])


# In[70]:


x = np.diag(np.arange(1, 101))


# In[71]:


x


# In[72]:


[1, 2, 3]
[1, 2, 3]
[1, 2, 3]


# In[73]:


v = np.array([1,2,3])
print(v)
np.tile(v,(5, 2)) # stack 3 copies of v on top of each other


# In[76]:


x1 = np.array([[1, 2, 3, 4], [5, 6, 7,8 ]])
np.tile(x1, (1, 3))


# In[ ]:


np.random.seed(53833)
print(np.random.random())
print(np.random.random())
print(np.random.random())
print(np.random.random())
print(np.random.random())
print(np.random.random())


# In[ ]:


np.random.seed(53833)
print(np.random.random())
print(np.random.random())
print(np.random.random())


# In[ ]:


x = np.random.random((4, 4))


# In[ ]:


rounded = np.round(x, 2)


# In[ ]:


rounded


# In[ ]:


new = rounded * 100


# In[ ]:


new


# In[ ]:


intt = new.astype(np.int32)
intt


# In[ ]:


intt.astype(np.float32)


# In[ ]:


a = np.arange(10)
a.dtype


# In[ ]:


#memory used by each array element in bytes
a.itemsize


# In[ ]:


x = np.arange(24)


# In[ ]:


x.reshape(-1, 8)


# In[2]:


z = np.array([[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]])
print(z)
print(z.shape)


# In[3]:


#  -1 is an unknown dimension to be figured out by numpy
z.reshape(-1)


# In[4]:


# Now trying to reshape with (-1) . Result new shape is (12,) and is compatible with original shape (3,4)
# So we get result new shape as (12, 1).again compatible with original shape(3,4)
z.reshape(1,-1)


# In[5]:


# Now trying to reshape with (-1, 1) . We have provided column as 1 but rows as unknown . 
z.reshape(-1,1)


# In[6]:


# New shape as (-1, 2). row unknown, column 2. 
z.reshape(-1, 2)


# In[ ]:


# Now trying to keep column as unknown. 
# New shape as (1,-1). i.e, row is 1, column unknown. 
z.reshape(1,-1)


# In[ ]:


# New shape (2, -1). Row 2, column unknown. 
z.reshape(2, -1)


# In[ ]:


# New shape as (3, -1). Row 3, column unknown. 
z.reshape(3, -1)


# In[7]:


np.zeros((4, 3, 2))


# In[8]:


# -1 will automatically adjust dimention
np.arange(18).reshape(2,3,-1)


# # accessing Numpy array element

# In[ ]:


a = np.array([2,4,6,8,10,12,14,16])


# In[ ]:


a


# In[ ]:


a[2]


# In[ ]:


a[[2,4,6]]


# In[ ]:


a[2:]


# In[ ]:


a[2:5]


# In[ ]:


a[0::2]


# Lets check the same for 2 D array

# In[9]:


a = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[10]:


a


# In[ ]:


a[2,2]


# In[11]:


a > 2


# In[12]:


a[a > 2]


# In[13]:


a[(a > 2) & (a < 5)]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # subset of numpy array

# In[14]:


a = np.arange(10)


# In[15]:


a


# In[16]:


b = a


# In[17]:


b


# In[18]:


b[0] = 11


# In[19]:


b


# In[20]:


# Notice a is also changed
a


# In[55]:


np.shares_memory(a,b)


# In[28]:


a = np.arange(10)


# In[29]:


b = a.copy()


# In[30]:


b[0] = 11


# In[31]:


a


# In[32]:


np.shares_memory(a,b)


# # More operations

# In[33]:


a = np.array([[1,2,3],[4,5,6]])


# In[34]:


a


# In[35]:


a.T


# In[36]:


b = np.array([[7,8,9],[10,11,12]])


# In[37]:


a


# In[38]:


b


# In[77]:


np.vstack((a,b))


# In[78]:


np.hstack((a,b))


# # MAthmatical operation

# In[ ]:





# In[ ]:





# In[39]:


a = np.arange(1,10)


# In[40]:


a


# In[41]:


np.sin(a)


# In[42]:


np.cos(a)


# In[43]:


np.exp(a)


# In[44]:


np.sum(a)


# In[45]:


np.median(a)


# In[46]:


a.std()


# In[50]:


a = np.arange(1,10).reshape(3,3)


# In[51]:


a


# In[52]:


np.linalg.det(a)


# In[53]:


np.linalg.inv(a)


# In[54]:


np.linalg.eig(a)


# In[55]:


a


# In[56]:


b = a.T


# In[57]:


b


# In[98]:


np.dot(a,b)


# In[99]:


a = np.array([1,1,0], dtype = bool)
b = np.array([1,0,1], dtype = bool)
print(a)
print(b)


# In[100]:


np.logical_or(a,b)


# In[101]:


np.logical_and(a,b)


# In[58]:


np.all(a == a)


# In[59]:


a = np.arange(1,10).reshape(3,3)


# In[60]:


a


# In[61]:


np.all(a > 2)


# In[62]:


np.any(a == 8)


# In[67]:


a = np.array([[1, 2], [3, 4]])
a


# In[64]:


a.sum()


# In[65]:


a.sum(axis=0)


# In[66]:


a.sum(axis=1)


# In[68]:


a.max()


# In[69]:


a.argmax()


# In[12]:


a


# In[70]:


a.shape


# In[71]:


a = a[:, np.newaxis] 
a


# In[72]:


a.shape


# In[73]:


a = np.array([[3, 5, 1, 2, 9, 7],[7, 3, 5, 9, 12, 2]])


# In[74]:


np.sort(a)


# In[75]:


np.argsort(a)


# In[76]:


a = np.array([14, 5, 4, 2])


# In[77]:


np.argsort(a)


# In[156]:


a

