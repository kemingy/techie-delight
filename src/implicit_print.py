# Write a program to print all numbers between 1 to N without using semicolon.

def implicit_print(n):
    [print(_) for _ in range(1, n + 1)]


if __name__ == '__main__':
    implicit_print(10)
