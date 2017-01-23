"""Test for binary search tree data structures."""

import pytest
from random import randint

TEST_BST1 = [1, 3, 5, 4, 9, 8, 12, 11]
TEST_BST2 = [11, 6, 8, 19, 4, 12, 5, 17, 43, 49, 31]

TEST_DICT = [
    (10, [10, 6, 11, 4, 8, 19, 5, 10, 17, 43, 31, 49]),
    (7, [8, 3, 9, 1, 5, 12, 4, 7, 11]),
    (25, [5, 10, 20, 25, 30, 40, 50, 60, 70]),
]

TEST_DEPTH = [
    (55, 5),
    # (10, 5),
]

TEST_BALANCE = [
    (TEST_BST1, -5),
    (TEST_BST2, 0),
    ([50, 40, 30, 20, 10, 60], 3),
]


@pytest.fixture
def create_empty_node():
    """Return node with val of 1."""
    from bst import TreeNode
    new_node = TreeNode(1)
    return new_node


@pytest.fixture
def empty_bst():
    """Return bst with no nodes."""
    from bst import BST
    empty_bst = BST()
    return empty_bst


@pytest.fixture
def bst_one_node():
    """Return bst with one node with val of 11."""
    from bst import BST
    new_bst = BST(TEST_BST1[-1])
    return new_bst


@pytest.fixture
def bst1():
    """Return bst filled with nodes."""
    from bst import BST
    new_bst = BST(TEST_BST1)
    return new_bst


@pytest.fixture
def bst2():
    """Return bst filled with more nodes."""
    from bst import BST
    new_bst = BST(TEST_BST2)
    return new_bst


def test_create_empty_treenode(create_empty_node):
    """Test creation of an empty node."""
    assert create_empty_node.val is 1
    assert create_empty_node.left is None
    assert create_empty_node.right is None
    assert create_empty_node.parent is None


def test_insert_at_end_of_tree(bst1):
    """Test insert node at end of tree."""
    bst1.insert(7)
    new_node = bst1.search(7)
    assert bst1.contains(7)
    assert new_node.parent.val == 8
    assert new_node.is_leaf()


def test_insert_node_at_root(empty_bst):
    """Test insert node at root."""
    empty_bst.insert(10)
    assert empty_bst.root.val == 10
    assert empty_bst.root.is_leaf()
    assert empty_bst.depth() == 1


def test_insert_existing_node(bst2):
    """Test inserting a node that already exists."""
    cur_size = bst2.size
    bst2.insert(8)
    assert cur_size == bst2.size


def test_tree_is_empty(empty_bst):
    """Test size of an empty tree is equal to 0."""
    assert empty_bst.size == 0


def test_contains_returns_false(empty_bst):
    """Test that contains return False if node is not found."""
    assert empty_bst.contains(1) is False


def test_size_is_increased_when_initialized_w_one_node(bst_one_node):
    """Test that size is increased when initialized with one node."""
    assert bst_one_node.size == 1


def test_size_is_equal_to_iterable(bst1):
    """Test that size is increased correctly when initialized with an iterable."""
    assert bst1.size == len(TEST_BST1)


def test_size_is_increased_when_adding_nodes(bst2):
    """Test that size is increased correctly when removing a node."""
    add_amt = randint(0, 100)
    dupes = 0
    for i in range(add_amt):
        insert_val = randint(50, 1000)
        if bst2.contains(insert_val):
            dupes += 1
        bst2.insert(insert_val)
    assert bst2.size == len(set(TEST_BST2)) + add_amt - dupes


@pytest.mark.parametrize('s, result', TEST_DEPTH)
def test_depth_returns_correct_val(s, result, bst2):
    """Test depth returns correct val in a full tree."""
    bst2.insert(s)
    assert bst2.depth() == result


@pytest.mark.parametrize('s, result', TEST_BALANCE)
def test_balance_returns_correct_val(s, result):
    """Test balance returns correct val in a full tree."""
    from bst import BST
    b = BST(s)
    assert b.balance() == result


def test_balance_called_with_none_returns_zero(empty_bst):
    """Test balance returns zero."""
    assert empty_bst.balance(None) == 0