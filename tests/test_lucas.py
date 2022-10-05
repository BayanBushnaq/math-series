import pytest

from math_series.math_series import lucas_series


"""
base case (1)
if num == 0 =>2

base case (2) 
if num == 1 => 1

main case 
if num > 1 => lucas(num-2)+lucas(n-1)

type error case 
if num != int => plz enter integer number
"""

def test_base_case1():
    actual  = lucas_series(0)
    expected = 2
    assert actual == expected

def test_base_case2():
    actual  = lucas_series(1)
    expected = 1
    assert actual == expected

def test_type_error():
    actual = lucas_series("string")
    expected = "plz enter integer number"
    assert actual == expected

def test_main_case():
    actual = lucas_series(3)
    expected = 4
    assert actual == expected

def test_main_case1():
    actual = lucas_series(7)
    expected = 29
    assert actual == expected