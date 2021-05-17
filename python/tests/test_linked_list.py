import pytest
from challenges.data_structure.linked_list.linked_list import *


def test_insert(list_test):
    excpected = "{10} -> {Manar} -> {Reem} ->  NULL"
    actual = f"{list_test}"
    assert excpected == actual

def test_includes(list_test):
    actual = [list_test.includes(55),list_test.includes("Manar"),list_test.includes(5)]
    excpected = [False, True , False]
    assert excpected == actual
    
    
def test_insertAfter(list_test):
    actual = list_test.insertAfter("Manar", "Roya")
    excpected = f' "Roya" added secssfuly...'
    assert excpected == actual

def test_insertAfterNone(list_test):
    actual = list_test.insertAfter("M", "Roya")
    excpected = "this node is not exist!"
    assert excpected == actual
    

@pytest.fixture
def list_test():
    linked = Linked_list()
    linked.insert("Reem")
    linked.insert("Manar")
    linked.insert(10)
    return linked
