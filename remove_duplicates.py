#!/usr/bin/python

def remove_duplicates(x):
    y = len(x)
    z = []
    n = 0
    while n < y:
        if x[n] not in z:
            z.append(x[n])
            n += 1
        else:
            n += 1
    return z

print remove_duplicates([1,1,2,2,3,4,5,5])

