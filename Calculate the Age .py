#!/usr/bin/env python
# coding: utf-8

# In[5]:


#calculate the age 

from datetime import date 

birth_day = int(input("Enter your day of birth: "))
birth_month = int(input("Enter your month of birth: "))
birth_year = int(input("Enter your year of birth: "))

current_day = date.today().day
current_month = date.today().month
current_year = date.today().year

Age_day = current_day-birth_day
Age_month = current_month-birth_month
Age_year = current_year-birth_year

print(f"Your age is : {Age_year} years, {Age_month} months, {Age_day} days")


# In[ ]:




