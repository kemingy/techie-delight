# Given two integers, find minimum number between them without using any 
# conditional statement(or ternary operator).

def minimum(x, y):
    return x * (x < y) + y * (x > y)
