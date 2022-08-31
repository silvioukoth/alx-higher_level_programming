#!/usr/bin/pthon3
#This function that prints a dictionary by ordered keys.

def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(y, a_dictionary[y])) for y in sorted(a_dictionary)]
