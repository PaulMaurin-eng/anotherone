#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 13:27:08 2025

@author: paulmaurin
"""

#DIPcomplex

class Abstractmessenger:
    
    def send(self, text):
        pass
    
    
class Messenger(Abstractmessenger):
    
    
    def send(self, text):
        print(f"Sending email: {text}")

    
class Push_notif(Abstractmessenger):
    
        
    def send(self, text):
        print(f"Sending a push: {text}")
        
        
class Sms_notif(Abstractmessenger):
    
    
    def send(self, text):
        print(f"Sending sms: {text}")
        
        
class Envoye():
    def __init__(self, message = Abstractmessenger):
        self.message = message
        
        
    def operation(self, text):
        self.message.send(text)
       
 


envoye = Envoye(Messenger())
num1 = input("what do you want to send?     ")

envoye.operation(num1)


envoye = Envoye(Push_notif())
num1 = input("what do you want to send?     ")

envoye.operation(num1)

envoye = Envoye(Sms_notif())
num1 = input("what do you want to send?     ")

envoye.operation(num1)
        
        
        
n1 = input("How do you want to send it: 0;email , 1;Push  , 2;sms    ")
n2 = input("And the message?    ")

if n1 == "0":
    envoye = Envoye(Messenger())
    envoye.operation(n2)


elif n1 == "1":
    envoye = Envoye(Push_notif())
    envoye.operation(n2)
    
elif n1 == "2":
    envoye = Envoye(Sms_notif())
    envoye.operation(n2)
    
    
    
    
    

    
    
    
    
    
    
    
