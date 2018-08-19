# Given a large number N, find all positive numbers less than N that can be
# represented as sum of two cubes for at-least two different pairs.

def get_cube(n):
    root = int(n ** (1 / 3))
    ans = set()

    for i in range(root):
        for j in range(i + 1, root):
            cube_sum = i ** 3 + j ** 3
            if cube_sum in ans:
                yield cube_sum
            else:
                ans.add(cube_sum)
