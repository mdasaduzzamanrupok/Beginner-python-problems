#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Sum of digits of a given number 

i = int(input("Enter number to find sum of digits: "))

sum = 0 

while (i>0):
    sum = sum+i%10
    i =i//10
    
print("Sum of digits : ", sum)


# In[ ]:





# In[ ]:




