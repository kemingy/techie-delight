# Given a number, find out if it is even or odd without using any conditional
# statement (if-else) or ternary operator.

def is_even(n):
    return n & 1 == 0

def print_even_or_odd(n):
    word = ['even', 'odd']
    print(word[n & 1])

if __name__ == '__main__':
    print_even_or_odd(4)
    print_even_or_odd(1)
