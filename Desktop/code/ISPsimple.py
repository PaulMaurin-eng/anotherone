#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 12:17:54 2025

@author: paulmaurin
"""

#ISP

# Without ISP

from abc import ABC, abstractmethod


class WorkerInterface(ABC):
    
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    
class Worker(WorkerInterface):
    
    def work(self):
        print("I am working")
        
    def eat(self):
        print("I am eating")
        
        
class Robot(WorkerInterface):
     
    def work(self):
         print("I am working")
         
    def eat(self):
         pass      
        
        
        
robot = Robot()
robot.eat()
robot.work()

worker = Worker()
worker.eat()
worker.work()






#With ISP


from abc import ABC, abstractmethod


class WorkerInterface(ABC):
    
    @abstractmethod
    def work(self):
        pass
    
    
    
class EatingInterface(ABC):
    
    @abstractmethod
    def eat(self):
        pass
    
    
class Worker(WorkerInterface,EatingInterface):
    
    def work(self):
        print("I am working")
        
    def eat(self):
        print("I am eating")
        
        
class Robot(WorkerInterface):
     
    def work(self):
         print("I am working")
         
    
    
robot = Robot()

robot.work()

worker = Worker()
worker.eat()
worker.work() 
    
























#Correcta