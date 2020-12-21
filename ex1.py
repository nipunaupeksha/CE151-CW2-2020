#!/usr/bin/env python
# coding: utf-8

# In[8]:


def isPalindrome(text1, text2):
    text1 = text1.replace(" ","")
    text2 = text2.replace(" ","")
    text3 = text1[::-1]
    text4 = text2[::-1]
    
    if text1==text3 and text2==text4:
        return True
    else:
        return False


# In[5]:


def isPalindromeIgnoreCase(text1):
    text1 = text1.replace(" ","")
    text1 = text1.casefold()
    text2 = text1[::-1]
    
    return text1==text2


# In[11]:


text1 = input("Input first string: ")
text2 = input("Input second string: ")
b = isPalindrome(text1,text2)
if b==True:
    print("Both strings are palindromes")
else:
    print("Either one string or both of them are not palindromes")
    
text3 = input("Input a sentence: ")
b = isPalindromeIgnoreCase(text3)
if b==True:
    print("The sentence is palindromic")
else:
    print("The sentence is not palindromic")


# In[ ]:




