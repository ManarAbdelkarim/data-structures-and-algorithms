import pytest
from challenges.quick_sort.quick_sort import *


def test_insert():
    actual =quick_sort([3,2,4,1], 0, len([3,2,4,1]) - 1)
    excpected = [1,2,3,4]
    assert excpected == actual


def test_insert2():
    actual = quick_sort([], 0, len([]) - 1)
    excpected = []
    assert excpected == actual


def test_insert3():
    actual = quick_sort([4], 0, len([4]) - 1)
    excpected = [4]
    assert excpected == actual


def test_insert4():
    actual = quick_sort([6,-7,3,-2,5], 0, len([6,-7,3,-2,5]) - 1)
    excpected = [-7, -2, 3, 5, 6]
    assert excpected == actual


