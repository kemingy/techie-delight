# In this post, we will discuss how to determine if two integers are equal
# without using comparison operators (==, !=, <, >, <=, >=) & arithmetic
# operators (+, -, *, /, %)

def number_equal(x, y):
    return True if x ^ y == 0 else False
