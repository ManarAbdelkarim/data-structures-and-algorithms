from challenges.data_structure.stacks_and_queues.stacks_and_queues import *
import pytest
import unittest


''' Stack tests for '''

def test_push(stack_test):
    excpected = "three\ntwo\none"
    actual = f"{stack_test}"
    assert excpected == actual

def test_push_to_empty():
    stack = Stack()
    stack.push("one")
    excpected = "one"
    actual = f"{stack}"
    assert excpected == actual

def test_peek(stack_test):
    stack = stack_test
    excpected = "three"
    actual = f"{stack.peek()}"
    assert excpected == actual

def test_empty_stack():
    stack = Stack()
    excpected = True
    actual =  stack.is_empty()
    assert excpected == actual

def test_empty_stack_peek():
    stack = Stack()
    with  pytest.raises(EmptyStackException):
        stack.peek()

def test_empty_queue_pop():
    stack = Stack()
    with  pytest.raises(EmptyStackException):
        stack.pop()

def test_pop(stack_test):
    stack_test.pop()
    excpected = "two\none"
    actual = f"{stack_test}"
    assert excpected == actual

def test_emptying_stack(stack_test):
    for i in range(3):
        stack_test.pop()
    excpected = True
    actual =  stack_test.is_empty()
    assert excpected == actual

def test_adding_multiple_to_stack():
    stack = Stack()
    for i in range(1,4):
        stack.push(i)
    excpected = "3\n2\n1"
    actual = f"{stack}"
    assert excpected == actual

    


''' queue tests '''

def test_enqueue(queue_test):
    excpected = "one\ntwo\nthree"
    actual = f"{queue_test}"
    assert excpected == actual

def test_enqueue_to_empty():
    queue = Queue()
    queue.enqueue("one")
    excpected = "one"
    actual = f"{queue}"
    assert excpected == actual

def test_peek(queue_test):
    excpected = "one"
    actual = f"{queue_test.peek()}"
    assert excpected == actual

def test_empty_queue():
    queue = Queue()
    excpected = True
    actual =  queue.is_empty()
    assert excpected == actual

def test_empty_queue_peek():
    queue = Queue()
    with  pytest.raises(EmptyStackException):
        queue.peek()

def test_empty_queue_dequeue():
    queue = Queue()
    with  pytest.raises(EmptyStackException):
        queue.dequeue()

def test_dequeue(queue_test):
    queue_test.dequeue()
    excpected = "two\nthree"
    actual = f"{queue_test}"
    assert excpected == actual

def test_emptying_queue(queue_test):
    for i in range(3):
        queue_test.dequeue()
    excpected = True
    actual =  queue_test.is_empty()
    assert excpected == actual

def test_adding_multiple_to_queue():
    queue = Queue()
    for i in range(1,4):
        queue.enqueue(i)
    excpected = "1\n2\n3"
    actual = f"{queue}"
    assert excpected == actual

@pytest.fixture
def stack_test():
  stack = Stack()
  stack.push('one')
  stack.push("two")
  stack.push("three")
  return stack


@pytest.fixture
def queue_test():
  queue = Queue()
  queue.enqueue("one")
  queue.enqueue("two")
  queue.enqueue("three")
  return queue
