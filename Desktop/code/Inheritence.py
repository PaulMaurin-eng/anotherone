#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 15:13:16 2025

@author: paulmaurin
"""

#inheritance


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print("Your vehicle is starting")
        
        
    def stop(self):
        print("Your vehicle is stopping")
        
        
        
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"
        
        
class Car(Vehicle):
    def __init__(self, brand, model, year, doors, fuel_type):
        super().__init__(brand, model, year)
        self.doors = doors
        self.fuel_type = fuel_type
        
    def start(self):
        print(f"The car {self.brand} {self.model} is ready to drive!")
        
class Truck(Vehicle):
    def __init__(self, brand, model, year,capacity_tons, num_wheels):
        super().__init__(brand, model, year)
        self.capacity_tons = capacity_tons
        self.num_wheels = num_wheels
        
    def start(self):
        print(f"The truck {self.brand} {self.model} is hauling goods!")        
        
        
my_car = Car("Tesla", "Model 3", 2022, 4, "electric")
my_truck = Truck("Volvo", "FH16", 2020, 20.0, 18)

print(my_car)   # 2022 Tesla Model 3
print(my_truck) # 2020 Volvo FH16

my_car.start()  # The car Tesla Model 3 is ready to drive!
my_truck.start()# The truck Volvo FH16 is hauling goods!

my_car.stop()   # The vehicle is stopping.