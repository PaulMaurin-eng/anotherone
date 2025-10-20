#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 12:57:11 2025

@author: paulmaurin
"""




class Book_Initiation:
    def __init__(self):
        self.book = []
        self.user = []
        
        
        
  
class Book_registration:
    def regi_book(self, title, author, copies):
        self.book.append({"Title" :title, "Author" : author, "Copies" : copies} )
 
    
class User_registration:
    def regi_user(self, name, id_num, email):
        self.user.append({"Name" : name, "id_num" : id_num, "email" : email} )      
        
        
class Table_print:
    print("Available books:")
    print("--------------------------------------------------------------------------------")
    def table(self):
        for i in self.book:
             
             print(f"Title: {i['Title']} | Author: {i['Author']}  | Copies avai: {i['Copies']}")
             print("--------------------------------------------------------------------------------")
         
       
class verification_book:   
    
    def che(self, title):
        return any(i['Title']== title for i in self.book)
    
    def process(self, title):
        
        if self.che(title):
            print("We have your book")
            
        else:
            print("Not found")
            
            
class verif_user:
    def check(self, id_num):
        return any(i['id_num'] == id_num for i in self.user)
    def conf(self, id_num):
        if self.check(id_num):
            print("user found")
        
        
class everyth(Book_Initiation, Book_registration, User_registration, Table_print, verification_book, verif_user):
    pass
        
num1 = everyth()
num1.regi_book("la nuit du mal", "xavier", 3)
num1.regi_user("Jean", "234", "Jean@email.com")
num1.regi_book("La vie", "Mark", 1)

num1.table()
num1.process("La vie")
num1.conf("234")




