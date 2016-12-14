"""Test dbl_linked_list data structures."""

import pytest

@pytest.fixture
def create_empty_node():
    from dbl_linked_list import Dbl_Node
    new_node = Dbl_Node()
    return new_node


def test_create_empty_dbl_node(create_empty_node):
    """Test creation of an empty node."""
    assert create_empty_node.value is None
    assert create_empty_node.nxt is None
    assert create_empty_node.prev is None


def test_create_node_with_