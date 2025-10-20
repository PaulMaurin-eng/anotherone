#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:33:36 2025

@author: paulmaurin
"""

"""
Count word occurrences
Description: Write a program that takes a text and returns a dictionary 
with the number of times each word appears. Ignore uppercase/lowercase.


"""

str1 = ("""Wings of the Hour, The morning bends with quiet grace, 
           a silver thread across the sky;
           time unfolds in a gentle place,
           where dreams still linger, soft and shy.
           The river hums its patient song,
           carving paths the stones once kept;
           even shadows do not stay long,
           they drift where the daylight wept.
           And in this fleeting, fragile span,
           we build our worlds, we make them true;
           each step a map, each breath a plan,
           each choice a wing that carries you. """)




class Everything:
    
    library = {}
    
    def __init__(self, text):
       self.text = text
       self.wordlist = []
     
     
     
    def convert(self):
        lower_text = self.text.lower()
        conv_text = lower_text.replace("," ,"").replace(".","").replace(";","").replace(":","")
        self.wordlist = conv_text.split()
        print(self.wordlist)
        print("---------------------------------------------------------------")
      
       
    
    def occurence(self):
       
        
        word = []
        occure = []
        i = 0
        
        while i != len(self.wordlist):
            if self.wordlist[i] not in word:
                word.append(self.wordlist[i])
                occure.append(self.wordlist.count(self.wordlist[i]))
                
            i += 1 
            
        print(len(self.wordlist))
        print(len(word))
        print(len(occure))
        
        library = dict(zip(word ,occure))
        print(library)
     

        
num1 = Everything(str1)

num1.convert()

num1.occurence()



                
            
    


