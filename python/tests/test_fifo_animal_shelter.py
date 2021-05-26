from challenges.fifo_animal_shelter.fifo_animal_shelter import *
import pytest

# test 1: Can successfully enqueue into a queue
def test_queue_enqueue():
    expected = "5"
    queue = Queue()
    queue.enqueue(5)
    actual = f"{queue}"
    assert actual == expected
# test 2: Can successfully enqueue multiple values into a queue
def test_queue_multiple_enqueue(queue_test):
    expected = "4 3 2 1"
    actual = f"{queue_test}"
    assert actual == expected
# test 3: Can successfully dequeue out of a queue the expected value
def test_queue_dequeue(queue_test):
    expected = 4
    actual = queue_test.dequeue()
    assert actual == expected
# test 4 : Can successfully peek into a queue, seeing the expected value
def test_queue_peek_front(queue_test):
    expected = 4
    actual = queue_test.peek()
    assert actual == expected
# test 5: Can successfully empty a queue after multiple dequeues
def test_queue_multiple_dequeue(queue_test):
    for num in range(4):
        queue_test.dequeue()
    with pytest.raises(EmptyQueueException):
        queue_test.dequeue()

# test 6 :Calling dequeue or peek on empty queue raises exception
def test_peek_empty_queue():
    queue = Queue()
    with pytest.raises(EmptyQueueException):
        queue.peek()
    with pytest.raises(EmptyQueueException):
        queue.dequeue()


@pytest.fixture
def queue_test():
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue(1)
    return queue
