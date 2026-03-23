#!/usr/bin/env python
# coding: utf-8

# In[2]:


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
        
        
#functions calling

print(add(2,3,4,5,67,9))

print(average(4,6,7,2,4.5))

print(my_info(name='Ayesha',role='Student',degree='BSAI'))


# In[ ]:




