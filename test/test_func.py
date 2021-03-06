import math

from src import *

def test_clock():
    assert clock_angle('5:30') == 15
    assert clock_angle('9:00') == 90
    assert clock_angle('12:00') == 0

def test_add():
    assert add_func(12, 2) == 14
    assert add_func(0, 23) == 23
    assert add_func(-4, 2) == -2

def test_power():
    assert math.isclose(pow_func(2, 10), 1024)
    assert math.isclose(pow_func(1, 500), 1)
    assert math.isclose(pow_func(10, 2), 100)

def test_swap():
    assert swap(2, 5) == (5, 2)
    assert swap(2, 2) == (2, 2)
    assert swap(0, 4) == (4, 0)
    assert swap(-1, 3) == (3, -1)

def test_condition_print():
    from io import StringIO
    output = StringIO()
    condition_print(output=output)
    assert output.getvalue().strip() == 'Hello World'

def test_max_min():
    assert max_min_number(2, 4, 1) == (4, 1)
    assert max_min_number(0, 0, 0) == (0, 0)
    assert max_min_number(-2, 4, 8) == (8, -2)

def test_cube_sum():
    assert list(get_cube(25000)) == [1729, 4104, 13832, 20683]

def test_multiply():
    assert multiply(2, 5) == 10
    assert multiply(0, 4) == 0
    assert multiply(1, 0) == 0
    assert multiply(1, -3) == -3

def test_even():
    assert is_even(3) == False
    assert is_even(-3) == False
    assert is_even(0) == True

def test_square():
    assert square(3) == 9
    assert square(1) == 1
    assert square(0) == 0
    assert square(-9) == 81

def test_oneline():
    assert one_line_set_two([0, 1]) == [0, 0]
    assert one_line_set_two([1, 0]) == [0, 0]
    assert one_line_set_two([0, 0]) == [0, 0]

def test_minimum():
    assert minimum(2, 5) == 2
    assert minimum(45, -4) == -4
    assert minimum(0, 0) == 0

def test_divide():
    assert divide(1, 34) == 0
    assert divide(0, 2) == 0
    assert divide(32, 5) == 6
    assert divide(-44, 8) == -5

def test_ternary():
    assert ternary(True, 23, -9) == 23
    assert ternary(False, 22, 8) == 8

def test_equal():
    assert number_equal(2, 2) == True
    assert number_equal(0, -2) == False
    assert number_equal(-3, -3) == True

