# Write an algorithm to generate numbers from 1 to 7 with equal probability
# using a specified function which produces random numbers between 1 to 5 with
# equal probability.

from random import randint

def generate_seven():
    ans = 25
    while ans > 21:
        ans = (randint(1, 5) - 1) * 5 + randint(1, 5)

    return (ans % 7) + 1


if __name__ == '__main__':
    count = [0] * 7
    for _ in range(70000):
        count[generate_seven() - 1] += 1

    print(count)
