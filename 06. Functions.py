#!/usr/bin/env python
# coding: utf-8

# In[3]:


def func():
    print("I am a function")


# In[4]:


func()


# In[5]:


def add():
    num1 = int(input("Enter one number: "))
    num2 = int(input("Enter another number: "))
    print(num1 + num2)


# In[6]:


add()


# In[18]:


def add(num1, num2):
    print(num1 + num2)


# In[19]:


add(2, 3)


# In[20]:


s = add(2, 3)


# In[21]:


print(s)


# In[10]:


print("Hello")


# In[11]:


def add(num1, num2):
    addition = num1 + num2
    return addition


# In[12]:


add(3, 4)


# In[13]:


s = add(2, 4)


# In[14]:


s


# In[15]:


a = print("Aditya")


# In[17]:


print(a)


# In[22]:


def add(num1, num2):
    addition =  num1 + num2
    return addition


# In[23]:


add()


# In[24]:


print()


# In[32]:


def add(num1=None, num2=None):
    addition = None
    if num1 is not None and num2 is not None:
        addition = num1 + num2
    return addition


# In[33]:


add()


# In[34]:


add(2, "a")


# In[70]:


def add(num1=None, num2=None):
    addition = None
    
    con1 = isinstance(num1, str) == False
    con2 = isinstance(num2, str) == False
    
    if num1 and num2:
        
        if con1 and con2:
            addition = num1 + num2
        else:
            print("Please enter the numbers")
            
    else:
        print("Please enter the numbers")
    
    return addition


# In[71]:


add()


# In[72]:


add(2, 3)


# In[73]:


add('a', 3)


# In[74]:


add(2.0, 7.8)


# In[75]:


add(1.0, 8)


# In[92]:


var3 = 8

def func1():
    global var1
    var1 = 3
    var2 = 4
    print(var1)
    if var1 == 3:
        print(var1)
    
def func2():
    print(var1)


# In[93]:


func1()


# In[94]:


func2()


# ### Anonymous Function or Lambda

# In[1]:


def square(a):
    return a*a


# In[2]:


square(3)


# In[3]:


y = square(12)


# In[4]:


y


# In[15]:


sqr = lambda a : a*a


# In[16]:


sqr(2)


# In[17]:


sqr(20)


# In[18]:


add = lambda a, b: a + b


# In[19]:


add(32, 34)


# ### Filter

# In[28]:


nums = [3, 2, 6, 7, 8, 4, 6, 2, 9]


# In[29]:


def is_even(n):
    return n % 2 == 0


# In[30]:


evens = list(filter(is_even, nums))


# In[31]:


evens


# In[32]:


nums = [3, 2, 6, 7, 8, 4, 6, 2, 9]


# In[34]:


evens = list(filter(lambda x: x % 2 == 0, nums))


# In[35]:


evens


# In[36]:


odds = list(filter(lambda x: x % 2 != 0, nums))


# In[37]:


odds


# ### Map

# In[38]:


nums = [3, 2, 6, 7, 8, 4, 6, 2, 9]


# In[39]:


evens = list(filter(lambda x: x % 2 == 0, nums))


# In[40]:


evens


# In[41]:


def update(n):
    return n * 2


# In[44]:


doubles = list(map(update, evens))


# In[45]:


doubles


# In[46]:


doubles1 = list(map(lambda x: x*2, evens))


# In[47]:


doubles1


# In[48]:


triples = list(map(lambda x: x*3, evens))


# In[49]:


triples


# ### Reduce

# In[51]:


from functools import reduce


# In[52]:


def add_all(a, b):
    return a + b


# In[53]:


add = reduce(add_all, doubles)


# In[54]:


add


# ### Decorators
# 
# Changing the function without even touching it

# In[65]:


def div(a, b):
    print(a/ b)


# In[66]:


div(2, 4)


# In[67]:


def div(a, b):
    if a < b:
        a, b = b, a
    print(a/ b)


# In[68]:


div(2, 4)


# In[69]:


def div(a, b):
    print(a/ b)
    

# Decorator
def smart_div(func):
    
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    
    return inner


# In[70]:


div = smart_div(div)


# In[71]:


div(2, 4)


# ### args and kwargs

# In[72]:


def person(name, *data):
    print(name)
    print(data)


# In[73]:


p1 = person("Aditya", 16, "Bangalore", 9268268)


# In[74]:


def person(name, *data):
    print(name)
    for i in data:
        print(i)


# In[75]:


p2 = person('Aditya', 'Bangalore', 'Bannergatha', 'ASUS')


# In[78]:


def person(name, **data):
    print(name)
    print(data)


# In[79]:


p3 = person(name='Aditya', city='Bangalore', interest='Deep Learning')

