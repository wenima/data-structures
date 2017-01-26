"""Unit tests for Ternary Search Trie."""

import pytest
import types


TEST_TST_INSERT = [
    #insert into the TEST, giving a string and check for no. of leaves and
    #size (no of unique chars in the path to a word represents a node)
    ('sea'),
    ('sea shells'),
    ('the quick brown fox jumped over the lazy dog'),
    ]

TEST_TST = [
(1, [3]),
(2, [8]),
(8, [36]),
]

HASHES = [

]

@pytest.fixture
def create_empty_node():
    """Return an empty node."""
    from trie import TreeNode
    new_node = TreeNode()
    return new_node

@pytest.fixture
def empty_tst():
    """Return empty tst."""
    from trie import TST
    empty_tst = TST()
    return empty_tst

@pytest.fixture(params=TEST_TST)
def tst(request):
    from trie import TST
    new_tst = TST(request.param)
    return new_tst


def test_create_empty_treenode(create_empty_node):
    """Test creation of an empty node."""
    assert create_empty_node.hash is None
    assert create_empty_node.left is None
    assert create_empty_node.right is None
    assert create_empty_node.center is None
    assert create_empty_node.parent is None
    assert create_empty_node.char is ''


def test_insert_at_end_of_tree(empty_tst):
    """Test insert node at end of tree."""
    empty_tst.insert('xyz')
    assert empty_tst.contains('xyz')
    assert empty_tst._size == 3

# @pytest.mark.parametrize('leaves, nodes', TEST_TST)
# def test_insert_returns_correct_number_of_nodes_and_words(leaves, nodes, tst):
#     """Test insert into a TST."""
#     assert count_leaves() == leaves
#     assert tst.size() == nodes
