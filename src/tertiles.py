# Write an algorithm to generate 0, 1, and 2 with equal probability using a 
# specified function which either produces 0 or 1 with 50% probability each.

from random import randint

def generate_tertiles():
    x = randint(0, 1)
    y = randint(0, 1)
    return generate_tertiles() if x == 0 and y == 1 else x + y


if __name__ == '__main__':
    count = [0] * 3
    for _ in range(3000):
        count[generate_tertiles() - 1] += 1

    print(count)
