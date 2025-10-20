#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 14:09:14 2025

@author: paulmaurin
"""

'''

Check palindromes
Description: Make a function that determines whether a word or phrase is a palindrome 
(it reads the same left to right and right to left). Ignore spaces and uppercase/lowercase.

'''

class palindromes:
    def __init__(self, text):
        self.text = text
        
        
        
    def formating(self):
        lower_text = self.text.lower()
        conv_text = lower_text.replace("," ,"").replace(".","").replace(";","").replace(":","")
        return conv_text
        
    def check(self, text):
        pass
        
        
        
class word(palindromes):
    def __init__(self, text):
        super().__init__(text)
        
    def formating(self):
        self.lower_text = self.text.lower()
        
        
    
    def check(self):
        self.formating()
        b = True
        if len(self.lower_text) %2 == 0:
            i = 0
            
            while i != (len(self.lower_text)/2):
                if self.lower_text[i] == self.lower_text[-i-1]:
                    b = True
                    i +=1
                else:
                    b = False
                    break
           
                
        elif len(self.lower_text) %2 != 0:
            i = 0
            while i != ((len(self.lower_text)-1)/2):
                if self.lower_text[i] == self.lower_text[-i-1]:
                    b = True
                    i += 1
                else:
                    b = False
                    break
            
        
        if b == True:
             print("It is a palindrome")
             
        if b == False:
             print("It is noooot a plalindrome")   
    
    
    
    
    
class phrases(palindromes):
    def __init__(self, text):
        super().__init__(text)
        
        
        
    def formating(self):
        self.text = super().formating().split()
        
    
    def check(self):
        self.formating()
        b = True
        if len(self.text) %2 == 0:
            i = 0
            while i != (len(self.text)//2):
                if self.text[i] == self.text[-i-1]:
                    b = True
                    i += 1
                else:
                    b = False
                    break
              
        if len(self.text) %2 != 0:
            i = 0
            while i != ((len(self.text)-1)//2):
                if self.text[i] == self.text[-i-1]:
                    b =  True
                    i += 1
                else:
                    b =  False
                    break
       
        if b == True:
            print("It is a palindrome")
            
        if b == False:
            print("It is noooot a plalindrome")



str1 = "hola"
str2 = "nan"
str3 = "Anna"

str4 = "Maybe it is true"
str5 = "true is true"
str6 = "coding is important, important is coding"


num1 = word(str1)
num1.check()

num2 = word(str2)
num2.check()

num3 = word(str3)
num3.check()

num4 = phrases(str4)
num4.check()

num5 = phrases(str5)
num5.check()

num6 = phrases(str6)
num6.check()


