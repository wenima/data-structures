"""Testing the linked_list class - CF 401 Python Week 2 Assignment."""
import pytest

PARAMS_SAMPLE_LIST = ["something", 1, "pear", 3, "apple"]

def create_new_ll(lst):
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


# def test_linked_list_search_success():
#     """Test the search method of the Linked List class with a search query that exists."""
#     from linked_list import Node, Linked_List
#     new_ll = 

# def test_linked_list_search_failure():
#     """Test the search method of the Linked List class with a search query that DOES NOT exist."""

def test_linked_list_pop():
    """Test the pop method of the Linked List class."""
    from linked_list import Node, Linked_List, create_ll
    new_ll = create_ll()
    old_head_val = new_ll.head.value
    new_ll.pop()
    new_head_val = new_ll.head.value
    assert old_head_val == "two" and new_head_val == "something else"

def test_linked_list_display():
    """Test the display method of the Linked_List class."""
    from linked_list import Node, Linked_List, create_ll
    new_linked_list = create_ll()
    result = "('two', 'something else', 'something')"
    assert new_linked_list.display() == result

# def test_linked_list_size():
