#!/usr/bin/python3
#This function deletes keys with a specific value in a dictionary.

def complex_delete(a_dictionary, value):
     while value in a_dictionary.values():
         for n, y in a_dictionary.item():
             if y == value:
                 del a_dictinary[n]
                 break
     return (a_dictionary)
