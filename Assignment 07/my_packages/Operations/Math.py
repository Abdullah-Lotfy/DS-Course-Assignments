#!/usr/bin/env python
# coding: utf-8

# In[13]:


def get_average(*nums):
    summ=0
    for x in nums:
        summ+=x
    avg=summ/len(nums)
    return avg

