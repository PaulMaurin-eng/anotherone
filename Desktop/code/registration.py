#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 13:14:40 2025

@author: paulmaurin
"""
index = []
#incorecto
class user():
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
   
        
        
        
    def register(self):
        index.append(self)
        
        
    def sendemail(self):
        print(f"welcome to {self.name} you can contact them at {self.email}")
    


c = user("jean", "makert@jb")
c.register()
c.sendemail()

d = user("luis", "eoinvbei&oebv")
d.register()
d.sendemail()

e = user("mark", "ehcbbecbrep")
e.register()
e.sendemail()

#correct
index2 =[]
class user2:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
class regi:
    def register2(self):
        index2.append(self)
        
class emai:
    def send(self):
        print(f"welcome to {self.name} you can contact them at {self.email}")
        
        
class full(user2,regi,emai):
    pass
        
    
        
c2 = full("jean", "makert@jb")
c2.register2()
c2.send()

d2 = full("luis", "eoinvbei&oebv")
d2.register2()
d2.send()

e2 = full("mark", "ehcbbecbrep")
e2.register2()
e2.send()

    
    