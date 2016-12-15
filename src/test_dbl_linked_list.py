"""Test dbl_linked_list data structures."""

import pytest

TEST_ITER = [1, 2, 3, 4, 5]

@pytest.fixture
def create_empty_node():
    from dbl_linked_list import Dbl_Node
    new_node = Dbl_Node()
    return new_node

@pytest.fixture
def create_empty_dbl_ll():
    from dbl_linked_list import Dbl_Linked_List
    new_dll = Dbl_Linked_List()
    return new_dll

@pytest.fixture
def create_dbl_ll_one_value():
    from dbl_linked_list import Dbl_Linked_List
    new_dll = Dbl_Linked_List(5)
    return new_dll

@pytest.fixture
def create_list_with_iter():
    from dbl_linked_list import Dbl_Linked_List
    new_dll = Dbl_Linked_List(TEST_ITER)
    return new_dll


def test_create_empty_dbl_node(create_empty_node):
    """Test creation of an empty node."""
    assert create_empty_node.value is None
    assert create_empty_node.nxt is None
    assert create_empty_node.prev is None


def test_create_node_with_val_nxt_prev():
    """Test creation of Nodes with values and nxt, prev references."""
    from dbl_linked_list import Dbl_Node
    node1 = Dbl_Node(1)
    assert node1.value == 1 and node1.nxt is None and node1.prev is None
    node2 = Dbl_Node("two", node1)
    assert node2.value == "two" and node2.nxt is node1 and node2.prev is None
    node3 = Dbl_Node([3], node1, node2)
    assert node3.value == [3] and node3.nxt is node1 and node3.prev is node2


def test_create_empty_dbl_linked_list(create_empty_dbl_ll):
    """Test creation of empty Dbl_Linked_List."""
    dll = create_empty_dbl_ll
    assert dll.head is None
    assert dll.tail is None


def test_create_list_with_one_value():
    """Test that a list can be created with one value."""
    from dbl_linked_list import Dbl_Linked_List
    dll = Dbl_Linked_List(5)
    assert dll.head.value == 5
    assert dll.tail.value == 5


def test_create_list_with_one_value_assign_head_tail(create_dbl_ll_one_value):
    """Test that a list created with one value has correct prev/next."""
    dll = create_dbl_ll_one_value
    assert dll.head.nxt is None
    assert dll.head.prev is None
    assert dll.tail.nxt is None
    assert dll.tail.prev is None


def test_create_dbl_with_iterable():
    """Given an iterable, test that new Dbl_LL is created."""
    from dbl_linked_list import Dbl_Linked_List
    new_dll = Dbl_Linked_List(TEST_ITER)
    assert new_dll.head.value == 5
    assert new_dll.tail.value == 1


def test_create_dbl_with_iter_correct_size(create_list_with_iter):
    """Test that creating a dbl_ll with an iterable results in correct length."""
    dll = create_list_with_iter
    assert dll._size == 5


def test_create_dbl_with_iter_correct_prev_nxt(create_list_with_iter):
    """Creating a Dbl_LL with an iter head.nxt and tail.prev are correct."""
    dll = create_list_with_iter
    assert dll.head.nxt.value == 4
    assert dll.tail.prev.value == 2


"""PUSH SPECIFIC TESTS"""
def test_push_empty_list(create_empty_dbl_ll):
    """Test pushed val is new head and tail."""
    dll = create_empty_dbl_ll
    dll.push(5)
    assert dll.head.value == 5 and dll.tail.value == 5


def test_push_empty_list_new_head_tail(create_empty_dbl_ll):
    """Test that pushing on an empty list results in a new head, tail."""
    dll = create_empty_dbl_ll
    dll.push(5)
    assert dll.head is dll.tail


def test_first_pushed_val_nxt_prev_is_none(create_empty_dbl_ll):
    """Test that the first pushed Node has no nxt or prev."""
    dll = create_empty_dbl_ll
    dll.push(5)
    assert dll.head.nxt is None and dll.head.prev is None


def test_push_assigns_new_head(create_list_with_iter):
    """Test new head assigned."""
    dll = create_list_with_iter
    dll.push(6)
    assert dll.head.value == 6


def test_push_reassigns_prev_nxt(create_list_with_iter):
    """Test that pushing to a full list correctly assigns prev, nxt."""
    dll = create_list_with_iter
    old_head = dll.head
    dll.push(6)
    assert dll.head.nxt.value == old_head.value
    assert dll.head.nxt.prev is dll.head


def test_push_increases_size(create_list_with_iter):
    dll = create_list_with_iter
    old_size = dll._size
    dll.push(6)
    assert dll._size == old_size + 1

"""APPEND SPECIFIC TESTS"""
def test_append_empty_list(create_empty_dbl_ll):
    """Test appended val is new head and tail."""
    dll = create_empty_dbl_ll
    dll.append(5)
    assert dll.head.value == 5 and dll.tail.value == 5


def test_append_empty_list_new_head_tail(create_empty_dbl_ll):
    """Test that appending on an empty list results in a new head, tail."""
    dll = create_empty_dbl_ll
    dll.push(5)
    assert dll.head is dll.tail


def test_first_appended_val_nxt_prev_is_none(create_empty_dbl_ll):
    """Test that the first appended Node has no nxt or prev."""
    dll = create_empty_dbl_ll
    dll.append(5)
    assert dll.tail.nxt is None and dll.tail.prev is None


def test_append_assigns_new_tail(create_list_with_iter):
    """Test new tail is assigned."""
    dll = create_list_with_iter
    dll.append(6)
    assert dll.tail.value == 6


def test_append_reassigns_prev_nxt(create_list_with_iter):
    """Test that appending to a full list correctly assigns prev, nxt."""
    dll = create_list_with_iter
    old_tail = dll.tail
    dll.append(6)
    assert dll.tail.prev.value == old_tail.value
    assert dll.tail.prev.nxt is dll.tail


def test_append_increases_size(create_list_with_iter):
    """Test that append increases size correctly."""
    dll = create_list_with_iter
    old_size = dll._size
    dll.append(6)
    assert dll._size == old_size + 1

"""POP SPECIFIC TESTS"""
def test_pop_empty_list_raise_error(create_empty_dbl_ll):
    """Test that popping an empty list raises an Index Error."""
    dll = create_empty_dbl_ll
    with pytest.raises(IndexError):
        dll.pop()


def test_pop_reassign_head(create_list_with_iter):
    """Test that popping a populated list reassigns head."""
    dll = create_list_with_iter
    old_head = dll.head
    dll.pop()
    assert old_head.nxt.value == dll.head.value


def test_pop_decrease_size(create_list_with_iter):
    """Test that pop correctly decreases size."""
    dll = create_list_with_iter
    old_size = dll._size
    dll.pop()
    assert dll._size == old_size - 1


def test_pop_reassign_nxt_prev(create_list_with_iter):
    """Test that popping a populated list reassigns head.nxt and head.nxt.prev."""
    dll = create_list_with_iter
    dll.pop()
    assert dll.head.prev is None and dll.head.nxt.prev is dll.head


def test_pop_returns_correct_value(create_list_with_iter):
    """Test that pop returns the correct value."""
    dll = create_list_with_iter
    head_value = dll.head.value
    assert dll.pop() == head_value

"""SHIFT SPECIFIC TESTS"""
def test_shift_empty_list_raise_error(create_empty_dbl_ll):
    """Test that shifting an empty list raises an Index Error."""
    dll = create_empty_dbl_ll
    with pytest.raises(IndexError):
        dll.shift()


def test_shift_reassign_tail(create_list_with_iter):
    """Test that shifting a populated list reassigns head."""
    dll = create_list_with_iter
    old_tail = dll.tail
    dll.shift()
    assert old_tail.prev.value == dll.tail.value


def test_shift_decrease_size(create_list_with_iter):
    """Test that shift correctly decreases size."""
    dll = create_list_with_iter
    old_size = dll._size
    dll.shift()
    assert dll._size == old_size - 1


def test_shift_reassign_nxt_prev(create_list_with_iter):
    """Test that shifting a populated list reassigns head.nxt and head.nxt.prev."""
    dll = create_list_with_iter
    dll.shift()
    assert dll.tail.nxt is None and dll.tail.prev.tail is dll.head


def test_shift_returns_correct_value(create_list_with_iter):
    """Test that shift returns the correct value."""
    dll = create_list_with_iter
    tail_value = dll.tail.value
    assert dll.shift() == tail_value


"""REMOVE SPECIFIC TESTS"""
def test_remove_empty_list_raise_error(create_empty_dbl_ll):
    """Test remove on empty list raises an Index Error."""
    dll = create_empty_dbl_ll
    with pytest.raises(IndexError):
        dll.remove("something")


def test_remove_val_not_in_list(create_list_with_iter):
    """Test remove with value not in list raises Value Error."""
    dll = create_list_with_iter
    with pytest.raises(ValueError):
        dll.remove("something")


def test_remove_case_head(create_list_with_iter):
    """Test remove with case head.  Should run pop()."""
    dll = create_list_with_iter
    old_head = dll.head.nxt
    dll.remove(old_head.value)
    assert dll.head.value is old_head.nxt.value


def test_remove_case_tail(create_list_with_iter):
    """Test remove with case tail.  Should run shift()."""
    dll = create_list_with_iter
    old_tail = dll.tail
    dll.remove(old_tail.value)
    assert dll.tail.value == old_tail.prev.value


def test_remove_head_tail_do_not_change(create_list_with_iter):
    """Test that remove on any other node does not change head or tail."""
    dll = create_list_with_iter
    old_tail = dll.tail
    old_head = dll.head
    dll.remove(dll.head.nxt.value)
    assert old_tail is dll.tail and old_head is dll.head


def test_remove_prev_nxt_reassigned(create_list_with_iter):
    """Test that remove correctly changes prev and nxt."""
    dll = create_list_with_iter
    removed = dll.head.nxt
    dll.remove(removed.value)
    assert dll.head.nxt is removed.nxt and dll.head.nxt.prev is dll.head


def test_remove_correctly_changes_size(create_list_with_iter):
    """Test that remove method correctly changes size."""
    dll = create_list_with_iter
    old_size = dll._size
    dll.remove(dll.head.nxt.value)
    assert old_size == dll._size - 1
