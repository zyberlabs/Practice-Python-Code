#!/usr/bin/python

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(scores):
   total = 0
   for score in scores:
       total = total + score
   return total 

def grades_average(grades):
   sum = grades_sum(grades)
   average = sum / float(len(grades))
   return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance = variance + ((average - score) ** 2)
    total = variance / len(scores)
    return total

def grades_std_deviation(variance):
    return variance ** 0.5
    
print "Grades:"
print_grades(grades)
print "Sum of grades:",grades_sum(grades)
print "Grade Average:",grades_average(grades)
print "Grade Variance:",grades_variance(grades)
variance = grades_variance(grades)
print "Standard Deviation:",grades_std_deviation(variance)
