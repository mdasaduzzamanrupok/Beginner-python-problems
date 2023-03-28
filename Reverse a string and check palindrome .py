#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Reverse a string and check palindrome

my_str = str(input())
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
    print("This is palindrome")
else:
    print("This is not palindrome")


# In[15]:


def reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev = reverse(s)
    if (s==rev):
        return True
   
        return false

s = input("Type a string: ")
if (isPalindrome(s)==1):
    print("This is a palindrome")
    
else:
    print("This is not a Palindrome")


# In[ ]:




