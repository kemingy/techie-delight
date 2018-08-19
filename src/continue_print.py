# Write a program to print all numbers between 1 to N without using loop.

def print_below_n(n):
    if n < 1:
        return

    print_below_n(n - 1)
    print(n)

if __name__ == '__main__':
    print_below_n(10)
