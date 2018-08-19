# Write an algorithm to generate random numbers from 1 to 12 with equal 
# probability using a given fucntion which generates random numbers from 1 to 6
# with equal probability.

from random import randint

def generate_twelve_percentile():
    return 2 * randint(1, 6) - (randint(1, 6) & 1)


if __name__ == '__main__':
    count = [0] * 12
    
    for _ in range(12000):
        count[generate_twelve_percentile() - 1] += 1

    print(count)
