# In this post, we will discuss how to generate fair results from a biased coin
# which prefer one side of the coin over another, and returns TAILS with p 
# probability and HEADS with (1-p) probability where p != (1-p).

from random import random

p = random()

def biased():
    return 0 if random() < p else 1

def generate_fair():
    while True:
        x, y = biased(), biased()
        if x != y:
            return x


if __name__ == '__main__':
    count = [0] * 2
    for _ in range(10000):
        count[generate_fair()] += 1

    print('p: {}\n{}'.format(p, count))
