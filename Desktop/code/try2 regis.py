#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 12:33:54 2025

@author: paulmaurin
"""



#incorrr
library = []

class Regi:
    def __init__(self, email, name):
        self.email = email
        self.name = name
        
    def lis(self):
        library.append(self)
        
    def sen(self):
        
        print(f"Welcome to {self.name}, can be contacted at {self.email}")
        


roger = Regi("roger", "Roger")
roger.lis()
roger.sen()


#corre

library2 = []

class Regi:
    def __init__(self, name, email):
        self.name= name
        self.email = email
        
class Lis:
    def lis(self):
        library2.append(self)
        
class Sen:
    def ema(self):
        print(f"Welcome to {self.name}, can be contacted at {self.email}")
        
class ever(Regi, Lis, Sen):
    def __str__(self):
        return f"name: {self.name}, email: {self.email}"
    
    pass

roger = ever("roger", "Roger")
jean = ever("jean", "mark")
roger.lis()
roger.ema()
jean.lis()

print(library2)
for s in library2:
    print(s)


