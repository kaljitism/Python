#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Swap
a = 9
b = 5


# In[2]:


a


# In[3]:


b


# In[4]:


temp = a
a = b
b = temp


# In[5]:


a


# In[6]:


b


# In[7]:


a = 1
b = 2
c = 3 
d = 4
e = 5


# In[8]:


a, b, c, d, e = 1, 2, 3, 4, 5


# In[9]:


a


# In[10]:


b


# In[11]:


c


# In[12]:


d


# In[13]:


e


# In[15]:


print(a)
print(b)


# In[16]:


a, b = b, a


# In[17]:


print(a)
print(b)


# In[19]:


task = int(input("Say 1, if your friend is coming else say 0: "))

if task == 1:
    print("Go there")

if task == 0:
    print("Dont go")


# In[1]:


# BMI

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height ** 2)

print("\nThe BMI of the user is: {}".format(bmi))

print()

if bmi < 24:
    print("You are underweight. Kinly eat more!")
    
if bmi > 24 and bmi < 26:
    print("You are fit, just maintain your health!")
    
else:
    print("You are overweight. Start dieting and exercising")


# In[13]:


a = int(input("Enter any number between 0 and 5: "))

print()

if a == 0:
    print(0)
    
elif a == 1:
    print(1)
    
elif a == 2:
    print(2)
    
elif a == 3:
    print(3)
    
elif a == 4:
    print(4)
    
elif a == 5:
    print(5)
    
else:
    print("Invalid Input")


# In[24]:


code = input("Enter any one letter from your code: ")

if '1' in code or '0' in code:
    print("\nCode is in the binary")
    
else:
    print("\nCode is in some other language")


# In[15]:


a = '10010101'


# In[21]:


'0' not in a


# In[22]:


'0' in a

