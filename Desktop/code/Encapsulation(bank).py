#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 15:37:26 2025

@author: paulmaurin
"""

#encapsulation

class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner
        
    def deposit(self, amount):
        print(f"{self.owner}: You are deposing {amount}")
        self.balance += amount
        
    def withdraw(self, amount):
        
        if amount > self.balance:
            print(f"{self.owner}: You don't have anouth on your account, withdraw refused")
            return
        print(f"{self.owner}: You are withdrawing {amount}")
        self.balance -= amount
        
        
    def get_balance(self):
        print(f"{self.owner}: Your balance is {self.balance}")
        
    def transfer(self, amount, other_account):
      if amount > self.balance:
         print(f"{self.owner}: Not enough funds to transfer {amount}")
         return
      self.balance -= amount
      other_account.balance += amount
      print(f"{self.owner} transferred {amount} to {other_account.owner}")
        
        
        


pp1 = BankAccount(5000, "Paul")
pp2 = BankAccount(5000, "Jean")

pp1.deposit(500)
pp1.withdraw(3000)
pp1.transfer(1000, pp2)

pp1.get_balance()
pp2.get_balance()
