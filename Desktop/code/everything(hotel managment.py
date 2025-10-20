#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 12:54:30 2025

@author: paulmaurin
"""

from abc import ABC, abstractmethod

index = []


class Room(ABC):
    def __init__(self, room_number, price_per_night, is_available = True):
        self.room_number = room_number
        self.price_per_night = price_per_night
        self._is_available = is_available
        
    def is_available(self):
        return self._is_available
    
    
    def book_room(self):
        if not self.is_available:
            print(f"Room {self.room_number} is already booked.")
            return False
        self._is_available = False
        return True
    
    def free_room(self):
        self._is_available = True
    
    
    @abstractmethod 
    def calculate_price(self,nights):
        return
        
    
    
class Payment(ABC):
    
    @abstractmethod 
    def pay(self, amount):
        return
    
        
    
    
    
class Single(Room):
   
    
    def calculate_price(self,nights):
        return self.price_per_night * nights
        
       
    
class Double(Room):
      
      
      def calculate_price(self,nights):
          return (self.price_per_night*1.2) * nights
          
      
      
class Suite(Room):
    
    def calculate_price(self,nights):
        return ( self.price_per_night*1.5 )* nights
        
    
    
class CashPayment(Payment):
    def pay(self,amount):
        print(f"You pay {amount} with cash")
    
    
    
class CreditCardPayment(Payment):
    
    def __init__(self, card_number):
        self.card_number = card_number
    
    def pay(self,amount):
        print(f"You pay {amount} with a credit card: {self.card_number}")
    
    
    
class PaypalPayment(Payment):
    
    
    def __init__(self, email):
        self.email = email
    
    def pay(self,amount):
        print(f"You pay {amount} using paypal with email: {self.email}")
    
    
    
    
class guest:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
        
    def registration(self):
        index.append({"Name": self.name, "Email": self.email})
    
    
class reservation:
    def __init__(self, guest, room, night, payment_method):
        self.guest = guest
        self.room = room
        self.night = night
        self.payment_method = payment_method
        
        
    def confirm_booking(self):
        if self.room.book_room():
            total = self.room.calculate_price(self.night)
            print(f"Your reservation of room {self.room.room_number} is confirmed under the name {self.guest.name}")
            print(f"Your total is {total}")
            self.payment_method.pay(total)
             
        else:
            print("Reservation failed. Room not available.")
            
    
    
guest1 = guest("Paul", "paul@email.com")
guest2 = guest("Jean", "jean@email.com")

# Create rooms
room101 = Single(101, 100)
room102 = Double(102, 150)
room201 = Suite(201, 300)

# Create reservations
res1 = reservation(guest1, room101, 3, CreditCardPayment("1234567812345678"))
res2 = reservation(guest2, room201, 2, PaypalPayment("jean@paypal.com"))

# Confirm reservations
res1.confirm_booking()
res2.confirm_booking()
    
   

    
    
    
    
    
    
    
    
    
    
    
    
    