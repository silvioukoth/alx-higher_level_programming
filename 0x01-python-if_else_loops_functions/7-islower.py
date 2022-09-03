#!/usr/bin/python3
islower = __import__('7-islower').islower

def islower(c):
    print("'!' => {}".format("lower" if islower("!") else "upper"))
