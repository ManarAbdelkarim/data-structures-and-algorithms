from challenges.repeated_word.repeated_word import first_repeated
import pytest

def test_first_repeated():
    string = "Once upon a time, there was a brave princess who..."
    actual = first_repeated(string)
    expected = 'a'
    assert actual == expected


def test_first_repeated_empty():
    string = ""
    with pytest.raises(Exception):
        first_repeated(string)

def test_first_repeated_no_repeat():
    string = "My name is Manar"
    actual = first_repeated(string)
    expected = 'No repeated words'
    assert actual == expected

