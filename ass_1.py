# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:29:31 2023

@author: Dell
"""
"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal 
substring consisting of non-space characters only.
"""

def len_of_last_word(s):
    word=s.split()
    if not word:
        return 0
    return len(word[-1])

inp_str= len_of_last_word(input("enter: "))
print("length of last word is",inp_str)