#!/usr/bin/env python
# coding: utf-8

# In[12]:


number = [7,5,7,4,3,10,12,55,7,12,3]

rem_dup = list(set(number))

rem_dup.sort()

minimum = min(rem_dup)
maximum = max(rem_dup)
average = sum(rem_dup)/len(rem_dup)

print('Original list is: ', number)
print('Unique list is: ', rem_dup)
print('Sorted list is: ', rem_dup)
print('Minimum number is: ', minimum)
print('Maximum number is: ', maximum)
print("Average of list is: ", average)


# In[ ]:





# In[ ]:




