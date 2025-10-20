#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 12:49:59 2025

@author: paulmaurin
"""




class Vehicle:
    def __init__(self, speed):
        self.speed = speed
       
        
    def acceleration(self,  incr):
        self.speed += incr
        print(f"You are acceleration by {incr} you are now at {self.speed}")
    
    def slowing(self,  incr):
        self.speed -= incr
        print(f"You are slowing by {incr} you are now at {self.speed}")
    
    
    
    
class Moto(Vehicle):
    def acceleration(self, incr):
        super().acceleration(incr)
    
    def slowing(self, incr):
        super().slowing( incr)
    
    
    
class Car(Vehicle):
    def acceleration(self,incr):
        super().acceleration(incr)
    
    def slowing(self, incr):
        super().slowing( incr)
    
    
    
    
class Quad(Vehicle):
    def acceleration(self, incr):
        super().acceleration( incr)
    
    def slowing(self, incr):
        super().slowing( incr)
        
        
        
moto = Moto(0)
moto.acceleration(10)


moto = Moto(10)
moto.acceleration(40)
moto = Moto(80)
moto.acceleration(10)

moto.slowing(30)


