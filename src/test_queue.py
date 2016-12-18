"""Test the Queue data structure.

A Queue works based on the FIFO principle which is based in accounting and it
describes the method of the first item/person/inventory to enter something
to also be the first to leave it.

An example would be a line in a bank where the first customer in the line will
be the first one served and thus the first to exit the bank"""

import pytest

TEST_ITER = [1, 2, 3, 4, 5]


@pytest.fixture
def create_empty_node():
    """Return an empty DblNode object."""
    from dbl_linked_list import DblNode
    return DblNode()


@pytest.fixture
def new_q():
    """Given an iterable, create a new queue."""
    from queue import Queue
    this_q = Queue(TEST_ITER)
    return this_q


@pytest.fixture
def new_empty_q():
    """Create an empty object of type Queue to be used in test functions."""
    from queue import Queue
    this_empty_q = Queue()
    return this_empty_q

@pytest.fixture
def new_q_1():
    from queue import Queue
    this_q = Queue(TEST_ITER[-1])
    return this_q


def test_create_empty_dbl_node(create_empty_node):
    """Test creation of an empty node."""
    assert create_empty_node.value is None
    assert create_empty_node.nxt is None
    assert create_empty_node.prev is None


def test_create_node_with_val_nxt_prev():  #is that doing anyting past assert?
    """Test creation of DblNodes with values and nxt, prev references."""
    from dbl_linked_list import DblNode
    node1 = DblNode(1)
    assert node1.value == 1 and node1.nxt is None and node1.prev is None
    node2 = DblNode("two", node1)
    assert node2.value == "two" and node2.nxt is node1 and node2.prev is None
    node3 = DblNode([3], node1, node2)
    assert node3.value == [3] and node3.nxt is node1 and node3.prev is node2


def test_create_empty_Queue(new_empty_q):
    """Test creation of empty Queue."""
    assert new_empty_q._container.head is None
    assert new_empty_q._container.tail is None


def test_create_queue_with_one_value(new_q_1):
    """Test that a queue can be created with one value."""
    assert new_q_1._container.head.value == TEST_ITER[-1] and new_q_1._container.tail.value == TEST_ITER[-1]
    assert new_q_1._container.head.nxt is None
    assert new_q_1._container.head.prev is None
    assert new_q_1._container.tail.nxt is None
    assert new_q_1._container.tail.prev is None


def test_create_queue_with_iterable(new_q):
    """Given an iterable, test that new Queue is created correctly."""
    from queue import Queue
    assert new_q._container.head.value == TEST_ITER[0]
    assert new_q._container.tail.value == TEST_ITER[-1]


def test_create_queue_with_iter_correct_size(new_q):
    """Test that creating a queue with an iterable results in correct length."""
    assert new_q._container._size == len(TEST_ITER)


def test_create_queue_with_iter_correct_prev_nxt(new_q):
    """Creating a queue with an iter head.nxt and tail.prev are correct."""
    assert new_q._container.head.nxt.value == TEST_ITER[1]
    assert new_q._container.tail.prev.value == TEST_ITER[-2]


"""Enqueue SPECIFIC TESTS"""


def test_enque_empty_list(new_empty_q):
    """Test enqueued val is new tail."""
    new_empty_q.enqueue(TEST_ITER[-1])
    assert new_empty_q._container.head.value == TEST_ITER[-1] and new_empty_q._container.tail.value == TEST_ITER[-1]


def test_enqueue_empty_queue_new_head_tail(new_empty_q):
    """Test that enquing on an empty queue results in a new head, tail."""
    new_empty_q.enqueue(TEST_ITER[-1])
    assert new_empty_q._container.head is new_empty_q._container.tail


def test_first_enqueued_val_nxt_prev_is_none(new_empty_q):
    """Test that the first enqueued DblNode has no nxt or prev."""
    new_empty_q.enqueue(TEST_ITER[-1])
    assert new_empty_q._container.head.nxt is None and new_empty_q._container.head.prev is None


def test_enqueued_assigns_new_head(new_q):
    """Test new tail is assigned."""
    new_q.enqueue(6)
    assert new_q._container.tail.value == 6


def test_enqueue_reassigns_prev_nxt(new_q):
    """Test that enqueing to a full list correctly assigns prev, nxt."""
    old_tail = new_q._container.tail
    new_q.enqueue(6)
    assert new_q._container.tail.prev.value == old_tail.value
    assert new_q._container.tail.prev.nxt is new_q._container.tail


def test_enqueue_increases_size(new_q):
    """Test that enqueing a node is increasing the size by 1"""
    old_size = new_q._container._size
    new_q.enqueue(6)
    assert new_q._container._size == old_size + 1


"""DEQUEUE SPECIFIC TESTS"""


def test_dequeue_empty_list_raise_error(new_empty_q):
    """Test that dequeing an empty list raises an Index Error."""
    with pytest.raises(IndexError):
        new_empty_q.dequeue()


def test_dequeue_reassign_head(new_q):
    """Test that dequeueing a non-empty list reassigns head."""
    old_head = new_q._container.head
    new_q.dequeue()
    assert old_head.nxt.value == new_q._container.head.value


def test_dequeue_decrease_size(new_q):
    """Test that dequeue correctly decreases size."""
    old_size = new_q._container._size
    new_q.dequeue()
    assert new_q._container._size == old_size - 1


def test_dequeue_reassign_nxt_prev(new_q):
    """Test that dequeueing a non-empty list reassigns head.nxt and head.nxt.prev."""
    new_q.dequeue()
    assert new_q._container.head.prev is None and new_q._container.head.nxt.prev is new_q._container.head


def test_dequeue_returns_correct_value(new_q):
    """Test that dequeue returns the correct value."""
    head_value = new_q._container.head.value
    assert new_q.dequeue() == head_value


"""Peek specific TESTS """


def test_peek_returns_None_on_empty_queue(new_empty_q):
    """Test that peeking on an empty Queue object returns None"""
    assert new_empty_q.peek() is None


def test_peek_returns_first_in_queue(new_q):
    """Test that peek returns the value of the first node in the Queue object"""
    head_before_peek = new_q._container.head
    assert new_q.peek() == new_q._container.head.value and new_q._container.head == head_before_peek
