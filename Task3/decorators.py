#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[16]:


import time
#creating decorator
def exec_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        #my function is called
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Execution time is {end_time - start_time:.4f} seconds')
        return result
    return wrapper

#using decorator
@exec_time
def sum():
    total = 0
    for i in range(1_000_000):
        total += i
    print(f"Sum of 100 numbers is {total}")


sum()


# In[ ]:




