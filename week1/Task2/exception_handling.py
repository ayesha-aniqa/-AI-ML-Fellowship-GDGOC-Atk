#!/usr/bin/env python
# coding: utf-8

# In[6]:


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number"))
    op = input("Choose operator: + - * /")
    
    if op == '+':
        result = num1+num2
    elif op == '-':
        result =  num1-num2
    elif op == '*':
        result = num1*num2
    elif op =='/':
        result = num1/num2
    else: 
        print("Invalid operator")
        result = None
        
        #exceptions handling
except ValueError:
    print("please enter valid input ")

except ZeroDivisionError:
    print("number can't be divided with 0")

else:    
    if result is not None:
        print("Result is ", result)
        
finally:
    print("Calculator Finished.")


# In[ ]:




