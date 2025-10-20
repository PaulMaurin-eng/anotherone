#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 12:34:52 2025

@author: paulmaurin
"""

#Marketplace


from abc import ABC , abstractmethod


class product(ABC):
    def __init__(self, i_d, name, base_price):
        self.i_d = i_d
        self.name = name
        self.base_price = base_price
        
    
    def final_price(self, add_up):
        endprice = base_price + add_up
        
    
    
class pricing_strat(ABC):
    
    def __init__(self, base_price, add-up):
        super().__init__(base_price, add_up)
    
    def compute(self, base_price, add-up):
        
       
    
    
    def nodiscount(self):
        return add_up
    
    def pourcentdiscount(self):
        return base_price * 0.9
    
    def tier_discount(self):
        if cart_subtotal > 200:
            return base_price * 0.85
    
    
    
    
    
    
class Physical_product:
    def __init__(self, weight, stock, price):
        self.weight = weight
        self._stock = stock
        self.price = price
    
    def reduce_stock(i-d, qty):
        stock -= qty
        print(f"You have {stock} available")
        
    def increase_stock(self):
        stock += qty
        print(f"You bought {qty} more")
    
    
    
    
class Digital_product:
    
    def __init__(self, size, licenses, price):
        self.size = size
        self.licenses = licenses
        self.price = price
    
    
    
class Payment(ABC):
    
    def __init__(self,)
    
    
    def card(last4):
        print(f"You have paid with card number ending {last4}")
    
    def paypal(email):
        print(f"You have paid with this email: {email}")
    
    
class tax_calc:
    
    def __init__(self, tax):
        self.tax = tax
    
    def tax(self):
        tax = 0.25 * subtotal
    
    
    
    
    
class Shiping:
    
    
    def drone(self):
        shipping_price = 2
        
    def post(self):
        shipping_price = 8
        
    def express(self):
        shipping_price = 12
    
    
    
    
    
class cart:
    
    def __init__(self):
        
        
        
    def add(self, i_d):
        print(f"You have selected item num {i-d} which is a {self.product.name")
        print(f"It costs {self.product.price")
        Physical_product.reduce_stock(1)
        
    def remove(self, i_d):
        print(f"You have selected item num {i-d} which is a {self.product.name")
        print(f"It costs {self.product.price")
        Physical_product.increase_stock()
        
        
        
    def set_ship(self, shipping):
        
        
        
        
        
    def subtotal(self):
        
        
        
    def tax(self):
        
        
    def shipping_cost(self):
        
        
        
    def total(self):
        total = subtotal + tax + shipping_cost
        
    
    
    
    
 
    
    
class inventory:
    
    
    
class refunds