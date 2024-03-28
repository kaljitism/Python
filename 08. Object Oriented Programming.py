#!/usr/bin/env python
# coding: utf-8

# ### Class

# In[1]:


class Computer:
    
    # Attributes - Variables
    # Behaviours - Methods(Function)
    
    def config(self):
        print("Core i5")


# In[2]:


com1 = Computer()


# In[3]:


print(type(com1))


# In[4]:


config()


# In[5]:


Computer.config()


# In[6]:


Computer.config(com1)


# In[7]:


com2 = Computer()


# In[8]:


Computer.config(com2)


# In[9]:


com1.config()


# In[10]:


Computer().config()


# ### Constructor

# In[13]:


class Computer:
    
    def __init__(self):
        print('16 GB')
        self.config()
    
    def config(self):
        print("Core i5")


# In[14]:


com1 = Computer()
com2 = Computer()


# In[15]:


com1.config()


# In[16]:


com2.config()


# In[17]:


Computer().config()


# In[18]:


class Computer:
    
    def __init__(self, cpu, ram):
        cpu = 'i9'
        ram = 1024
    
    def config(self):
        print("Its CPU is ", cpu)
        print("Its RAM is ", ram)


# In[19]:


com1 = Computer()


# In[20]:


class Computer:
    
    def __init__(self, cpu='i9', ram=1024):
        cpu = cpu
        ram = ram
    
    def config(self):
        print("Its CPU is ", cpu)
        print("Its RAM is ", ram)


# In[22]:


Computer().config()


# In[23]:


class Computer:
    
    def __init__(self, cpu='i9', ram=1024):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("Its CPU is", self.cpu)
        print("Its RAM is", self.ram)


# In[24]:


Computer()


# In[25]:


com1 = Computer()


# In[26]:


com1.config()


# In[27]:


com1 = Computer('i3', 256)
com2 = Computer('i5', 512)
com3 = Computer('i9', 1024)


# In[28]:


com1.config()


# In[29]:


com2.config()


# In[30]:


com3.config()


# ### Object Comparison

# In[33]:


class Calculator:
    
    # Constructer
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    # Addition
    def sum(self):
        """Adds two Numbers"""
        return self.num1 + self.num2      # Sum
    
    # Substraction
    def diff(self):
        """Gives difference b/w two Numbers"""
        return abs(self.num1 - self.num2)      # Differnece
    
    # Multiplication
    def product(self):
        """Multiplies two Numbers"""
        return self.num1 * self.num2       # Product
    
    # Division
    def div(self):
        """Divide two Numbers"""
        return self.num1 / self.num2      # Quoteint


# In[34]:


class Computer:
    pass


# In[35]:


c1 = Computer()
id(c1)            # Objects are stored in Heap Memory


# In[36]:


c2 = Computer()
id(c2)


# In[37]:


class Computer:
    def __init__(self):
        self.name = "Aditya"
        self.age = 16


# In[38]:


c1 = Computer()


# In[39]:


c1.name


# In[40]:


c1.name = "A"


# In[41]:


c1.name


# In[42]:


c1.age = 17


# In[43]:


c1.age


# In[44]:


c2 = Computer()


# In[45]:


c2.name


# In[46]:


c2.age


# In[47]:


c1.name


# In[48]:


c1.age


# In[49]:


class Computer:
    def __init__(self):
        self.name = "Aditya"
        self.age = 16
        
    def update(self):
        self.age = 17


# In[65]:


Computer()


# In[50]:


c1 = Computer()


# In[52]:


c1.age


# In[53]:


c1.update()


# In[54]:


c1.age


# In[55]:


c2 = Computer()


# In[56]:


c2.age


# In[58]:


if c1 == c2:
    print(True)


# In[59]:


c1 = Computer()
c2 = Computer()


# In[60]:


if c1 == c2:
    print(True)


# In[61]:


c1 == c2


# In[66]:


if c1.age == c2.age:
    print(True)


# In[67]:


if c1.compare(c2):
    print(True)


# In[68]:


class Computer:
    def __init__(self):
        self.name = "Aditya"
        self.age = 16
        
    def update(self):
        self.age = 17
        
    def compare(self, obj):
        if self.age == obj.age:
            return True
        else:
            return False


# In[69]:


c1 = Computer()
c2 = Computer()


# In[70]:


if c1.compare(c2):
    print("They are same!")
else:
    print("Different!!!")


# In[71]:


c1.update()


# In[72]:


c1.compare(c2)


# ### Variable

# There are two types of Variables in OOP:
# 1. Instance Variable
# 2. Class(Static Variable)

# In[73]:


class Car:
    def __init__(self):
        
        # Instance Variable - As the object changes, these value changes
        
        self.mil = 10
        self.com = 'Maserati'


# In[74]:


c1 = Car()


# In[75]:


c2 = Car()


# In[76]:


c1.com, c1.mil


# In[77]:


c2.com, c2.mil


# In[78]:


c1.mil = 8


# In[79]:


print(c1.com, c1.mil)
print(c2.com, c2.mil)


# We are defining a varibale inside init, it is a instance variable. But when we define a varible outside init, it becomes the class varibale. Something which is static, like number of wheels, regardless of company or mileage. 

# In[81]:


class Car:
    
    # Class Variable
    wheels = 4
    
    def __init__(self):
        self.mil = 10
        self.com = "Maserati"


# In[82]:


c1 = Car()
c2 = Car()


# In our memory, we have namespaces.. Namespaces are the place where you create and store and object/ variable
# 1. Class Namespace
# 2. Object/ Instance Namespace

# In[83]:


c1.wheels


# In[84]:


c2.wheels


# In[91]:


c1.wheels = 5


# In[92]:


c1.wheels, c2.wheels


# In[93]:


Car.wheels = 5


# In[94]:


c1.wheels, c2.wheels


# In[95]:


Car.wheels = 10


# In[96]:


c1.wheels, c2.wheels


# In[97]:


c1 = Car()
c2 = Car()


# In[98]:


c1.wheels, c2.wheels


# In[99]:


Car.wheels = 8


# In[100]:


c1.wheels, c2.wheels


# ### Types of Methods
# 1. Instance Methods
# 2. Class Method
# 3. Static Method

# In[101]:


class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


# In[102]:


s1 = Student(25, 22, 76)
s2 = Student(12, 43, 67)


# In[103]:


class Student:
    
    school = "AI"
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        # Instace Method - Because it requires an instance variable to work
        return (self.m1 + self.m2 + self.m3)/ 3


# In[104]:


s1 = Student(25, 22, 76)
s2 = Student(12, 43, 67)


# In[105]:


s1.avg()


# In[106]:


s2.avg()


# Instance methods are of two types - 
# 1. Accessor Methods
# 2. Mutator Methods

# 1. Accessor Methods or Getter Fuctions get the value of object
# 2. Mutator Methods or Setter Functions change or update the value of object

# In[107]:


class Student:
    
    school = "AI"
    
    def __init__(self, m1=None, m2=None, m3=None):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/ 3
    
    # Getter Function - Accessor Method - Fetch the value
    def get_m1(self):
        return self.m1
    
    # Setter Function - Mutator Method - Update/ Change the value
    def set_m1(self, value):
        self.m1 = value


# In[108]:


s1 = Student()


# In[109]:


s1.get_m1()


# In[111]:


s1.set_m1(12)


# In[112]:


s1.get_m1()


# In[114]:


class Student:
    
    school = "AI"
    
    def __init__(self, m1=None, m2=None, m3=None):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/ 3
    
    def get_m1(self):
        return self.m1
    
    def set_m1(self, value):
        self.m1 = value
        
    # For instance Variable, keyword is self. For a class varible, the keyword is cls.    
    def info(cls):
        return cls.school


# In[115]:


s1 = Student()


# In[116]:


s1.info()


# In[118]:


Student.info(s1)


# In[119]:


Student().info()


# In[120]:


Student.info()


# In[121]:


class Student:
    
    school = "AI"
    
    def __init__(self, m1=None, m2=None, m3=None):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/ 3
    
    def get_m1(self):
        return self.m1
    
    def set_m1(self, value):
        self.m1 = value
        
    # We have to use decorators for explicitly defining the class method
    @classmethod
    def info(cls):
        return cls.school


# In[122]:


Student.info()


# In[123]:


class Student:
    
    school = "AI"
    
    def __init__(self, m1=None, m2=None, m3=None):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/ 3
    
    def get_m1(self):
        return self.m1
    
    def set_m1(self, value):
        self.m1 = value
        
    @classmethod
    def info(cls):
        return cls.school
    
    # Static Method
    def cls_info():
        print("Hey There, I am a static function")


# In[124]:


s1 = Student()


# In[125]:


s1.cls_info()


# In[126]:


Student.cls_info()


# In[132]:


class Student:
    
    school = "AI"
    
    def __init__(self, m1=None, m2=None, m3=None):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/ 3
    
    def get_m1(self):
        return self.m1
    
    def set_m1(self, value):
        self.m1 = value
        
    @classmethod
    def info(cls):
        return cls.school
    
    @staticmethod
    def cls_info():
        print("This is Student Class..")


# In[133]:


s1 = Student()


# In[138]:


s1.cls_info()


# In[130]:


Student.cls_info()

