#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 12:28:48 2025

@author: paulmaurin
"""

#polymophism



class Shape:
    def area(self):
        return
        
        
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (self.radius**2)*3.14
    
    
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return (self.width *self.height )
    
    
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return (self.base *self.height)/2
    
    


shapes = [
    Circle(4),
    Rectangle(5, 3),
    Triangle(6, 2)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")