from challenges.data_structure.hash_map.hash_map import *
import pytest


def test_add():
    hash_map = Hashmap()
    hash_map.add('Noura','she is sleepy all the day')
    actual = hash_map.__str__()
    expected = 'Noura -> she is sleepy all the day'
    assert  actual == expected

def test_add_duplicate():
    hash_map1 = Hashmap()
    hash_map1.add('Manar','she is studying all the day')
    hash_map1.add('Manar','playing in the garden')
    actual = hash_map1.__str__()
    expected = 'Manar -> playing in the garden'
    assert  actual == expected


def test_get(hash_map_test):
    actual = (hash_map_test.get('Manar'),hash_map_test.get('Sara'))
    expected = ('she is studying all the day' , 'not found')
    assert  actual == expected

def test_contains(hash_map_test):
    actual = (hash_map_test.contains('Manar') , hash_map_test.contains('Sara'))
    expected = (True, False)
    assert  actual == expected


@pytest.fixture
def hash_map_test():
    hash_map = Hashmap()
    hash_map.add('Noura','she is sleepy all the day')
    hash_map.add('Noura','she is solving trees all the day')
    hash_map.add('Tala','she is eating all the day')
    hash_map.add('Manar','she is studying all the day')
    hash_map.add('ranaM','also studying all the day')
    return hash_map


