"""Testing the linked_list class - CF 401 Python Week 2 Assignment."""
import pytest

@pytest.fixture
def new_list():
    from linked_list import  Linked_List
    this_list = Linked_List()
    return this_list


def test_create_new_empty_Stack_out_of_Linked_List():
    from stack import Stack
    new_stack = Stack()
    assert new_stack._container.head is None


def test_create_empty_Linked_List():
    from linked_list import Linked_List
    new_list = Linked_List()
    assert new_list.head is None


def test_empty_new_node_object_has_none():
    """Test the emptyiness of a node."""
    from linked_list import Node
    new_node = Node()
    assert new_node.value is None
    assert new_node.nxt is None

def test_new_node_has_data():
    """Test if a new node is correctly created with data"""
    from linked_list import Node
    new_node = Node("five")
    assert new_node.value == "five"

def test_when_initialized_with_iterable_makes_nodes():
    """Test if the number of nodes matches the number of elements passed with
    the iterable"""
    from stack import Stack
    my_nodes = [1, 2, 3]
    new_stack = Stack(my_nodes)
    assert len(new_stack._container) == 3
