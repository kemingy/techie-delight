# Given an binary array of size two having alteast one element as zero, write a
# single line function to set both its elements to zero. Use of ternary operator
# and direct assignment of elements are not allowed.

def one_line_set_two(array):
    assert len(array) == 2

    array[array[1]] = 0
    return array
