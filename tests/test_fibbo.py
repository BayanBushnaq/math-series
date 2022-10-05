import pytest
from math_series.math_series import fibbo_series

"""
base case 1 
if num == 0 => 0

base case 2
if num == 1 => 1

main case 
if num > 1 => fibbo(num-2)+fibb(num-1)

type error case
if num != int => "plz enter integer number"
"""


def test_basecase1():
    actual = fibbo_series(0)
    expected = 0
    assert actual == expected

def test_basecase2():
    actual = fibbo_series(1)
    expected = 1
    assert actual == expected

def test_maincase():
    actual = fibbo_series(5)
    expected = 5
    assert actual == expected

def test_maincase1():
    actual = fibbo_series(7)
    expected = 13
    assert actual == expected

def test_maincase2():
    actual = fibbo_series(4)
    expected = 3
    assert actual == expected

def test_type_error():
    actual = fibbo_series("bye")
    expected = "plz enter integer number"
    assert actual == expected