#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 16:02:56 2025

@author: paulmaurin
"""





class shape:
    def draw(self):
        pass
    
class triangle(shape):
    def draw(self):
        print("it's a triangle")
        
class circle(shape):
    def draw(self):
        print("It's a circle")
        
class rectangle(shape):
    def draw(self):
        print("its a rectangle")
        
        

t = triangle()
t.draw() 
