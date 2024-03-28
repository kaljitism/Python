#!/usr/bin/env python
# coding: utf-8

# ### Inner Class

# In[1]:


class Student:
    
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


# In[2]:


s1 = Student('Aditya', 1)


# In[3]:


s1.show()


# In[4]:


class Student:
    
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        
    def show(self):
        print(self.name, self.roll)


# In[5]:


s1 = Student('Aditya', 1)


# In[6]:


s1.show()


# In[7]:


class Student:
    
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()
        
    def show(self):
        print(self.name, self.roll)
        
    class Laptop:
        
        def __init__(self):
            self.brand = 'ASUS'
            self.cpu = 'i9'
            self.ram = 32


# In[8]:


s1 = Student('Aditya', 1)


# In[9]:


s1.lap.brand


# In[10]:


s1.lap.cpu


# In[11]:


s1.lap.brand


# In[12]:


s1 = Student("Aditya", 1)
s2 = Student("Aman", 2)


# In[13]:


print(s1.lap.brand)
print(s2.lap.brand)


# In[14]:


lap1 = s1.lap
lap2 = s2.lap


# In[15]:


print(id(lap1))
print(id(lap2))


# In[16]:


class Student:
    
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        
    def show(self):
        print(self.name, self.roll)
        
    class Laptop:
        
        def __init__(self):
            self.brand = 'ASUS'
            self.cpu = 'i9'
            self.ram = 32


# In[17]:


s1 = Student("Aditya", 1)


# In[18]:


lap1 = s1.Laptop()


# In[19]:


class Student:
    
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        
    def show(self):
        print(self.name, self.roll)
        
    class Laptop:
        
        def __init__(self):
            self.brand = 'ASUS'
            self.cpu = 'i9'
            self.ram = 32
            
        def show(self):
            print(self.brand, self.cpu, self.ram)


# In[20]:


s1 = Student("Aditya", 1)
lap1 = s1.Laptop()


# In[21]:


s1.show()


# In[22]:


lap1.show()


# In[23]:


class Student:
    
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()
        
    def show(self):
        print(self.name, self.roll)
        
    class Laptop:
        
        def __init__(self):
            self.brand = 'ASUS'
            self.cpu = 'i9'
            self.ram = 32
            self.show()
            
        def show(self):
            print(self.brand, self.cpu, self.ram)


# In[24]:


s1 = Student("Aditya", 1)


# In[25]:


class Student:
    
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.show()
        self.lap = self.Laptop()
        
    def show(self):
        print(self.name, self.roll)
        
    class Laptop:
        
        def __init__(self):
            self.brand = 'ASUS'
            self.cpu = 'i9'
            self.ram = 32
            self.show()
            
        def show(self):
            print(self.brand, self.cpu, self.ram)


# In[26]:


s1 = Student("Aditya", 1)


# ## Inheritence

# ### Single Inheritence

# In[27]:


class A:
    
    def feature1(self):
        print("Feature 1 working")
        
    def feature2(self):
        print("Feature 2 working")


# In[28]:


a1 = A()


# In[29]:


a1.feature1()
a1.feature2()


# In[30]:


class A:
    
    def __init__(self):
        pass
    
    def feature1(self):
        print("Feature 1 working")
        
    def feature2(self):
        print("Feature 2 working")
        
        
class B:
    
    def __init__(self):
        pass
    
    def feature3(self):
        print("Feature 3 working")
        
    def feature4(self):
        print("Feature 4 working")


# In[31]:


a1 = A()


# In[32]:


a1.feature1()
a1.feature2()


# In[33]:


b1 = B()


# In[34]:


b1.feature3()
b1.feature4()


# In[35]:


b1.feature1()


# In[36]:


class A:
    
    def __init__(self):
        pass
    
    def feature1(self):
        print("Feature 1 working")
        
    def feature2(self):
        print("Feature 2 working")
        
        
class B(A):
    
    def __init__(self):
        pass
    
    def feature3(self):
        print("Feature 3 working")
        
    def feature4(self):
        print("Feature 4 working")


# In[37]:


b1 = B()


# In[38]:


b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()


# A is superclass/ parent class. 
# 
# B is subclass/ child class.

# ### MultiLevel Inheritence

# In[39]:


class A:
    
    def __init__(self):
        pass
    
    def feature1(self):
        print("Feature 1 working")
        
    def feature2(self):
        print("Feature 2 working")
        
        
class B(A):
    
    def __init__(self):
        pass
    
    def feature3(self):
        print("Feature 3 working")
        
    def feature4(self):
        print("Feature 4 working")
        

class C(B):
    
    def __init__(self):
        pass
    
    def feature5(self):
        print("Feature 5 working")


# In[40]:


c1 = C()


# In[41]:


c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()


# ### Multiple Inheritence

# In[42]:


class A:
    
    def __init__(self):
        pass
    
    def feature1(self):
        print("Feature 1 working")
        
    def feature2(self):
        print("Feature 2 working")
        
        
class B:
    
    def __init__(self):
        pass
    
    def feature3(self):
        print("Feature 3 working")
        
    def feature4(self):
        print("Feature 4 working")
        

class C(A, B):
    
    def __init__(self):
        pass
    
    def feature5(self):
        print("Feature 5 working")


# In[43]:


a1 = A()
b1 = B()
c1 = C()


# In[44]:


a1.feature1()
a1.feature2()


# In[45]:


b1.feature3()
b1.feature4()


# In[46]:


c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()


# ### Constructer Inheritence

# In[47]:


class A:
    
    def __init__(self):
        print("In A's init")
    
    def feature1(self):
        print("Feature 1 working")
        
    def feature2(self):
        print("Feature 2 working")
        
        
class B(A):
    
    # We dont have B's init
    
    def feature3(self):
        print("Feature 3 working")
        
    def feature4(self):
        print("Feature 4 working")


# In[48]:


a1 = A()


# In[49]:


a1.feature1()
a1.feature2()


# In[50]:


b1 = B()


# In[51]:


class A:
    
    def __init__(self):
        print("In A's init")
    
    def feature1(self):
        print("Feature 1 working")
        
    def feature2(self):
        print("Feature 2 working")
        
        
class B(A):
    
    def __init__(self):
        print("In B's init")
    
    def feature3(self):
        print("Feature 3 working")
        
    def feature4(self):
        print("Feature 4 working")


# In[52]:


a1 = A()


# In[53]:


a1.feature1()
a1.feature2()


# In[54]:


b1 = B()


# If you create the object for subclass, it will first try to find init in subclass itself, if its not there, then it will go for the superclass's init.

# In[55]:


class A:
    
    def __init__(self):
        print("In A's init")
    
    def feature1(self):
        print("Feature 1 working")
        
    def feature2(self):
        print("Feature 2 working")
        
        
class B(A):
    
    def __init__(self):
        super().__init__()
        print("In B's init")
    
    def feature3(self):
        print("Feature 3 working")
        
    def feature4(self):
        print("Feature 4 working")


# In[56]:


b1 = B()


# In[57]:


class A:
    
    def __init__(self):
        print("In A's init")
    
    def feature1(self):
        print("Feature 1 working")
        
    def feature2(self):
        print("Feature 2 working")
        
        
class B:
    
    def __init__(self):
        print("In B's init")
    
    def feature3(self):
        print("Feature 3 working")
        
    def feature4(self):
        print("Feature 4 working")
        

class C(A, B):
    
    def __init__(self):
        print("In C's init")
        
    def feature5(self):
        print("Feature 5 working")


# In[58]:


c1 = C()


# In[59]:


class A:
    
    def __init__(self):
        print("In A's init")
    
    def feature1(self):
        print("Feature 1 of A working")
        
    def feature2(self):
        print("Feature 2 working")
        
        
class B:
    
    def __init__(self):
        print("In B's init")
    
    def feature1(self):
        print("Feature 1 of B working")
        
    def feature3(self):
        print("Feature 3 working")
        

class C(A, B):
    
    def __init__(self):
        super().__init__()
        print("In C's init")
        super().feature3()
        
    def feature4(self):
        print("Feature 4 working")


# In[60]:


c1 = C()


# #### Method Resolution Order
# 
# Object of child class in case of multiple inheritence prefers to go with leftmost class's init

# In[61]:


c1.feature1()


# ## Polymorphism
# 
# Multiple Forms/ Behavious of Objects.
# 
# Ways to implement Polymorphism are:
# 1. Duck Typing
# 2. Operator Overloading
# 3. Method Overloading
# 4. Method Overriding
# 

# ### Duck Typing

# If it looks like a duck,
# swims like a duck, 
# quacks like a duck, 
# then its probably a duck.

# In[62]:


x = 5


# In[63]:


id(x)


# In[64]:


x = "Aditya"


# In[65]:


id(x)


# In[66]:


x = "Aditya"


# In[67]:


id(x)


# In[68]:


x = ""


# In[69]:


id(x)


# In[70]:


y = x


# In[71]:


id(y)


# In[72]:


id(x) == id(y)


# In[73]:


class Laptop:
    
    def __init__(self):
        pass
    
    def code(self, ide):
        ide.execute()
        
class PyCharm:
    
    def __init__(self):
        pass
    
    def execute(self):
        print("Compiling")
        print("Running")


# In[74]:


lap1 = Laptop()


# In[75]:


lap1.code()


# In[76]:


ide = PyCharm()


# In[77]:


lap1.code(ide)


# In[78]:


class Laptop:
    
    def __init__(self):
        pass
    
    def code(self, ide):
        ide.execute()
        
class PyCharm:
    
    def __init__(self):
        pass
    
    def execute(self):
        print("Compiling")
        print("Running")
        
class MyCharm:
    
    def __init__(self):
        pass
    
    def execute(self):
        print("Spell Check")
        print("Debugging")
        print("Compiling")
        print("IPython Support")
        print("CUDA")


# In[79]:


ide = MyCharm()


# In[80]:


lap1.code(ide)


# ### Operator Overloading

# In[81]:


5 + 6


# 5 and 6 are operands,
# "+" is addition operator

# In[82]:


a = 5
b = 6


# In[83]:


a + b


# In[84]:


a = 5
b = "Aditya"


# In[85]:


a + b


# In[86]:


int.__add__(a, b)


# In[87]:


a = 5
b = 6


# In[88]:


int.__add__(a, b)


# In[89]:


a = "Aditya"
b = " Dwivedi"


# In[90]:


str.__add__(a, b)


# In[91]:


#  + - __add__()
#  - - __sub__()
#  * - __mul__()
# ..... magic methods


# In[92]:


class Student:
    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2


# In[93]:


s1 = Student(55, 56)
s2 = Student(60, 66)


# In[94]:


s3 = s1 + s2


# In[95]:


class Student:
    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        
    # Overloading Operator    
    def __add__(self, obj):
        m1 = self.m1 + obj.m1
        m2 = self.m2 + obj.m2
        s3 = Student(m1, m2)
        return s3


# In[96]:


s1 = Student(34, 45)
s2 = Student(43, 37)


# In[97]:


s3 = s1 + s2


# In[98]:


s3


# In[99]:


s3.m1


# In[100]:


s3.m2


# In[101]:


if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")


# In[102]:


class Student:
    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        
    # Overloading Operator    
    def __add__(self, obj):
        m1 = self.m1 + obj.m1
        m2 = self.m2 + obj.m2
        s3 = Student(m1, m2)
        return s3
    
    # Overloading Operator
    def __gt__(self, obj):
        s1 = self.m1 + self.m2
        s2 = obj.m1 + obj.m2
        if s1 > s2:
            return True
        else:
            return False


# In[103]:


s1 = Student(34, 45)
s2 = Student(43, 37)


# In[104]:


if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")


# In[105]:


print(s1)


# In[106]:


print(s1.__str__())


# In[107]:


class Student:
    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        
    # Overloading Operator    
    def __add__(self, obj):
        m1 = self.m1 + obj.m1
        m2 = self.m2 + obj.m2
        s3 = Student(m1, m2)
        return s3
    
    # Overloading Operator
    def __gt__(self, obj):
        s1 = self.m1 + self.m2
        s2 = obj.m1 + obj.m2
        if s1 > s2:
            return True
        else:
            return False
        
    def __str__(self):
        return "{} {}".format(self.m1, self.m2)


# In[108]:


s1 = Student(23, 45)


# In[109]:


print(s1)


# In[110]:


s1


# In[111]:


s1.__str__()


# ### Method Overloading

# Its not supported in Python
# 
# It means that if we have two functions with same name which have two parameters,
# 
# for eg,
# 1. def average(a, b)
# 2. def average(a, b, c)
# 
# 
# Try to implement this, you have to implement your own logic

# ### Method Overriding
# 
# You have two methods of same name and same parameters.
# 
# Try to implement it in Python, you have to implement it in Python. 
# 
# Make sure you are implementing it in different classes. And concept of inheritence will work here.
