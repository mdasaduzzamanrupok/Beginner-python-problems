#!/usr/bin/env python
# coding: utf-8

# In[6]:


#check a Prime number 

num = int(input("Enter any integer value: "))
for i in range(2,num):
    if num%i==0:
        print('Not a prime number')
        break
else:
    print('oh! Its Prime Number')

