import pytest
from mycalculator.my_calculator_functions import *


def test_multiply():
    value = multiply(1,1,1,1,1,1,1,1,1,1,1)
    assert value == "Error >10 values given!"

def test_multiply_positive_positive():
    value = multiply(1,2,3)
    assert value == 6

def test_multiply_positive_negative():
    value = multiply(1,-2)
    assert value == -2

def test_multiply_negative_negative():
    value = multiply(-1,-1)
    assert value == 1
