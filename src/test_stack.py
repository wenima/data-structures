"""Testing the linked_list class - CF 401 Python Week 2 Assignment."""
import pytest

PARAMS_SAMPLE_LIST = ["something", 1, "pear", 3, "apple"]

def create_new_empty_ll(lst):
    """Given a list, create a new Linked List with all the values."""
    from linked_list import Node, Linked_List
    new_ll = Linked_List()
    for value in lst:
        new_ll.push(value)
    return new_ll


def test_node_init():
    """Test the initialization of a node."""
    from linked_list import Node
    assert type(Node) == type


def test_node_instantiation():
    """Test if the Node objects gets initiated correctly"""
    from linked_list import Node, init_node
    assert init_node() == "<class 'linked_list.Node'>"


def empty_new_node_object_has_none():
    """Test the emptyiness of a node."""
    from linked_list import Node
    new_node = Node()
    assert new_node.value is None
    assert new_node.nxt is None

def baseclass_has_none_as_nxt():
    """Test if the baseclass has field set to None"""
    from linked_list import Node
    assert Node.nxt == None
