#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 13:13:56 2025

@author: paulmaurin
"""
import random as ran

class event_registration:
    def __init__(self):
        self.sport = []
        
    def add_event(self, sport):
        self.sport.append(sport)
        
class user_registration:
    
    def __init__(self):
        self.user = []
       
    
    def add_user(self, name, country, ownsport):
        
        self.user.append({"Name": name, "Country":country, "sport":ownsport })
       
        
        
class rand_result:
    
    def __init__(self, event_registration, user_registration):
        self.event_registration = event_registration
        self.user_registration = user_registration
    
    
    
    def result(self):
        
        
        for sport in self.event_registration.sport:
            print(f"For the {sport} category")
            
            users_list = [u["Name"] for u in self.user_registration.user]
            
            
            num1 = ran.choice(users_list)
            print(f"The gold winner in first place is {num1}")
            users_list.remove(num1)
            
            num2 = ran.choice(users_list)
            print(f"The silver winer in second place is {num2}")
            users_list.remove(num2)
            
            num3 = ran.choice(users_list)
            print(f"The bronze winner in third place is {num3}")
        
        
events = event_registration()        
person = user_registration()


person.add_user("Jean", "france", "run")
person.add_user("mark","US", "run")
person.add_user("Kyle", "Mexique", "run")
events.add_event("run")

rng = rand_result(events, person)
rng.result()


       
        
