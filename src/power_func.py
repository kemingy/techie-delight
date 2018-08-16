# Given two positive integers, implement power function without using
# multiplication and division operators.

import math

def quick_pow(e, n):
    if not e:
        return 0

    ans, tmp = 1, e

    while n > 0:
        if n & 1 == 1:
            ans *= tmp

        tmp *= tmp
        n = n >> 1

    return ans

def pow_func(x, y):
    log_x = math.log(x)
    summary = 0

    for i in range(y):
        summary += log_x

    return math.exp(summary)
