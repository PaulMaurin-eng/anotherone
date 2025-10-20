#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 16:10:20 2025

@author: paulmaurin
"""



class operation:
    def calc(self, a ,b):
        pass



class addition(operation):
    def calc(self, a, b):
        return a + b
        
 

class substraction(operation):
    def calc(self, a, b):
        return a - b
   


class multiplication(operation):
    def calc(self, a, b):
        return a * b
    


class division(operation):
    def calc(self, a, b):
        return a / b
    
    
class calculator:
    def __init__(self):
        self.operation = {}
        
    def add_operation(self, name, operation):
        self.operation[name] = operation
        
    def calculate(self,name, a, b):
        return self.operation[name].calc(a,b)
        
       
        
calculat = calculator()  
calculat.add_operation("Addition",addition())
calculat.add_operation("Substraction",substraction())
calculat.add_operation("Multiplication",multiplication())
calculat.add_operation("Division",division())

print(calculat.calculate("Addition", 5,5))








