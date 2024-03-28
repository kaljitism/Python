#!/usr/bin/env python
# coding: utf-8

# # Basic Plotting: Introduction to ```matplotlib```
# 
# In this section, we will:
# - Create basic plots using ```matplotlib.pyplot```
# - Put axis labels and titles
# - Create multiple plots (subplots) in the same figure
# - Change the scales of x and y axes
# - Create common types of plots: Histograms, boxplots, scatter plots etc. 
# - Working with images
# 
# ```matplotlib``` is a python library. It contains the ```pyplot``` module, which is basically a collection of functions such as ```plot```, ```title```, ```show()``` etc. ```pyplot``` is one of the most commonly used module for creating a variety of plots such as line plots, bar plots, histograms etc. 
# 
# Let's start with the basics.

# ## Basic Plotting, Axes Labels and Titles

# In[1]:


get_ipython().system('pip install matplotlib')


# In[2]:


import matplotlib.pyplot as plt


# In[4]:


x = [1, 2, 3, 4, 5]
y = x


# In[13]:


plt.plot(x, y)
plt.title('Straight Line')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()


# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[16]:


x_1 = np.arange(1, 11, 0.5)
y_1 = x_1 ** 2


# In[17]:


x_1


# In[18]:


y_1


# In[26]:


plt.scatter(x_1, y_1, s=5, c='k') # Plotting
# 'b' = blue, 'k' = black, 'g' = green, 'y' = yellow
plt.title('Quadratic Function')
plt.xlabel('X')
plt.ylabel('f(X) = X**2')
plt.show()


# In[27]:


x = [1, 2, 4, 54, 23, 74, 2]
y = [23, 53, 63, 24, 65, 23, 2]


# In[29]:


plt.plot(x, y)


# In[4]:


linear_space = np.linspace(1, 20, 100)


# In[5]:


linear_space


# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Plotting two 1-D numpy arrays
x = np.linspace(5, 1000, 100)
y = np.linspace(10, 1000, 100)

plt.plot(x, y)


# In[16]:


# need to call plt.show() explicitly to display the plot
plt.show()


# In[18]:


# can also work with lists, though it converts lists to np arrays internally
plt.plot([1, 4, 6, 8], [3, 8, 3, 5])
plt.show()


# Let's see how to put labels and the x and y axes and the chart title. 
# 
# Also, you can specify the limits of x and y labels as a range using ```xlim([xmin, xmax])``` and ```ylim([ymin, ymax])```.
# 

# In[23]:


# Axis labels and title
x = np.arange(1000)
y = x
plt.plot(x, y)

# x and y labels, and title
plt.xlabel("Current")
plt.ylabel("Voltage")
plt.title("Ohm's Law")

# Define the range of labels of the axis 
# Arguments: plt.axis(xmin, xmax, ymin, ymax)
plt.xlim([20, 80])
plt.ylim([20, 80])
plt.show()


# In[43]:


# Change the colors and line type

# initialising x and y arrays
x = np.linspace(0, 10, 20)
y = x*2

# color blue, line type '+'
plt.plot(x, y, 'b+')

# put x and y labels, and the title
plt.xlabel("Current")
plt.ylabel("Voltage")
plt.title("Ohm's Law")

plt.show()


# In[26]:


# Plotting multiple lines on the same plot

x = np.linspace(0, 5, 10)
y = np.linspace(3, 6, 10)

# plot three curves: y, y**2 and y**3 with different line types
plt.plot(x, y, 'r-', x, y**2, 'b+', x, y**3, 'g^')
plt.show()


# ## Figures and Subplots
# 
# You often need to create multiple plots in the same figure, as we'll see in some upcoming examples.
# 
# 
# ```matplotlib``` has the concept of **figures and subplots** using which you can create *multiple subplots inside the same figure*.   
# 
# To create multiple plots in the same figure, you can use the method ```plt.subplot(nrows, ncols, nsubplot)```.

# In[27]:


x = np.linspace(1, 10, 100)
y = np.log(x)

# initiate a new figure explicitly 
plt.figure(1)

# Create a subplot with 1 row, 2 columns 

# plt.subplot(a, b, c) or plt.subplot(abc)
# a = number of rows
# b = number of columns
# c = figure number or position in the figure

# create the first subplot in figure 1 
plt.subplot(121)     # equivalent to plt.subplot(1, 2, 1)
plt.title("y = log(x)")
plt.plot(x, y)

# create the second subplot in figure 1
plt.subplot(122)
plt.title("y = log(x)**2")
plt.plot(x, y**2)

plt.show()


# Let's see another example - say you want to create 4 subplots in two rows and two columns.

# In[9]:


# Example: Create a figure having 4 subplots
x = np.linspace(1, 10, 100)

# Optional command, since matplotlib creates a figure by default anyway
plt.figure(1)

# subplot 1
plt.subplot(2, 3, 1)
plt.title("Linear")
plt.plot(x, x)


# subplot 2 
plt.subplot(2, 3, 3)
plt.title("Cubic")
plt.plot(x, x**3)

# figure 2
plt.figure(2)

# subplot 1
plt.subplot(2, 3, 1)
plt.title("Log")
plt.plot(x, np.log(x))

# subplot 2
plt.subplot(2, 3, 3)
plt.title("Exponential")
plt.plot(x, np.exp(x))

plt.show()


# You can see the list of colors and shapes here: https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot

# ## Types of Commonly Used Plots
# 
# Let's now use the retail store's sales data to create some commonly use plots such as:
# - Boxplots
# - Histograms
# - Scatter plots
# - Bar plots

# In[35]:


# Example: Globals sales data
df = pd.read_csv("./global_sales_data/market_fact.csv")
df.head()


# ### Boxplot

# In[36]:


# Boxplot: Visualise the distribution of a continuous variable
plt.boxplot(df['Order_Quantity'])
plt.show()


# In[37]:


# Boxplot of Sales is quite unreadable, since Sales varies 
# across a wide range
plt.boxplot(df['Sales'])
plt.show()


# As you can see, the boxplot of ```Sales``` is pretty unreadable, since Sales varies across a wide range as shown below.

# In[38]:


# Range of sales: min is 2.24, median is 449, max is 89061
df['Sales'].describe()


# The solution to this problem is to **change the scale of the axis** (in this case, the y axis) so that the range can fit into the size of the plot.
# 
# 
# One commonly used technique is to transform an axis into the **logarithmic scale**. You can transform the scale of an axis using ```plt.yscale('log')```.

# In[13]:


# Usual (linear) scale subplot
plt.subplot(1, 2, 1)
plt.boxplot(df['Sales'])

# log scale subplot
plt.subplot(1, 2, 2)
plt.boxplot(df['Sales'])
plt.yscale('log')
plt.show()


# Clearly, the log scale subplot is far more readable - you can infer that the minimum sales is around 0, the median is approximtely in the middle of 100 and 1000, and the max is reaching 100,000.

# ### Histogram
# 
# Histograms are useful for visualising distribution of single variables.

# In[14]:


# Histograms
plt.hist(df['Sales'])
plt.show()


# In[15]:


# The histogram can be made more readable by using 
# a log scale

plt.hist(df['Sales'])
plt.yscale('log')
plt.show()


# ### Scatter Plot
# 
# Scatter plots are used to visualise two variables, one one each axis. 

# In[58]:


# Scatter plots with two variables: Profit and Sales
plt.scatter(df['Sales'], df['Profit'])
plt.show()


# ## Working with Images
# 
# ```matplotlib``` can also read images using the ```plt.imread()``` method. Internally, it reads and stores images as an ```array```. The array can then be used for various data manipulation tasks, just as a normal array.
# Let's look at an example.

# In[40]:


# reading a PNG/ JPEG/ JPG image
image = plt.imread("me.jpg")
plt.imshow(image)
plt.show()


# In[41]:


# looking at attributes of the image 
print(type(image))
print(image.shape)
print(image.dtype)


# Note that it is a 3-D array of size 960 x 720 x 3, and each element is stored as type float32. Let's look at the content of the array.

# In[42]:


# print the array
image


# In the array, each inner list is of dimension size =3 and represents a pixel. Since this is an RGB image, there are 3 pixels (other types of images are RGBA, where A is alpha and represents transparency).
# 
# We will not discuss images in detail in this module, though we'll work with them later in some machine learning modeling exercises. 

# In the next section, we will learn to visualise distributions using an differnt visualisation library, seaborn.

# ## Matplotlib Resources
# 1. <a href="https://matplotlib.org/users/pyplot_tutorial.html">Official documentation</a>
# 2. <a href="https://github.com/rougier/matplotlib-tutorial">Matplotlib tutorial showing a variety of plots</a>
# 
