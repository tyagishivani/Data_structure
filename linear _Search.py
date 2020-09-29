# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:34:56 2020

@author: DELL
"""

####Linear Search #######
def linear(arr,key):
    for i in range(0,len(arr)):
        if (arr[i]==key):
            return i
    else:
        return -1

arr = [10,20,30,50]
k = 50
print(linear(arr,k))



# Time Complexity = O(n)
#space complexity = O(1)