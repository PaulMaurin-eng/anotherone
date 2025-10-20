#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:00:42 2025

@author: paulmaurin
"""

#LSP


class Vehicle:
    
    def __init__(self, speed ) :
        self.speed = speed
        
        
    def accelerate(self, increment):
        self.speed += increment
        print(f"You speed is {self.speed} KM/H")
        
        
    def brake(self, decrement):
        self.speed -= decrement 
        if self.speed <= 0:
            print( "you have stopped")
        if self.speed > 0:
            print(f"You speed is {self.speed} KM/H")
    
    
class Moto(Vehicle):
    
    def accelerate(self,increment):
        print("Your moto is accelerating")
        super().accelerate(increment)
    
    def brake(self,decrement):
        print("Your moto is slowing")
        super().brake(decrement)
             
  
class Car(Vehicle):
    
    def accelerate(self,increment):
        print("Your car is accelerating")
        super().accelerate(increment)
    
    def brake(self,decrement):
        print("Your car is slowing")
        super().brake(decrement)
        
    
class Quad(Vehicle):
    
    def accelerate(self,increment):
        print("Your quad is accelerating")
        super().accelerate(increment)
    
    def brake(self,decrement):
        print("Your quad is slowing")
        super().brake(decrement)
    
   
# starting at a speed of 0  
moto = Moto(0)
print(moto.accelerate(15))  
print(moto.brake(6))  

car = Car(0)
print(car.accelerate(10))  
print(car.brake(10))
    
quad = Quad(0)
print(quad.accelerate(5))  
print(quad.brake(3))



#starting at a speed of 40

moto = Moto(40)
print(moto.accelerate(15))  
print(moto.brake(6))  

car = Car(40)
print(car.accelerate(10))  
print(car.brake(10))
    
quad = Quad(40)
print(quad.accelerate(5))  
print(quad.brake(3))








    
    
    