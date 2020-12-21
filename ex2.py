#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[4]:


def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr


# In[9]:


def listMaker():
    l1 = []
    l2 = []
    for i in range(15):
        l1.append(random.randint(0,100))
        l2.append(random.randint(0,100))
    #can either use bubble sort or list sorting
    l1 = bubbleSort(l1)
    l2 = bubbleSort(l2)
    l3 = l1+l2
    l3 = bubbleSort(l3)
    print(l3)


# In[15]:


def stringSorter(text):
    l = list(text)
    l.sort()
    l = ''.join(l)
    print(l)


# In[18]:


listMaker()
text = input("Input a string to be sorted: ")
stringSorter(text)


# In[ ]:




