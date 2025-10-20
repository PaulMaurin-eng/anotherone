#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 12:59:52 2025

@author: paulmaurin
"""

# DIP


#Without


class Switch:
    
    
    def turn_on(self):
        print("It's on")
        
    def turn_off(self):
        print("It's off")
        

class Lampe:
    
    def __init__(self, ):
        self.switch = Switch()
        
    def operate(self, command):
        if command == "On":
            self.switch.turn_on()
            
        if command == "Off":
            self.switch.turn_off()
            
        
        

lampe = Lampe()
num1 = input("on or off    ")
lampe.operate(num1)

num2 = input("and now?    ")
lampe.operate(num2)



#With




class AbstractSwitch:
    
    
    def turn_on(self):
        pass
        
    def turn_off(self):
        pass


class LightSwitch(AbstractSwitch):
    
    
    def turn_on(self):
        print("It's on")
        
    def turn_off(self):
        print("It's off")
        
class Lampe():
    
    def __init__(self, switch:AbstractSwitch ):
        self.switch = switch
        
    def operate(self, command):
        if command == "On":
            self.switch.turn_on()
            
        if command == "Off":
            self.switch.turn_off()
        
        
        
lampe = Lampe(LightSwitch())
num1 = input("on or off    ")
lampe.operate(num1)

num2 = input("and now?    ")
lampe.operate(num2)










