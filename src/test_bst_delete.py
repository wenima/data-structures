"""Test BST traversal methods."""

import pytest
import types


TEST_BST1 = [50, 30, 70, 20, 40, 80, 60, 65, 75, 85, 32, 34, 36, 10]


TEST_BST_DELETE = [
    #delete a leaf, check children for middle value, result should match last value
    (10, 20, []),
    #delete a node with only one child on the left
    (20, 30, [10, 40]),
    #child on the right
    (34, 32, [36]),
    #delete a node with a tree under it on the right side
    (32, 40, [34]),
    # #delete a node with 2 children under it
    (70, 50, [30, 75]),
    (80, 70, [60, 85])
]


@pytest.fixture
def bst_one_node():
    from bst import BST
    new_bst = BST(TEST_BST1[-1])
    return new_bst


@pytest.fixture
def bst1():
    from bst import BST
    new_bst = BST(TEST_BST1)
    return new_bst


@pytest.fixture
def bst2(bst1):
    bst1.insert(31)
    bst1.insert(31.5)
    return bst1


@pytest.mark.parametrize('d, n, result', TEST_BST_DELETE)
def test_delete_returns_correct_children(d, n, result, bst1):
    """Test delete a node keeps tree intact."""
    bst1.delete(d)
    children = [c.val for c in bst1.search(n).children()]
    assert children == result
