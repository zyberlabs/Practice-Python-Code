#!/usr/bin/python

def median(x):
    y = sorted(x)
    i = len(y) / 2
    if len(y) % 2 == 0:
        z = (float(y[i-1]) + float(y[i])) / 2
    else:
        z = y[i]
    return z

print median([5,3,2,7,1,4])
print median([5,3,2,1,4])

