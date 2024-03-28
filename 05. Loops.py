#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(1)
print(2)
print(3)
print(4)
print(5)


# In[2]:


# Loops - Iteration - Repetition
# Value Based - For Loop
# Condition Based - While Loop


# In[3]:


for i in range(1, 6):
    print(i)


# In[4]:


for i in range(1, 11):
    print(i)


# In[5]:


for i in range(11):
    print(i)


# In[6]:


for i in range(6):
    print(i)


# In[14]:


for i in range(2, 21, 3):
    print(i)


# In[12]:


for i in range(10):
    print(i)


# In[15]:


text = "abcdef"


# In[16]:


for i in text:
    print(i)


# In[17]:


len(text)


# In[18]:


for i in range(len(text)):
    print(text[i])


# In[19]:


for i in range(len(text)):
    if text[i] == 'd':
        print(i)


# In[20]:


index = 0
for letter in text:
    if letter == 'd':
        print(index)
    index += 1


# In[21]:


for i in range(101):
    if i % 5 == 0:
        print("{} is divisible by 5".format(i))
    else:
        print("{} is not divisible by 5".format(i))


# In[22]:


i = 0
while i < 11:
    print(i)
    i += 1


# In[23]:


i = 0
while i < 101:
    if i % 5 == 0:
        print("{} is divisible by 5".format(i))
    else:
        print("{} is not divisible by 5".format(i))
    i += 1


# In[24]:


i = 1
while i < 61:
    if i % 6 == 0:
        print(i)
    i += 1


# In[25]:


i = 6
while i < 61:
    print(i)
    i += 6


# In[26]:


# Infinte Loop
i = 10
while i > 0:
    print(i)
    i += 1


# In[27]:


while True:
    print("It is true")


# In[29]:


a = int(input())
b = int(input())
c = int(input())


# ### Break, Continue and Pass

# In[12]:


x = int(input("How many candies you want?: "))
available = 10

i = 1
while i <= x:
    if i > available:
        print("Get Lost")
        break
    print("Candy")
    i +=1


# In[15]:


for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i)


# In[21]:


# Fizzbuzz
# <<Write the code>>


# In[22]:


for i in range(1, 101):
    if i % 2 != 0:
        pass
    else:
        print(i)


# ### Patterns

# In[23]:


print("####")
print("####")
print("####")
print("####")


# In[26]:


for i in range(4):
    print("#")


# In[28]:


for i in range(4):
    print("#", end="")


# In[32]:


for i in range(4):
    print("#", end="")
print()
    
for i in range(4):
    print("#", end="")
print()
    
for i in range(4):
    print("#", end="")
print()
    
for i in range(4):
    print("#", end="")


# In[43]:


for i in range(4):
    for j in range(4):
        print("#", end="")
    print()


# In[50]:


for i in range(4): print("#"*4)


# In[46]:


for i in range(5):
    for j in range(i):
        print("#", end="")
    print()


# In[47]:


for i in range(5):
    print("#"*i)


# ### For Else

# In[1]:


nums = [12, 15, 16, 21, 26]


# In[2]:


for num in nums:
    if num % 5 == 0:
        print(num)


# In[3]:


nums = [12, 15, 16, 21, 25]


# In[4]:


for num in nums:
    if num % 5 == 0:
        print(num)


# In[5]:


nums = [12, 15, 16, 21, 25]


# In[7]:


for num in nums:
    if num % 5 == 0:
        print(num)
        break


# In[8]:


nums = [10, 15, 16, 21, 25]


# In[9]:


for num in nums:
    if num % 5 == 0:
        print(num)
        break


# In[10]:


nums = [12, 14, 16, 21, 26]


# In[11]:


for num in nums:
    if num % 5 == 0:
        print(num)
        break


# In[12]:


nums = [12, 14, 16, 21, 26]


# In[13]:


for num in nums:
    if num % 5 == 0:
        print(num)
        break
    else:
        print("Not found")


# In[14]:


nums = [12, 14, 16, 21, 26]


# In[15]:


for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("Not found")


# In[16]:


nums = [12, 14, 16, 21, 26]


# In[ ]:




