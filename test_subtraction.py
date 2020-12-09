import pytest
from mycalculator.my_calculator_functions import *


def test_subtract():
    value = subtract(1,2,3)
    assert value == -4

def test_subtract_positive_negative():
    value = subtract(1,-2,3)
    assert value == 0

def test_subtract_negative_negative():
    value = subtract(-1,-2)
    assert value == 1