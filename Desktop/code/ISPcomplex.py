#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 12:35:51 2025

@author: paulmaurin
"""

#ISP complex

from abc import ABC,abstractmethod


class Only_wb(ABC):
    
    @abstractmethod
    def print_job(self):
       pass
 
    
class Only_color(ABC):
    
    
    @abstractmethod 
    def print_colo(self):
        pass
 
    
class Fax(ABC):
    
    @abstractmethod 
    def faxing(self):
        pass
    
class Scan(ABC):
    
    @abstractmethod 
    def scanned(self):
        pass
    
    



class Classic(Only_wb):
     
    def print_job(self):
        print("I am printing in black and white")
    
         
    
class Multi(Only_wb,Only_color):
    
    def print_job(self):
        print("I am printing in black and white")
        
    def print_colo(self):
        print("I am printing in colors")
       
    
class Everyth(Only_wb,Only_color,Fax,Scan):
    
    def print_job(self):
        print("I am printing in black and white")
        
    def print_colo(self):
        print("I am printing in colors")
        
    def faxing(self):
        print("I am sending a fax")
        
    def scanned(self):
        print("I am scanning a document")
        
        
num1 = Everyth()
num1.faxing()
num1.scanned()
num1.print_job()
num1.print_colo()

num2 = Multi()
num2.print_job()
num2.print_colo()

num3 = Classic()
num3.print_job()
    
    
    
    
    
    
    
    
    
    
    
    
    