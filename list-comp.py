#!/usr/bin/python

evens = []
for x in range(1,12):
    if (x**2) % 2 == 0:
        evens.append(x)

squares = [x**2 for x in range(1,12) if (x**2) % 2 == 0]
cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 == 0]

print evens
print squares
print cubes_by_four

