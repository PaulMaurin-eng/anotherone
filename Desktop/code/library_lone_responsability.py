#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 15:46:49 2025

@author: paulmaurin
"""

#using lone responsability


class library:
    def __init__(self):
        self.book = []
        self.user = []
        self.dispon = []
        
   
class registration:    
    
    def register(self, title, author, numa):
        self.book.append({"Title" :title , "Author" : author, "Num available": numa})
   
        
class user_add:   
    
    def add_user(self, name, nid, email):
        self.user.append({"user name": name, "Id num":nid , "Email": email})
       
class give_access:        
       
    def access(self, user_id, book_title):
        
        
        user = next((u for u in self.user if u["Id num"] == user_id), None)
        if user is None:
            print(f"User with id {user_id} not found.")
            return False

        # find book
        book = next((b for b in self.book if b["Title"] == book_title), None)
        if book is None:
            print(f"Book '{book_title}' not found.")
            return False

        # availability
        if book["Num available"] <= 0:
            print("unavailable")
            return False

                 
        book["Num available"] -= 1
        self.dispon.append({"User id": user_id, "Book title": book_title})
        print(f"here is your book {user['user name']}: {book['Title']}, {book['Author']}")
        return True
            
class everything(library, registration, user_add, give_access):
     pass
      



lib1 = everything()
lib1.register("La vie de gh","mark",8)
lib1.add_user("Jean",3748,"3ifb3i7239")
lib1.access(3748,"La vie de gh")