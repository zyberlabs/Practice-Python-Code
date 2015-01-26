#!/usr/bin/python

my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

print "writing out to a file"
my_file = open("output.txt", "w")

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()

print "readling in from a file:"
r_file = open("mystuff.py", "r")

print r_file.read()

r_file.close

print "readling in from a file:"
my_file = open("output.txt", "r")

print my_file.readline()
print my_file.readline()
print my_file.readline()

my_file.close()

with open("text.txt", "w") as textfile:
    textfile.write("Success!")

