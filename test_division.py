import pytest
from mycalculator.my_calculator_functions import *


def test_division():
    value = divide(1,2,3,4,5,6,7,8,9,10,11)
    assert value == "Error >10 values given!"

def test_division_positive_negative():
    value = divide(10,-2)
    assert value == -5

def test_division_negative_negative():
    value = divide(-10,-2)
    assert value == 5

def test_division_negative_positive():
    value = divide(-10, 10)
    assert value == -1

def test_division_by_zero():
    value = divide(10, 0)
    assert value == "Error division by zero!"