#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#number guessing game

from random import randint

for x in range(1,20):
    guessingNumber = int(input("Enter your guessing number 1 to 20: "))
    randomNumber = randint(1,20)
    if guessingNumber == randomNumber:
        print("You have won")
    else:
        print("your have lost")
        print("random number was : ", randomNumber)


# In[ ]:





# In[ ]:




