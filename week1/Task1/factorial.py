#!/usr/bin/env python
# coding: utf-8

# In[17]:


#input for finding factorial
num = int(input('Enter a number for factorial:\n'))
factorial=1

#calcuating factorial
if num == 0:
    factorial = 1
for i in range  (1, num+1):
    factorial *= i
  

#printing the factorial
print('factorial of the number ', num, ' is ',factorial)


# In[ ]:





# In[ ]:




