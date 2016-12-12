"""Testing the linked_list class - CF 401 Python Week 2 Assignment."""
import pytest

PARAMS_NODE_VALUES = [
    ("something"),
    ("something 2", "something 3")
]


def test_node_init():
    """Test the initialization of a node."""
    from linked_list import Node
    assert type(Node) == type

# @pytest.mark.parametrize(value, nxt, PARAMS_NODE_VALUES)
# # def test_node_value(value, nxt):
#     """Test the contents of nodes created with given input."""

def test_node_instantiation():
    """Test if the Node objects gets initiated correctly"""
    from linked_list import Node, init_node
    assert init_node() == "<class 'linked_list.Node'>"

def test_node_assign_value():
    """Test if the Node objects takes a value and returns it correctly"""
    from linked_list import Node, set_note_attributes
    assert set_note_attributes
