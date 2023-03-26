#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Generate a random number

import random 

num = random.randint(1,10)

print(num)


# In[11]:


num = random.randrange(100,200,2)

print(num)


# In[12]:


num = random.uniform(50,10)
print(num)


# In[13]:


numlist= random.sample(range(150,250),15)
print(numlist)


# In[14]:


numList = [1,2,3,4,8]

random.shuffle(numList)
print(numList)


# In[15]:


print(random.choice(numList))


# In[ ]:




