# Given two integers, multiply them without using multiplication operator or
# conditional loops.

def mul(x, y):
    if x == 0 or y == 0:
        return 0

    if x == 1:
        return y

    if y == 1:
        return x

    return x + multiply(x, y - 1)


def multiply(x, y):
    ans = mul(x, abs(y))
    return ans if y > 0 else -ans
