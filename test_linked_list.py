"""Testing the linked_list class - CF 401 Python Week 2 Assignment."""
import pytest


def test_node_init():
    """Test the initialization of a node."""
    from linked_list import Node
    assert type(Node) == type


def test_node_instantiation():
    """Test if the Node objects gets initiated correctly"""
    from linked_list import Node, init_node
    assert init_node() == "<class 'linked_list.Node'>"


def test_node_value():
    """Test the contents of nodes created with given input."""
    from linked_list import Node
    node2 = Node("Something")
    assert node2.value == "Something" and node2.nxt == None


def test_linked_list_init():
    """Test initialization of the linked_list."""
    from linked_list import Linked_List
    assert type(Linked_List) == type


def test_linked_list_push():
    """Test the push method of the Linked List class."""
    from linked_list import Node, Linked_List
    new_ll = Linked_List()
    new_ll.push("Something")
    assert new_ll.head.value == "Something" and new_ll.tail.value == "Something" and new_ll.length == 1


# def test_linked_list_search():


def test_linked_list_pop():
    """Test the pop method of the Linked List class."""
    from linked_list import Node, Linked_List, create_ll
    new_ll = create_ll()
    old_head_val = new_ll.head.value
    new_ll.pop()
    new_head_val = new_ll.head.value
    assert old_head_val == "two" and new_head_val == "something else"


# def test_linked_list_size():