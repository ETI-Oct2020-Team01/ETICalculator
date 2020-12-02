import pytest
from mycalculator.my_calculator_functions import *


def test_add():
    value = add(1,4)
    assert value == 5

def test_add_more_than_10():
    value = add(1,0,0,0,0,0,0,0,0,0,0,0)
    assert value == "Input more than 10"