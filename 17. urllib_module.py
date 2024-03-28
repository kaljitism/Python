#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
For importing or downloading Data from the web, we use urllib.
"""
print()


# In[2]:


"""
URL - Universal/Uniform Resource Locator

They are nothing but reference to web resources

Here, our focus will be only on web addresses..

They are consist of: 
    # Protocol Identifier - https: or http:
    # Resource Name: kaljit.com
"""
print()


# In[4]:


"""
HTTP: HyperText Transfer Protocol
HTTPS: HyperText Transfer Protocol Secure

Communication between client computers and web servers is done
by sending HTTP/ HTTPS requests and recieving HTTP / HTTPS Response.
"""
print()


# In[6]:


"""
Going to website: Sending HTTP request or get request()
When we use urlretrieve() of urllib, we are using get request
"""
print()


# In[8]:


"""
Apart from recieving data from get request, it saves files and all
locally.
"""
print()


# In[10]:


from urllib import request


# In[19]:


url = 'http://files.pushshift.io/reddit/comments/RC_2007-01.bz2'
request.urlretrieve(url, 'RC_2007-02.bz2')


# In[ ]:





# In[ ]:





# In[ ]:





# In[20]:


"""
os
sys
urllib
numpy
pandas
matplotlib
seaborn
json
sqlAlchemy/ SQLite3
sklearn and statsmodel
Deep Learning - keras, tensorflow, pytorch
NLP - NLTK, Spacy and Gensim
Computer Vision - OpenCV
"""


# In[ ]:


"""
Blogs of whatever I have taught to you...
Python...
Numpy, Pandas, Matplotlib... 
EDA.. Stats.. 
All Machine Learning Algos...
"""
# Blogs will be linked to my Github

kaljit.com

