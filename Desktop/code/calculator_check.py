#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 12:35:32 2025

@author: paulmaurin
"""



class opera:
    def calc(self, a,b):
        pass
    
    
class add(opera):
    def calc(self, a,b):
        return a+b
    
class take(opera):
    def calc(self, a,b):
        return a-b
    
class multi(opera):
    def calc(self, a,b):
        return a*b
class devi(opera):
    def calc(self, a,b):
        return a/b
    
class calculate:
    def __init__(self):
        self.opera = {}
        
    def add_opera(self, name , opera):
        self.opera[name] = opera
        
    def actual(self, name, a,b):
        return self.opera[name].calc(a,b)
        
        
num1 = calculate()

num1.add_opera("Addition", add())
num1.add_opera("Substraction", take())
num1.add_opera("Multiplication", multi())
num1.add_opera("Division", devi())


print(num1.actual("Addition", 10,5))

