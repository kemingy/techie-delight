# Given two numbers, add them without using addition operator.

def add_func(x, y):
    if not y:
        return x

    sum = x ^ y
    carry = (x & y) << 1

    return add_func(sum, carry)
