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
    

def test_kthFromEnd(list_test):

    actual = [list_test.kthFromEnd(4),list_test.kthFromEnd(-1),list_test.kthFromEnd(3),list_test.kthFromEnd(0),list_test.kthFromEnd(1)]
    expected = ['4 is not in the range of the list' , '-1 is not in the range of the list','3 is not in the range of the list' ,'Reem','Manar']
    assert actual == expected
    


def test_zipList(list_test1,list_test2):
    actual = Linked_list.zipLists(list_test1,list_test2)
    excpected = "{1} -> {5} -> {3} -> {9} -> {2} -> {4} ->  NULL"
    assert excpected == actual

def test_zipList_unbalance1(list_test1,list_test2):
    list_test1.append(4)
    actual = Linked_list.zipLists(list_test1,list_test2)
    excpected = "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> {4} ->  NULL"
    assert excpected == actual

def test_zipList_unbalance2(list_test1,list_test2):
    list_test2.append(4)
    actual = Linked_list.zipLists(list_test1,list_test2)
    excpected = "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> {4} ->  NULL"
    assert excpected == actual

def test_zipList_None(list_test1):
    list_test2 = Linked_list()
    actual = Linked_list.zipLists(list_test1,list_test2)
    excpected = "{1} -> {3} -> {2} ->  NULL"
    assert excpected == actual


@pytest.fixture
def list_test():
    linked = Linked_list()
    linked.insert("Reem")
    linked.insert("Manar")
    linked.insert(10)
    return linked

@pytest.fixture
def list_test1():
    linked1 = Linked_list()
    linked1.append(1)
    linked1.append(3)
    linked1.append(2)
    return linked1

@pytest.fixture
def list_test2():
    linked2 = Linked_list()
    linked2.append("5")
    linked2.append("9")
    linked2.append(4)
    return linked2