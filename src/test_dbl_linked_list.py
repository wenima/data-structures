"""Test dbl_linked_list data structures."""

import pytest

TEST_ITER = [1, 2, 3, 4, 5]
sample_from_the_midde_of_iterable = random.choice(TEST_ITER[1:len(TEST_ITER) - 1])


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
    assert new_dll.head.value == TEST_ITER[-1]
    assert new_dll.tail.value == TEST_ITER[0]


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


def test_pop_empty_list_raise_error(dbl_ll_empty):
    """Test that popping an empty list raises an Index Error."""
    with pytest.raises(IndexError):
        dbl_ll_empty.pop()


def test_pop_reassign_head(dbl_ll):
    """Test that popping a populated list reassigns head."""
    old_head = dbl_ll.head
    dbl_ll.pop()
    assert old_head.nxt.value == dbl_ll.head.value


def test_pop_decrease_size(dbl_ll):
    """Test that pop correctly decreases size."""
    old_size = dbl_ll._size
    dbl_ll.pop()
    assert dbl_ll._size == old_size - 1


def test_pop_reassign_nxt_prev(dbl_ll):
    """Test that popping a populated list reassigns head.nxt and head.nxt.prev."""
    dbl_ll.pop()
    assert dbl_ll.head.prev is None and dbl_ll.head.nxt.prev is dbl_ll.head


def test_pop_returns_correct_value(dbl_ll):
    """Test that pop returns the correct value."""
    assert dbl_ll.head.value == dbl_ll.pop()


"""SHIFT SPECIFIC TESTS"""


def test_shift_empty_list_raise_error(dbl_ll_empty):
    """Test that shifting an empty list raises an Index Error."""
    with pytest.raises(IndexError):
        dbl_ll_empty.shift()


def test_shift_reassign_tail(dbl_ll):
    """Test that shifting a populated list reassigns tail."""
    old_tail = dbl_ll.tail
    dbl_ll.shift()
    assert old_tail.prev.value == dbl_ll.tail.value


def test_shift_decrease_size(dbl_ll):
    """Test that shift correctly decreases size."""
    old_size = dbl_ll._size
    dbl_ll.shift()
    assert dbl_ll._size == old_size - 1


def test_shift_reassign_nxt_prev(dbl_ll):
    """Test that shifting a populated list reassigns tail.prev"""
    dbl_ll.shift()
    assert dbl_ll.tail.nxt is None and dbl_ll.tail.prev.nxt is dbl_ll.tail


def test_shift_returns_correct_value(dbl_ll):
    """Test that shift returns the correct value."""
    tail_value = dbl_ll.tail.value
    assert dbl_ll.shift() == tail_value


"""REMOVE SPECIFIC TESTS"""


def test_remove_val_not_in_list(dbl_ll):
    """Test remove with value not in list raises Value Error."""
    with pytest.raises(ValueError):
        dbl_ll.remove("something")

@pytest.mark.parametrize('s, result', TEST_STRINGS)
def test_string_to_array(s, result):
    """Test if string_to_array outputs a list from an input string"""
    from kata_string_to_array import string_to_array
    assert string_to_array(s) == result

@pytest.mark.parametrize('s, result', REMOVE_TESTS)
def test_remove_case_head(s, result, dbl_ll):
    """Test remove with case head.  Should run pop()."""
    new_head = dbl_ll.head.nxt
    assert dbl_ll.remove(TEST_ITER[-1]) == result and new_head == dbl_ll.head


def test_remove_case_tail(dbl_ll):
    """Test remove with case tail.  Should run shift()."""
    new_tail = dbl_ll.tail.prev
    dbl_ll.remove(TEST_ITER[0])
    assert new_tail is dbl_ll.tail


def test_remove_head_tail_do_not_change(dbl_ll):
    """Test that remove on any other node does not change head or tail."""
    old_tail = dbl_ll.tail
    old_head = dbl_ll.head
    dbl_ll.remove(sample_from_the_midde_of_iterable)
    assert old_tail is dbl_ll.tail and old_head is dbl_ll.head


def test_remove_prev_nxt_reassigned(dbl_ll):
    """Test that remove correctly changes prev and nxt."""
    removed = dbl_ll.head.nxt
    dbl_ll.remove(removed.value)
    assert dbl_ll.head.nxt is removed.nxt and dbl_ll.head.nxt.prev is dbl_ll.head


def test_remove_correctly_changes_size(dbl_ll):
    """Test that remove method correctly changes size."""
    old_size = dbl_ll._size
    dbl_ll.remove(dbl_ll.head.nxt.value)
    assert old_size == dbl_ll._size + 1
