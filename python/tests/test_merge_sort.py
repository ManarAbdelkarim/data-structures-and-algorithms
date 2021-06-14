import pytest
from challenges.merge_sort.merge_sort import *


def test_insert():
    actual =merge_sort([3,2,4,1])
    excpected = [1,2,3,4]
    assert excpected == actual


def test_insert2():
    actual = merge_sort([])
    excpected = []
    assert excpected == actual


def test_insert3():
    actual = merge_sort([4])
    excpected = [4]
    assert excpected == actual


def test_insert4():
    actual = merge_sort([6,-7,3,-2,5])
    excpected = [-7, -2, 3, 5, 6]
    assert excpected == actual


