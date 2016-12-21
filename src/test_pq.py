"""Test dbl_linked_list data structures."""

import pytest
import random

ROUTINES = [
    ("get_up", 1),
    ("make_coffee", 2),
    ("shower", 3),
    ("shave", 4),
    ("get_dressed", 5),
    ("walk_the_dog", 6),
    ("make_breakfast", 7),
    ("read_newspaper", 8),
    ("commute", 9),
]


@pytest.fixture
def pq_empty():
    from priorityq import PriorityQueue
    new_pq = PriorityQueue()
    return new_pq

@pytest.fixture
def pq1():
    from priorityq import PriorityQueue
    new_pq = PriorityQueue(ROUTINES[-1])
    return new_pq

@pytest.fixture
def pq():
    from priorityq import PriorityQueue
    new_pq = PriorityQueue(ROUTINES)
    return new_pq


def test_create_empty_pq(pq_empty):
    """Test creation of empty PriorityQueue."""
    assert pq_empty._heap[0] == 0
    assert len(pq_empty) == 1

def test_create_list_with_one_value(pq1):
    """Test that a PriorityQueue can be created with one value."""
    assert pq1[-1] == ROUTINES[-1]


def test_pop_from_pq_returns_top_prio_item(pq):
    """Test that popping from PriorityQueue returns the item with the highest prio and remove it from the queue."""
    assert ROUTINES[0] == pq.pop()
    assert pq._heap 


def test_create_dbl_with_iterable(dbl_ll):
    """Given an iterable, test that new Dbl_LL is created."""
    assert dbl_ll.head.value == TEST_ITER[-1]
    assert dbl_ll.tail.value == TEST_ITER[0]


def test_create_dbl_with_iter_correct_size(dbl_ll):
    """Test that creating a dbl_ll with an iterable results in correct length."""
    assert dbl_ll._size == TEST_ITER[-1]


def test_create_dbl_with_iter_correct_prev_nxt(dbl_ll):
    """Creating a Dbl_LL with an iter head.nxt and tail.prev are correct."""
    assert dbl_ll.head.nxt.value == TEST_ITER[-2]
    assert dbl_ll.tail.prev.value == TEST_ITER[1]


"""PUSH SPECIFIC TESTS"""


def test_push_empty_list(dbl_ll_empty):
    """Test pushed val is new head and tail."""
    dbl_ll_empty.push(TEST_ITER[-1])
    assert dbl_ll_empty.head.value == TEST_ITER[-1] and dbl_ll_empty.tail.value == TEST_ITER[-1]


def test_push_empty_list_new_head_tail(dbl_ll_empty):
    """Test that pushing on an empty list results in a new head, tail."""
    dbl_ll_empty.push(TEST_ITER[-1])
    assert dbl_ll_empty.head is dbl_ll_empty.tail


def test_first_pushed_val_nxt_prev_is_none(dbl_ll_empty):
    """Test that the first pushed Node has no nxt or prev."""
    dbl_ll_empty.push(TEST_ITER[-1])
    assert dbl_ll_empty.head.nxt is None and dbl_ll_empty.head.prev is None


def test_push_assigns_new_head(dbl_ll):
    """Test new head assigned."""
    dbl_ll.push(6)
    assert dbl_ll.head.value == 6


def test_push_reassigns_prev_nxt(dbl_ll):
    """Test that pushing to a full list correctly assigns prev, nxt."""
    old_head = dbl_ll.head
    dbl_ll.push(6)
    assert dbl_ll.head.nxt.value == old_head.value
    assert dbl_ll.head.nxt.prev is dbl_ll.head


def test_push_increases_size(dbl_ll):
    old_size = dbl_ll._size
    dbl_ll.push(6)
    assert dbl_ll._size == old_size + 1


"""APPEND SPECIFIC TESTS"""


def test_append_empty_list(dbl_ll_empty):
    """Test appended val is new head and tail."""
    dbl_ll_empty.append(TEST_ITER[-1])
    assert dbl_ll_empty.head.value == TEST_ITER[-1] and dbl_ll_empty.tail.value == TEST_ITER[-1]


def test_append_empty_list_new_head_tail(dbl_ll_empty):
    """Test that appending on an empty list results in a new head, tail."""
    dbl_ll_empty.append(TEST_ITER[-1])
    assert dbl_ll_empty.head is dbl_ll_empty.tail


def test_first_appended_val_nxt_prev_is_none(dbl_ll_empty):
    """Test that the first appended Node has no nxt or prev."""
    dbl_ll_empty.append(TEST_ITER[-1])
    assert dbl_ll_empty.tail.nxt is None and dbl_ll_empty.tail.prev is None


def test_append_assigns_new_tail(dbl_ll):
    """Test new tail is assigned."""
    dbl_ll.append(6)
    assert dbl_ll.tail.value == 6


def test_append_reassigns_prev_nxt(dbl_ll):
    """Test that appending to a full list correctly assigns prev, nxt."""
    old_tail = dbl_ll.tail
    dbl_ll.append(6)
    assert dbl_ll.tail.prev.value == old_tail.value
    assert dbl_ll.tail.prev.nxt is dbl_ll.tail


def test_append_increases_size(dbl_ll):
    """Test that append increases size correctly."""
    old_size = dbl_ll._size
    dbl_ll.append(6)
    assert dbl_ll._size == old_size + 1


"""POP SPECIFIC TESTS"""


def test_pop_from_empty_list(dbl_ll_empty):
    """Test pop from empty list to return an IndexError"""
    with pytest.raises(IndexError):
        dbl_ll_empty.pop()


def test_pop_from_list_size_2(dbl_ll_2):
    """Test pop on a list of size 2"""
    old_head = dbl_ll_2.head
    old_size = dbl_ll_2._size
    assert dbl_ll_2.head.value == dbl_ll_2.pop() and old_head.nxt == dbl_ll_2.head and dbl_ll_2._size == old_size - 1


def test_pop_on_list_size_1(dbl_ll_one_value):
    """Test pop on list containing one element, head&tail should be None"""
    dbl_ll_one_value.pop()
    assert dbl_ll_one_value.head is None and dbl_ll_one_value.tail is None


"""SHIFT SPECIFIC TESTS"""


def test_shift_empty_list_raise_error(dbl_ll_empty):
    """Test that shifting an empty list raises an Index Error."""
    with pytest.raises(IndexError):
        dbl_ll_empty.shift()

def test_shift_on_list_size_1(dbl_ll_one_value):
    """Test shit on list containing one element, head&tail should be None"""
    dbl_ll_one_value.shift()
    assert dbl_ll_one_value.head is None and dbl_ll_one_value.tail is None


def test_shift_list_size_2(dbl_ll_2):
    """Test that shifting a list of size 2 reassigns tail."""
    old_tail = dbl_ll_2.tail
    old_size = dbl_ll_2._size
    assert dbl_ll_2.tail.value == dbl_ll_2.shift() and old_tail.prev ==  dbl_ll_2.tail and dbl_ll_2._size == old_size - 1


"""REMOVE SPECIFIC TESTS"""


@pytest.mark.parametrize('s, result', REMOVE_TESTS_STR)
def test_remove_head_tail_middle(s, result, dbl_ll):
    """Test remove with 1 operation on either end and 1 in the middle.
    remove() should run pop() if s is head and shift() if s is tail."""
    assert dbl_ll.remove(s) == result
