# Write an algorithm to generate 0 and 1 with 75% and 25% probability 
# respectively using a specified function which produces either 0 or 1 each with
# 50% probability

from random import randint

def generate_quartile():
    return randint(0, 1) & randint(0, 1)


if __name__ == '__main__':
    n = 1000
    zero, one = 0, 0
    for _ in range(n):
        if generate_quartile() == 0:
            zero += 1
        else:
            one += 1

    print('N: {}\nZero: {}\nOne: {}'.format(n, zero, one))
