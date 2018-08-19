# Given an integer, find its square without using multiplication and division
# operator. Also, use of power function from any programming language library
# is not allowed.

def square(n):
    n = abs(n)
    addup = sum(range(n))
    return n + addup + addup

