#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 13:28:22 2025

@author: paulmaurin
"""
from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str = Field(min_Lenght = 1, max_Lenght = 100)
    author: str 
    isbn: str = Field(default = None)
    price: float 
    in_stock: bool = Field(default = True)
    
    
book={"La nuit du mal", "Jean",234594834 , 34,True}

print(book.title)