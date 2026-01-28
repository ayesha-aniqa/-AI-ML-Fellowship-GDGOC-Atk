#!/usr/bin/env python
# coding: utf-8

# # Fabonacci Generator

# In[ ]:


import pdb

def fibonacci_generator(n):
    a, b = 0, 1
    pdb.set_trace()          # Debugging starts here
    for i in range(n):
        yield a
        a, b = b, a + b


for num in fibonacci_generator(15):
    print(num)


# # Custom range generator

# In[6]:


import pdb

def custom_range(start, end, step):
    pdb.set_trace()          # Debugging starts here
    while start < end:
        yield start
        start += step


# Using the generator
for value in custom_range(1, 10, 2):
    print(value)


# In[ ]:





# In[ ]:




