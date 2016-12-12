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
# def test_node_value(value, nxt):
    """Test the contents of nodes created with given input."""
