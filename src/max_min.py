# Given three integers, find maximum and minimum number between them without
# using conditional statements or ternary operator.

def maximum(a, b):
    lookup = [a, b]
    return lookup[a < b]

def minimum(a, b):
    lookup = [a, b]
    return lookup[a > b]

def max_min_number(a, b, c):
    return maximum(a, maximum(b, c)), minimum(a, minimum(b, c))
