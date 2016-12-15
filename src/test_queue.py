"""Test dbl_linked_list data structures."""

import pytest

TEST_ITER = [1, 2, 3, 4, 5]

@pytest.fixture
def create_empty_node():
    """Return an empty Node object."""
    from linked_list import Node
    return Node()


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


def test_create_empty_dbl_node(create_empty_node):
    """Test creation of an empty node."""
    assert create_empty_node.value is None
    assert create_empty_node.nxt is None
    assert create_empty_node.prev is None


def test_create_node_with_val_nxt_prev(): #multiple asserts are bad
    """Test creation of Nodes with values and nxt, prev references."""
    from queue import Node
    node1 = Node(1)
    assert node1.value == 1 and node1.nxt is None and node1.prev is None
    node2 = Node("two", node1)
    assert node2.value == "two" and node2.nxt is node1 and node2.prev is None
    node3 = Node([3], node1, node2)
    assert node3.value == [3] and node3.nxt is node1 and node3.prev is node2

def test_create_empty_Queue(new_q):
    """Test creation of empty Queue."""
    assert new_q.head is None
    assert new_q.tail is None


def test_create_queue_with_one_value():
    """Test that a queue can be created with one value."""
    from queue import Queue
    new_q = Queue(5)
    assert new_q.head.value == 5 and new_q.tail.value == 5
    assert new_q.head.nxt is None
    assert new_q.head.prev is None
    assert new_q.tail.nxt is None
    assert new_q.tail.prev is None

# def test_create_queue_with_one_value_assign_head_tail(new_q): #refactor this / rolled into test_create_queue_with_one_value
#     """Test that a list created with one value has correct prev/next."""
#     assert new_q.head.nxt is None
#     assert dll.head.prev is None
#     assert dll.tail.nxt is None
#     assert dll.tail.prev is None

def test_create_queue_with_iterable(new_q):
    """Given an iterable, test that new Queue is created correctly."""
    from queue import Queue
    assert new_q.head.value == TEST_ITER[-1]
    assert new_q.tail.value == TEST_ITER[0]


def test_create_queue_with_iter_correct_size(new_q):
    """Test that creating a queue with an iterable results in correct length."""
    assert dll._size == len(TEST_ITER)


def test_create_queue_with_iter_correct_prev_nxt(new_q):
    """Creating a queue with an iter head.nxt and tail.prev are correct."""
    dll = create_list_with_iter
    assert dll.head.nxt.value == TEST_ITER[-2]
    assert dll.tail.prev.value == TEST_ITER[1]

#Enqueue SPECIFIC TESTS
def test_enque_empty_list(new_empty_q):
    """Test enqueued val is new tail."""
    new_empty_q.enqueue(5)
    assert dll.head.value == 5 and dll.tail.value == 5

def test_enqueue_empty_queue_new_head_tail(new_empty_q):
    """Test that enquing on an empty queue results in a new head, tail."""
    new_empty_q.enqueue(5)
    assert new_empty_q.head is new_empty_q.tail

def test_first_enqueued_val_nxt_prev_is_none(new_empty_q):
    """Test that the first enqueued Node has no nxt or prev."""
    new_empty_q.enqueue(5)
    assert new_empty_q.head.nxt is None and new_empty_q.head.prev is None

def test_enqueued_assigns_new_head(new_q):
    """Test new tail is assigned."""
    new_q.enqueue(6)
    assert new_q.tail.value == 6

def test_enqueue_reassigns_prev_nxt(new_q):
    """Test that enqueing to a full list correctly assigns prev, nxt."""
    old_head = new_q.head
    new_q.enqueue(6)
    assert dll.tail.prev.value == old_tail.value
    assert dll.tail.prev.nxt is dll.tail

def test_enqueue_increases_size(new_q):
    """Test that enqueing a node is increasing the size by 1"""
    old_size = new_q._size
    new_q.push(6)
    assert new_q._size == old_size + 1

"""DEQUEUE SPECIFIC TESTS"""
def test_dequeue_empty_list_raise_error(new_empty_q):
    """Test that dequeing an empty list raises an Index Error."""
    dll = create_empty_dbl_ll
    with pytest.raises(IndexError):
        dll.dequeue()

def test_dequeue_reassign_head(new_q):
    """Test that dequeueing a non-empty list reassigns head."""
    dll = create_list_with_iter
    old_head = dll.head
    dll.dequeue()
    assert old_head.nxt.value == dll.head.value

def test_dequeue_decrease_size(new_q):
    """Test that dequeue correctly decreases size."""
    dll = create_list_with_iter
    old_size = dll._size
    dll.dequeue()
    assert dll._size == old_size - 1

def test_dequeue_reassign_nxt_prev(new_q):
    """Test that dequeueing a non-empty list reassigns head.nxt and head.nxt.prev."""
    dll = create_list_with_iter
    dll.dequeue()
    assert dll.head.prev is None and dll.head.nxt.prev is dll.head


def test_dequeue_returns_correct_value(new_q):
    """Test that dequeue returns the correct value."""
    dll = create_list_with_iter
    head_value = dll.head.value
    assert dll.dequeue() == head_value
