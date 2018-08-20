# Write an algorithm to get 0 and 1 with equal probability using a function
# which generates random numbers from 1 to 5 with equal probability.

from random import randint

def quantile():
    ans = 5
    while ans == 5:
        ans = randint(1, 5)

    return ans & 1 == 1


if __name__ == '__main__':
    count = [0] * 2
    for _ in range(10000):
        count[quantile() - 1] += 1

    print(count)
