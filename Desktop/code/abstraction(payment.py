#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 12:45:54 2025

@author: paulmaurin
"""

#abstraction


from abc import ABC, abstractmethod


class payment(ABC):
    
    
    @abstractmethod
    def pay(self,amount):
        return
        
        
        
        
        
class Creditcardpayment(payment):
    def pay(self,amount):
        print(f"You pay {amount} with a creditcard")
    
    
    
    
class PaypalPayment(payment):
    def pay(self,amount):
        print(f"You pay {amount} with paypal")
    
    
    
class CryptoPayment(payment):
    def pay(self,amount):
        print(f"You pay {amount} with a cyrpto")
    
    
    
num1 = CryptoPayment()
num1.pay(200)