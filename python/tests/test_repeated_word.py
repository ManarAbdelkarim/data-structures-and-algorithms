from challenges.repeated_word.repeated_word import *
import pytest

def test_first_repeated():
    hashmap = HashMap()
    string = "Once upon a time, there was a brave princess who..."
    actual = hashmap.first_repeated(string)
    expected = 'a'
    assert actual == expected


def test_first_repeated_empty():
    hashmap = HashMap()
    string = ""
    with pytest.raises(Exception):
        hashmap.first_repeated(string)

def test_first_repeated_no_repeat():
    hashmap = HashMap()
    string = "My name is Manar"
    actual = hashmap.first_repeated(string)
    expected = 'No repeated words'
    assert actual == expected

