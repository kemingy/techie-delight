import math

from src import (
    clock_angle,
    add_func,
    pow_func,
    swap,
    condition_print,

)

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
