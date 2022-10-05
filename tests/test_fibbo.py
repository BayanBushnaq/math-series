import pytest
from math_series.math_series import fibbo_series


def test_fibbo():
    actual = fibbo_series()
    expected = None
    assert actual == expected