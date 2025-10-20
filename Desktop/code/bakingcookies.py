#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 11:01:32 2025

@author: paulmaurin
"""

class Cookie():
    def __init__(self, butter, egg, sugar):
        self.butter = butter
        self.egg = egg
        self.sugar = sugar
        
    def bake(self):
        print(f"You are baking a cookie with {self.butter}, {self.egg} and {self.sugar}. "  )
        
        
        
        
class Chocolate(Cookie):
    
    def __init__(self, butter, egg, sugar,chocolate):
        super().__init__(butter, egg, sugar)
        self.Chocolate = chocolate
        
    def bake(self):
        super().bake()
        print(f"and you add {self.Chocolate}")
        
        
class raisin(Cookie):
    
    def __init__(self, butter, egg, sugar,raisin):
      super().__init__(butter, egg, sugar)
      self.raisin = raisin
      
    def bake(self):
        super().bake()
        print(f"and you also added {self.raisin}")

     
        
ingre =[]     

ingre.append(input("what's the first ingredient you have"))
ingre.append(input("what's the second"))
ingre.append(input("what's the third"))
may = input("you have more?").strip()

if may:
    ingre.append(may)

if len(ingre) == 3:
    c = Cookie(*ingre)
    c.bake()

elif len(ingre) == 4:
    if ingre[3] == "chocolate":
        c2 = Chocolate(*ingre)
        c2.bake()
        
    elif ingre[3]=="raisin":
        c3 = raisin(*ingre)
        c3.bake()




        
    
    