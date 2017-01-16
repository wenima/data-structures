"""Test dbl_linked_list data structures."""

import pytest

TEST_ITER = [1, 3, 5, 4, 9, 8, 12, 11]

TEST_DICT = [
    (7, [8, 3, 9, 1, 5, 12, 4, 7, 11]),
    (25, [5, 10, 20, 25, 30, 40, 50, 60, 70]),
]

TEST_DEPTH = [
    (7, 4),
    (10, 5),
]


@pytest.fixture
def create_empty_node():
    from bst import TreeNode
    new_node = TreeNode()
    return new_node

@pytest.fixture
def empyt_bst():
    from bst import bst
    new_bst = bst()
    return new_bst

@pytest.fixture
def bst_one_node():
    from bst import bst
    new_bst = bst(TEST_ITER[-1])
    return new_bst

@pytest.fixture
def bst():
    from bst import bst
    new_bst = bst(TEST_ITER)
    return new_bst


def test_create_empty_treenode(create_empty_node):
    """Test creation of an empty node."""
    assert create_empty_node.value is None
    assert create_empty_node.left is None
    assert create_empty_node.right is None
    assert create_empty_node.parent is None

def test_has_iter(empty_bst):
    """Test that the Binary Search Tree is iterable."""
    assert '__iter__' in dir(empty_bst)

def test_insert_at_end_of_tree(bst):
    """Test insert node at end of tree"""
    bst.insert(7)
    new_node = bst.search(7)
    assert bst.contains(7)
    assert new_node.left is None
    assert new_node.right is None
    assert new_node.parent.value == 5


@pytest.mark.parametrize('n, result', TEST_DICT
def test_insert_puts_node_in_right_place(bst):
    """Test insert works correctly."""
    bst.insert(n)
    assert bst.contains(n)
    assert bst.search(n.left).value < n.value
    assert bst.search(n.right).value > n.value

def test_tree_is_empty(empty_bst):
    """Test size of an empty tree is equal to 0."""
    assert empty_bst.size() == 0

def test_contains_returns_false(empty_bst):
    """Test that contains return False if node is not found."""
    assert empty_bst.contains(1) == False

@pytest.mark.parametrize('n, result', TEST_DEPTH
def test_depth_returns_correct_value(bst):
    """Test depth returns correct value in a full tree."""
    bst.insert(n)
    assert bst.depth() == result
