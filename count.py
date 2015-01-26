#!/usr/bin/python

def count(sequence, item):
    x = 0
    for each in sequence:
        if each == item:
            x += 1
    return x

print count([1,2,1,1], 1)
    

