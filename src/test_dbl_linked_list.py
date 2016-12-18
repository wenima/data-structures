"""Test dbl_linked_list data structures."""

import pytest
import random

TEST_ITER = [1, 2, 3, 4, 5]
TEST_ITER_2 = [1, 2]
middle_item = random.choice(TEST_ITER[1:len(TEST_ITER) - 1])
idx = [i for i, x in enumerate(TEST_ITER) if x == middle_item]


REMOVE_TESTS_STR = [
    (TEST_ITER[0], "Succesfully removed Node with value: {0}. New tail set to {1}, new size is {2}".format(TEST_ITER[0], TEST_ITER[1], len(TEST_ITER) - 1)),
    (middle_item, "Succesfully removed Node with value: {0}. {1} points now to {2} and {3} to {4}, new size is {5}".format(TEST_ITER[idx[0]], TEST_ITER[idx[0] + 1], TEST_ITER[idx[0] - 1], TEST_ITER[idx[0] - 1], TEST_ITER[idx[0] + 1], len(TEST_ITER) - 1)),
    (TEST_ITER[-1], "Succesfully removed Node with value: {0}. New head set to {1}, new size is {2}".format(TEST_ITER[-1], TEST_ITER[ - 2], len(TEST_ITER) - 1)),
    ("not_in_list", ValueError),
]


@pytest.fixture
def create_empty_node():
    from dbl_linked_list import DblNode
    new_node = DblNode()
    return new_node

@pytest.fixture
def dbl_ll_empty():
    from dbl_linked_list import DblLinkedList
    new_dll = DblLinkedList()
    return new_dll

@pytest.fixture
def dbl_ll_one_value():
    from dbl_linked_list import DblLinkedList
    new_dll = DblLinkedList(TEST_ITER[-1])
    return new_dll

@pytest.fixture
def dbl_ll():
    from dbl_linked_list import DblLinkedList
    new_dll = DblLinkedList(TEST_ITER)
    return new_dll


def test_create_empty_dbl_node(create_empty_node):
    """Test creation of an empty node."""
    assert create_empty_node.value is None
    assert create_empty_node.nxt is None
    assert create_empty_node.prev is None


def test_create_node_with_val_nxt_prev():
    """Test creation of Nodes with values and nxt, prev references."""
    from dbl_linked_list import DblNode
    node1 = DblNode(1)
    assert node1.value == 1 and node1.nxt is None and node1.prev is None
    node2 = DblNode("two", node1)
    assert node2.value == "two" and node2.nxt is node1 and node2.prev is None
    node3 = DblNode([3], node1, node2)
    assert node3.value == [3] and node3.nxt is node1 and node3.prev is node2


def test_create_empty_dbl_linked_list(dbl_ll_empty):
    """Test creation of empty DblLinkedList."""
    assert dbl_ll_empty.head is None
    assert dbl_ll_empty.tail is None


def test_create_list_with_one_value(dbl_ll_one_value):
    """Test that a list can be created with one value."""
    assert dbl_ll_one_value.head.value == TEST_ITER[-1]
    assert dbl_ll_one_value.tail.value == TEST_ITER[-1]


def test_create_list_with_one_value_assign_head_tail(dbl_ll_one_value):
    """Test that a list created with one value has correct prev/next."""
    assert dbl_ll_one_value.head.nxt is None
    assert dbl_ll_one_value.head.prev is None
    assert dbl_ll_one_value.tail.nxt is None
    assert dbl_ll_one_value.tail.prev is None


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
    assert dbl_ll_empty.head.value == TEST_ITER[-1]
    assert dbl_ll_empty.tail.value == TEST_ITER[-1]


def test_push_empty_list_new_head_tail(dbl_ll_empty):
    """Test that pushing on an empty list results in a new head, tail."""
    dbl_ll_empty.push(TEST_ITER[-1])
    assert dbl_ll_empty.head is dbl_ll_empty.tail
    assert dbl_ll_empty.head.nxt is None
    assert dbl_ll_empty.head.prev is None


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


"""APPEND SPECIFIC TESTS"""


def test_append_empty_list(dbl_ll_empty):
    """Test appended val is new head and tail."""
    dbl_ll_empty.append(TEST_ITER[-1])
    assert dbl_ll_empty.head.value == TEST_ITER[-1]
    assert dbl_ll_empty.tail.value == TEST_ITER[-1]


def test_append_empty_list_new_head_tail(dbl_ll_empty):
    """Test that appending on an empty list results in a new head, tail."""
    dbl_ll_empty.append(TEST_ITER[-1])
    assert dbl_ll_empty.head is dbl_ll_empty.tail


def test_first_appended_val_nxt_prev_is_none(dbl_ll_empty):
    """Test that the first appended Node has no nxt or prev."""
    dbl_ll_empty.append(TEST_ITER[-1])
    assert dbl_ll_empty.tail.nxt is None
    assert dbl_ll_empty.tail.prev is None


def test_append_assigns_new_tail(dbl_ll):
    """Test new tail is assigned."""
    dbl_ll.append(6)
    assert dbl_ll.tail.value == 6


def test_append_iterable_in_reverse(dbl_ll):
    """Test that appending the iterable in reverse order has the correctly
    structure"""
    for item in reversed(TEST_ITER):
        dbl_ll.append(item)
    assert len(dbl_ll) == len(TEST_ITER) * 2
    assert dbl_ll.tail.prev.value == TEST_ITER[1]
    assert dbl_ll.tail.prev.nxt is dbl_ll.tail


"""POP SPECIFIC TESTS"""


def test_pop_from_empty_list(dbl_ll_empty):
    """Test pop from empty list to return an IndexError"""
    with pytest.raises(IndexError):
        dbl_ll_empty.pop()


def test_pop_a_list_from_len_to_zero(dbl_ll):
    """Test using pop to empty a doubley linked list. At length 2 check
    for a special condition."""
    for i in range(len(TEST_ITER) - 1):
        if len(dbl_ll) == 2:
            old_head = dbl_ll.head
            assert dbl_ll.head.value == dbl_ll.pop()
            assert old_head.nxt == dbl_ll.head
        dbl_ll.pop()
    assert dbl_ll.head is None
    assert dbl_ll.tail is None


"""SHIFT SPECIFIC TESTS"""


def test_shift_empty_list_raise_error(dbl_ll_empty):
    """Test that shifting an empty list raises an Index Error."""
    with pytest.raises(IndexError):
        dbl_ll_empty.shift()


def test_shift_a_list_from_len_to_zero(dbl_ll):
    """Test using shift to empty a doubley linked list. At length 2, check
    for a special condition"""
    for i in range(len(TEST_ITER) - 1):
        if len(dbl_ll) == 2:
            old_tail = dbl_ll.tail
            assert dbl_ll.tail.value == dbl_ll.shift()
            assert old_tail.prev ==  dbl_ll.tail
        dbl_ll.shift()
    assert dbl_ll.head is None
    assert dbl_ll.tail is None


"""REMOVE SPECIFIC TESTS"""


@pytest.mark.parametrize('s, result', REMOVE_TESTS_STR)
def test_remove_head_tail_middle(s, result, dbl_ll):
    """Test remove with 1 operation on either end and 1 in the middle.
    remove() should run pop() if s is head and shift() if s is tail."""
    assert dbl_ll.remove(s) == result
