#!/usr/bin/python

def is_even(x):
    return x % 2 == 0

def purify(x):
    y = 0
    z = []
    while y < len(x):
        print
        print "Current x:",x
        print "index:",y
        print "X @ index:",x[y]
#        if is_even(x[y]):
        if x[y] % 2 == 0:
            z.append(x[y])
            y = y + 1
        else:
            y = y + 1
    return z

print purify([4,5,5,4])


