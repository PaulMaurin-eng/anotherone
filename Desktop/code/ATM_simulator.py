#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 16:25:21 2025

@author: paulmaurin
"""

"""
ATM simulator (simplified)
Description: Create a program that simulates an ATM. 
It should allow checking the balance, depositing, 
and withdrawing money until the user decides to exit.

"""


accounts = {
             1 : 30,
             2 : 4000,
             3 : 2000000,
             4 : 2974,
             5 : 28302}

index = []


class Balance_check:
    
    def __init__(self, card):
        self.card = card
        
    def check(self):
        self.available = accounts[self.card]
        print(f"Your account number: {self.card} , you have {self.available} $ on it.")
        index.append(f"Account: {self.card}, has {self.available}$")
    
    
    
    
class deposing:
    def __init__(self, card, incre):
        self.card = card
        self.incre = incre
    
    def add(self, card, incre):
        accounts[card] += incre
        print(f"You added {incre} $ to your account")
        index.append(f"Account: {self.card}, deposed {incre}$")
    
    
class withdraw:
    def __init__(self, card, desc):
        self.card = card
        self.desc = desc
        
    def take(self, card, desc):
        
        if desc > accounts[card]:
            print("No enouth on the account")
        else:
            accounts[card] -= desc
            print(f"You took {desc} $ from your account")
            index.append(f"Account: {self.card}, withdrew {desc}$")
            
class transaction:
    def __init__(self):
        pass
        
    def register(self):
        print(index)
        
    
    
    
    

num = input ("What is your account number?    ")
print("---------------------------------")
num_int = int(num)
i = False
while i != True:
    
   
    x = input("""What would you like to do? 
               options are: 
                   - Balance_check
                   - deposing
                   - withdraw
                   - transaction
                   - exit
                                     """)
    
    
    if x == "Balance_check":
        resp = Balance_check(num_int)
        resp.check()
        print("---------------------------------")
        
        
    if x == "deposing":
        amount = input("How much are you deposing?  ")
        amount_int = int(amount)
        resp = deposing(num_int, amount_int)
        resp.add(num_int, amount_int)
        print("---------------------------------")
        
    if x == "withdraw":
        amount = input("How much are you withdrawing?  ")
        amount_int = int(amount)
        resp = withdraw(num_int, amount_int)
        resp.take(num_int, amount_int)
        print("---------------------------------")
        
        
    if x == "transaction":
        resp = transaction()
        resp.register()
        
    if x == "exit":
        i = True
    
        
        
    
        


