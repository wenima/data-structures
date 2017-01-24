"""Test self-balancing tree methods."""
import pytest


BALANCED = [50, 30, 70, 20, 40, 80, 60, 65, 75, 85, 34, 33, 36, 29, 41]
TEST_DEEP = [19, 17, 24, 88, 25, 59, 49, 87, 79, 65, 74]
PROBLEMATIC = [60, 34, 80, 12, 40, 73, 89, 5, 23, 38, 47, 65, 76, 86, 94, 3, 9, 13, 30, 37, 39, 42, 50, 62, 72, 75, 79, 83, 88, 91, 96, 2, 4, 18, 25, 41]
BAD = [425, 314, 649, 244, 362, 593, 751, 216, 319, 369, 505, 615, 682, 816, 370, 572, 670, 739, 801, 891, 773, 881]


@pytest.fixture
def balanced_avl():
    """Return balanced avl."""
    from avl import AVL
    new_avl = AVL(BALANCED)
    return new_avl


@pytest.fixture(params=[BALANCED, TEST_DEEP, PROBLEMATIC, BAD])
def diff_avl(request):
    """Return balanced avl."""
    from avl import AVL
    new_avl = AVL(request.param)
    return new_avl, request.param


@pytest.fixture
def random_avl():
    """Return large random avl."""
    import random
    from avl import AVL
    rando_avl = AVL()
    for i in range(80):
        rando_avl.insert(random.randint(0, 100))
    return rando_avl


RANDOM = random_avl()


def test_init_non_iterable():
    """If non iterable is passed to init, it should insert non iterable."""
    from avl import AVL
    avl = AVL(5)
    assert avl.root.val == 5


def test_check_balance_balanced_returns_none(balanced_avl):
    """Check balanced on balanced tree should return None."""
    for node in balanced_avl:
        assert balanced_avl._check_balance(node) is None


def test_check_balance_unbalanced_returns_unbalanced_subtree_root(balanced_avl):
    """Check balance should return root of unbalanced subtree."""
    from bst import TreeNode
    node = balanced_avl.search(36)
    node.left = TreeNode(35, parent=node)
    node.left.left = TreeNode(34.4, parent=node.left)
    assert balanced_avl._check_balance(node.left.left).val == 36


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


def test_auto_balance_on_insertion(diff_avl):
    """Test auto balancing on large random trees."""
    avl, values = diff_avl
    nodes = avl.pre_order()
    for node in nodes:
        assert abs(avl.balance(avl.search(node))) <= 1


def test_auto_balance_on_insertion_random_tree(random_avl):
    """Test auto balancing on large random trees."""
    nodes = random_avl.pre_order()
    for node in nodes:
        assert abs(random_avl.balance(random_avl.search(node))) <= 1


@pytest.mark.parametrize('value', list(RANDOM.pre_order()))
def test_rebalance_after_delete_random_tree(value):
    """Test avl rebalances after deletions."""
    RANDOM.delete(value)
    nodes = RANDOM.pre_order()
    for node in nodes:
        actual_node = RANDOM.search(node)
        assert abs(RANDOM.balance(actual_node)) <= 1


def test_rebalance_after_delete_for_deep(diff_avl):
    """Test avl rebalances after deletions."""
    avl, values = diff_avl
    nodes = avl.pre_order()
    for node in nodes:
        actual_node = avl.search(node)
        for value in values:
            if value != node:
                avl.delete(value)
                assert abs(avl.balance(actual_node)) <= 1
