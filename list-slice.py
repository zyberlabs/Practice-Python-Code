#!/usr/bin/python

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]

my_list = range(1, 11) # List of numbers 1 - 10
backwards = my_list[::-1]

print my_list[::2]
print backwards

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]

print backwards_by_tens

to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[8:15]

