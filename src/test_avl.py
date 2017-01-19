"""Test self-balancing tree methods."""
import pytest


UNBALANCED = [50, 30, 70, 20, 40, 80, 60, 65, 75, 85, 34, 33, 36, 35]
BALANCED = [50, 30, 70, 20, 40, 80, 60, 65, 75, 85, 34, 33, 36, 29, 41]


@pytest.fixture
def unbalanced_avl():
    """Return unbalanced avl."""
    from avl import AVL
    new_avl = AVL(UNBALANCED)
    return new_avl


@pytest.fixture
def balanced_avl(unbalanced_avl):
    """Return balanced avl."""
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


def test_rebalance_left_rotation():
    """Test all the connections after a left rotation rebalance."""
    from avl import AVL
    lefty = AVL([1, 4, 8])
    lefty.rebalance(lefty.root)
    assert lefty.root.val == 4
    children = lefty.root.children()
    assert [c.val for c in children] == [1, 8]
    for child in children:
        assert child.parent is lefty.root


def test_rebalance_right_rotation():
    """Test all the connections after a right rotation rebalance."""
    from avl import AVL
    righty = AVL([8, 4, 1])
    righty.rebalance(righty.root)
    assert righty.root.val == 4
    children = righty.root.children()
    assert [c.val for c in children] == [1, 8]
    for child in children:
        assert child.parent is righty.root


def test_rebalance_right_left_rotation():
    """Test all the connections after a right rotation rebalance."""
    from avl import AVL
    refty = AVL([1, 8, 4])
    refty.rebalance(refty.root)
    assert refty.root.val == 4
    children = refty.root.children()
    assert [c.val for c in children] == [1, 8]
    for child in children:
        assert child.parent is refty.root


def test_rebalance_left_right_rotation():
    """Test all the connections after a right rotation rebalance."""
    from avl import AVL
    lighty = AVL([8, 1, 4])
    lighty.rebalance(lighty.root)
    assert lighty.root.val == 4
    children = lighty.root.children()
    assert [c.val for c in children] == [1, 8]
    for child in children:
        assert child.parent is lighty.root
