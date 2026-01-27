#!/usr/bin/env python
# coding: utf-8

# In[4]:


#setting the number
number = 75

while True:
    guess=int(input('Guess the number:'))
    if guess > number:
        print('You guessed greater number')
    elif guess < number:
        print( 'You guessed smaller number')
    else: 
        print('Your guess is correct.', number)
        break
    


# In[ ]:




