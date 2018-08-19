# Write a program to perform division of two numbers without using division
# operator ('/')

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError('y = 0')

    sign = 1 if x * y > 0 else -1
    x, y = abs(x), abs(y)
    mask, quotient = 1, 0

    while y <= x:
        y <<= 1
        mask <<= 1

    while mask > 1:
        y >>= 1
        mask >>= 1
        if x >= y:
            x -= y
            quotient |= mask

    return sign * quotient
