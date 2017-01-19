"""Test self-balancing tree methods."""
import pytest


UNBALANCED = [50, 30, 70, 20, 40, 80, 60, 65, 75, 85, 34, 33, 36, 35]
BALANCED = [50, 30, 70, 20, 40, 80, 60, 65, 75, 85, 34, 33, 36, 29, 41]


@pytest.fixture
def unbalanced_avl():
    from avl import AVL
    new_avl = AVL(UNBALANCED)
    return new_avl


@pytest.fixture
def balanced_avl(unbalanced_avl):
    from avl import AVL
    new_avl = AVL(BALANCED)
    return new_avl


def test_check_balance_balanced_returns_none(balanced_avl):
    """Check balanced on balanced tree should return None."""
    for node in balanced_avl:
        assert balanced_avl.check_balance(node) is None


def test_check_balance_unbalanced_returns_unbalanced_subtree_root(unbalanced_avl):
    """Check balance should return root of unbalanced subtree."""
    a_node = unbalanced_avl.search(35)
    another_node = unbalanced_avl.search(20)
    assert unbalanced_avl.check_balance(a_node).val == 40
    assert unbalanced_avl.check_balance(another_node).val == 30
