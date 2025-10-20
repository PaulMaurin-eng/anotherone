#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 12:17:26 2025

@author: paulmaurin
"""

#inheritence - library systems


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def display_info(self):
        print(f"You are reading {self.title} from {self.author} made in {self.year}")
        
        
        
class Ebook(Book):
    def __init__(self, title, author, year, file_size):
        
        super().__init__(title, author, year)
        self.file_size = file_size
        
    def display_info(self):
        print(f"You are reading {self.title} from {self.author} made in {self.year} and it's {self.file_size} MB")
        
    
    
    
class Printedbook(Book):
    
    def __init__(self, title, author, year, num_pages):
        
        super().__init__(title, author, year)
        self.num_pages = num_pages
        
    def display_info(self):
        print(f"You are reading {self.title} from {self.author} made in {self.year}. It has {self.num_pages} pages")
        
        
        

book1 = Book("la nuit", "Jean", "2002")
book1.display_info()

book2 = Ebook("Le soir", "Mark", 2004,200)
book2.display_info()

book3 = Printedbook("le matin", "Sam", 2008, 600)
book3.display_info()

library = [book1, book2, book3]
for b in library:
    b.display_info()