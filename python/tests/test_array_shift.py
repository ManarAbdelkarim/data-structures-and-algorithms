from challenges.array_shift.array_shift import *

def test_array1():
    actual =[[],1]
    
    expect= None
    assert array_shift(actual[0],actual[1]) == expect

def test_array2():
    actual = [3,2]
    
    expect= None
    assert array_shift(actual[0],actual[1]) == expect

def test_array3():
    actual = [[1,2],'hello']
    
    expect= None
    assert array_shift(actual[0],actual[1]) == expect

def test_array4():
    actual =[[2,4,6,8],5]
    expect= [2,4,5,6,8]
    assert array_shift(actual[0],actual[1]) == expect