#!/usr/bin/env python
# coding: utf-8

# ### Lists
# 
# Mutable data types

# In[3]:


my_first_list = [1, 2, 3, 4, 5]


# In[4]:


my_first_list


# In[5]:


lst = ['Aditya', 2, 3, 5, 'Python']


# In[6]:


lst


# In[56]:


type(lst)


# In[7]:


for i in lst:
    print(i)


# In[10]:


for item in my_first_list:
    print("This is: {}".format(item))


# In[11]:


len(my_first_list)


# In[12]:


len(lst)


# In[13]:


new_lst = lst + my_first_list


# In[14]:


new_lst


# In[15]:


newer_lst = my_first_list + lst


# In[16]:


newer_lst


# In[17]:


for i in newer_lst:
    print(i)


# In[18]:


len(newer_lst)


# In[19]:


marks = [24, 34, 45, 41, 44]
bonus = [1, 2, 5, 4, 5]


# In[20]:


total_marks = marks + bonus


# In[21]:


total_marks


# In[22]:


lst


# In[23]:


lst.append('Java')


# In[24]:


lst


# In[25]:


total_marks = []
for i in range(len(marks)):
    new_element = marks[i] + bonus[i]
    total_marks.append(new_element)


# In[26]:


total_marks


# In[27]:


lst1 = ["Python", 'Java', 'C', 'C++']


# In[29]:


lst1.append('JavaScript')


# In[31]:


lst1


# In[34]:


lst1.pop()


# In[35]:


lst1


# In[36]:


lst1.insert(2, 'JavaScript')


# In[48]:


lst1.insert(0, 'Assembly')


# In[49]:


lst1


# In[38]:


lst1[3] = 'C#'


# In[39]:


lst1


# In[40]:


lst1.remove('C#')


# In[41]:


lst1


# In[42]:


lst1.pop(1)


# In[43]:


lst1


# ### Tuples
# 
# Immutable data types

# In[50]:


my_first_tuple = (1, 2, 3, 4, 5)


# In[51]:


my_first_tuple


# In[69]:


my_first_tuple[2]


# In[52]:


for i in my_first_tuple:
    print(i)


# In[54]:


len(my_first_tuple)


# In[55]:


type(my_first_tuple)


# In[57]:


tup = (1, 2, 3, 5)


# In[62]:


lst_tup = list(tup)


# In[63]:


lst_tup


# In[64]:


lst_tup.insert(3, 4)


# In[65]:


lst_tup


# In[66]:


tup = tuple(lst_tup)


# In[68]:


tup


# ### Dictionaries

# In[70]:


# Key - Value Pair


# In[71]:


my_first_dict = {'Apurva': 90, 'Ashwin': 91, 'Deepa': 89, 'Shashidhar': 88, 'Siddhartha': 93}


# In[72]:


my_first_dict


# In[73]:


my_first_dict['Apurva']


# In[74]:


my_first_dict['Shashidhar']


# In[75]:


len(my_first_dict)


# In[84]:


for key, values in my_first_dict.items():
    print(key, values)


# In[80]:


for key in my_first_dict:
    print(key)


# In[81]:


for key in my_first_dict:
    print(my_first_dict[key])


# In[85]:


my_first_dict['Aditya'] = 87


# In[86]:


my_first_dict


# In[87]:


my_first_dict['Aditya']


# In[89]:


my_first_dict.pop('Aditya')


# In[90]:


my_first_dict


# ### List Comprehensions

# In[1]:


a = [1, 3, 5, 7, 9, 11]


# In[6]:


# b =  [ 2, 6, 10, 14, 18, 22]


# In[4]:


b = []
for i in range(len(a)):
    b.append(a[i] * 2)


# In[7]:


c = []
for item in a:
    c.append(item * 2)


# In[8]:


b


# In[9]:


c 


# In[11]:


d = [item * 2 for item in a]


# In[12]:


d


# In[13]:


# [1, 4, 9, 16, 25, 36]


# In[14]:


e1 = []
for x in range(1, 7):
    e1.append(x ** 2)


# In[15]:


e1


# In[16]:


d1 = [x ** 2 for x in range(1, 7)]


# In[17]:


d1


# In[18]:


# [36, 25, 16, 9, 4, 1]


# In[19]:


l1 = [x ** 2 for x in range(6, 0, -1)]


# In[20]:


l1


# ### Generators

# In[46]:


def TopTen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


# In[47]:


values = TopTen()


# In[41]:


values


# In[42]:


print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())


# In[48]:


for i in values:
    print(i)


# In[50]:


def TopTen():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


# In[51]:


values = TopTen()


# In[52]:


for i in values:
    print(i)


# In[ ]:




