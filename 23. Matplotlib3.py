#!/usr/bin/env python
# coding: utf-8

# # Visualising Time Series Data
# 
# In the section, we will explore ways to visualise data gathered over time. We will:
# - Plot simple time series plots
# - Derive variables such as month and year and use them for richer visualisations
# 
# 

# In[1]:


# loading libraries and reading the data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set seaborn theme if you prefer
sns.set(style="white")

# read data
market_df = pd.read_csv("./global_sales_data/market_fact.csv")
customer_df = pd.read_csv("./global_sales_data/cust_dimen.csv")
product_df = pd.read_csv("./global_sales_data/prod_dimen.csv")
shipping_df = pd.read_csv("./global_sales_data/shipping_dimen.csv")
orders_df = pd.read_csv("./global_sales_data/orders_dimen.csv")


# ## Visualising Simple Time Series Data
# 
# Let's say you want to visualise numeric variables such as ```Sales```, ```Profit```, ```Shipping_Cost``` etc. over time. 

# In[2]:


market_df.head()


# Since the ```Order_Date``` variable is in the orders dataframe, let's merge it.

# In[3]:


# merging with the Orders data to get the Date column
df = pd.merge(market_df, orders_df, how='inner', on='Ord_id')
df.head()


# In[4]:


# Now we have the Order_Date in the df
# It is stored as a string (object) currently
df.info()


# Since ```Order_Date``` is a string, we need to convert it into a ```datetime``` object. You can do that using ```pd.to_datetime()```. 

# In[5]:


# Convert Order_Date to datetime type
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Order_Date is now datetime type
df.info()


# Now, since on each day, multiple orders were placed, we need to aggregate ```Sales``` using a metric such as mean, median etc., and then create a time series plot.
# 
# We will group by ```Order_Date``` and compute the sum of ```Sales``` on each day.

# In[6]:


# aggregating total sales on each day
time_df = df.groupby('Order_Date')['Sales'].sum()
print(time_df.head())

print(type(time_df))


# We can now create a time-series plot using ```sns.tsplot()```.

# In[7]:


# time series plot

# figure size
plt.figure(figsize=(16, 8))

# tsplot
sns.tsplot(data=time_df)
plt.show()


# ### Using Derived Date Metrics for Visualisation
# 
# It is often helpful to use derived variables from date such as month and year and using them to identify hidden patterns.

# In[8]:


# extracting month and year from date

# extract month
df['month'] = df['Order_Date'].dt.month

# extract year
df['year'] = df['Order_Date'].dt.year

df.head()


# Now you can plot the average sales across years and months.

# In[9]:


# grouping by year and month
df_time = df.groupby(["year", "month"]).Sales.mean()
df_time.head()


# In[10]:


plt.figure(figsize=(8, 6))
# time series plot
sns.tsplot(df_time)
plt.xlabel("Time")
plt.ylabel("Sales")
plt.show()


# There is another way to visualise numeric variables, such as ```Sales```, across the year and month. We can pivot the ```month``` column to create a wide-format dataframe, and then plot a heatmap.
# 

# In[11]:


# Pivoting the data using 'month' 
year_month = pd.pivot_table(df, values='Sales', index='year', columns='month', aggfunc='mean')
year_month.head()


# You can now create a heatmap using ```sns.heatmap()```.

# In[12]:


# figure size
plt.figure(figsize=(12, 8))

# heatmap with a color map of choice
sns.heatmap(year_month, cmap="YlGnBu")
plt.show()


# ### Addtional Reading on Time Series Plots and Heatmaps
# 
# 1. <A href="https://seaborn.pydata.org/generated/seaborn.heatmap.html">Seaborn heatmaps (documentation)</a>
# 
