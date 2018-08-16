# Given two integers, swap them without using any third variable.

def swap(x, y):
    if x != y:
        x = x ^ y
        y = x ^ y
        x = x ^ y

    return x, y

