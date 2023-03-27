#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Remove duplicate from a list 

list_one = [1,2,3,4,5,6,7,7,8,9,100,200,300,47]

list_two = [1,3,5,8,6,8,4,5,10,5,14,49,17,25,4]


list_three = list_one+list_two

unique_list = []

for i in list_three:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)    


# In[ ]:




