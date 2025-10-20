#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 10:44:56 2025

@author: paulmaurin
"""

#LSP

#incorrecto 

class Bird:
    def fly(self):
        print("flying")
        
        
class Chicken(Bird):
    def fly(self):
        return Exception(print("Chicken don't fly"))
    
    
    
bird = Bird()
bird.fly()
chicken = Chicken()
chicken.fly()
    


#correcto


class Bird2:
    def move(self):
        return "Moving"
    
    
class Chicken2(Bird2):
    def move(self):
        return "Walking"
    
bird2 = Bird2()
print(bird2.move())
chicken2 = Chicken2
print(chicken2.move)


bird3 = Chicken2()
print(bird3.move())
chicken3 = Bird2
print(chicken3.move)
    
    
    
    




