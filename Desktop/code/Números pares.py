#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:03:56 2025

@author: paulmaurin
"""

"""
Even numbers in a list
Description: Given a list of integers, create a function that returns a new list containing only the even numbers.
"""

list1 = [1,5,24,7,3,2,8,4,4,6,887,0,34,99,600000]





def even(lis):
    index = len(lis)
    print(index)
    i=0
    list_even= []
    list_odd =[]
    while i != index:
        print(f"num {i}")
        if lis[i] %2 == 0:
            list_even.append(lis[i])
            
        else: list_odd.append(lis[i])
        i +=1 
      
    print(list_even)
    print(list_odd)
    
    
    
even(list1)


