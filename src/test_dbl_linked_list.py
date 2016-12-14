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


def test_create_dbl_with_iterable():
    """Given an iterable, test that new Dbl_LL is created."""
    from dbl_linked_list import Dbl_Linked_List
    new_dll = Dbl_Linked_List(TEST_ITER)
    assert new_dll.head.value == 5

"""PUSH SPECIFIC TESTS"""
def test_pushed_val_is_new_head_and_tail(create_empty_dbl_ll):
    """Test pushed val is new head and tail."""
    dll = create_empty_dbl_ll
    dll.push(5)
    assert dll.head.value == 5 and dll.tail.value == 5


def test_first_pushed_val_nxt_prev_is_none(create_empty_dbl_ll):
    """Test that the first pushed Node has no nxt or prev."""
    dll = create_empty_dbl_ll
    dll.push(5)
    assert dll.head.nxt is None and dll.head.prev is None


def test_push_new_head_points_to_old_head(create_empty_dbl_ll):
    """Test new head points to old head, old head to new."""
    dll = create_empty_dbl_ll
    dll.push(5)
    old = dll.head
    dll.push(3)
    assert dll.head.next is old


def test_push_old_prev_points_to_new_head(create_empty_dbl_ll):
    """Test that the new head is prev of old head."""
    dll = create_empty_dbl_ll
    dll.push(5)
    old = dll.head
    dll.push(3)
    assert old.prev is dll.head


def test_push_old_head_is_now_tail(create_empty_dbl_ll):
    """Test the old head is now tail in list of two."""
    dll = create_empty_dbl_ll
    dll.push(5)
    old_tail = dll.head
    dll.push(4)
    assert old_tail.value == dll.tail.value


def test_push_tail_still_tail(create_empty_dbl_ll):
    """Test that the old tail is still tail when pushed."""
    dll = create_empty_dbl_ll
    dll.push(5)
    old_tail = dll.tail
    dll.push(4)
    assert old_tail.value == dll.tail.value

"""APPEND SPECIFIC TESTS"""
def test_append_empty_list_new_tail_and_head(create_empty_dbl_ll):
    """Test that new tail is created on append."""
    dll = create_empty_dbl_ll
    dll.append(5)
    assert dll.head.value == 5 and dll.tail.value == 5

def test_append_new_tail(create_empty_dbl_ll):
    """Test that when a new tail is added, the tail attribute is updated."""
    dll = create_empty_dbl_ll
    dll.append(5)
    dll.append(4)
    assert dll.tail.value == 4

def test_append_tail_head_doesnt_change(create_empty_dbl_ll):
    """Test that when a new tail is added, the head doesn't change."""
    dll = create_empty_dbl_ll
    dll.append(5)
    new_head = dll.head
    dll.append(4)
    assert new_head.value == dll.head.value

def test_append_tail_nxt_prev_updated(create_empty_dbl_ll):
    """Test that when a val is appended, the prev of the old tail is updated."""
    dll = create_empty_node
    dll.append(5)
    old_tail = dll.tail
    dll.append(4)
    assert old_tail.prev.value == dll.tail.value
    assert dll.tail.nxt.value == old_tail.value

"""POP SPECIFIC TESTS"""

