#!/usr/bin/env python
# coding: utf-8

# In[6]:


#utility add function
def add(*args):
    return sum(args)

#utility avaerage function
def average(*args):
    return sum(args) / len(args)

#utility information/data function
def my_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

        


# In[ ]:





# In[ ]:





# In[ ]:




