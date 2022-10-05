import pytest

from math_series.math_series import fibbo_series, sum_series ,lucas_series

"""
case 1
if 2 optional values ==(0 , 1)=> fibbo()

case 2 
if 2 optional values == (2 , 1) => lucas()

case 3 
if optional values != case 1 and case 2 => sum_series

case 4 
if optional values are not found => fibbo()

case 5
if type (values) != int => plz enter integer number
"""

def test_case1():
    actual = sum_series(3,0,1)
    expected = fibbo_series(3)
    assert actual == expected 

def test_case2():
    actual = sum_series(3,2,1)
    expected = lucas_series(3)
    assert actual == expected 

def test_case3():
    actual = sum_series(3)
    expected = fibbo_series(3)
    assert actual == expected 

def test_case4():
    actual = sum_series(3,2,6)
    expected = 14
    assert actual == expected 

def test_case5():
    actual = sum_series("string")
    expected = "plz enter integer number"
    assert actual == expected 

