"""Test BST traversal methods."""

import pytest
import types


TEST_BST1 = [2, 1, 3, 5, 4, 9, 8, 12, 11, 11]
TEST_BST2 = [11, 6, 8, 19, 4, 12, 5, 17, 43, 49, 31]


@pytest.fixture
def empty_bst():
    from bst import BST
    empty_bst = BST()
    return empty_bst

@pytest.fixture
def bst1():
    from bst import BST
    new_bst = BST(TEST_BST1)
    return new_bst


@pytest.fixture
def bst2():
    from bst import BST
    new_bst = BST(TEST_BST2)
    return new_bst

def test_in_order_on_empty(empty_bst):
    """Test in order traversal of empty bst returns empty generator."""
    assert list(empty_bst.in_order()) == []


def test_pre_order_on_empty(empty_bst):
    """Test pre order traversal of empty bst returns empty generator."""
    assert list(empty_bst.pre_order()) == []


def test_post_order_on_empty(empty_bst):
    """Test post order traversal of empty bst returns empty generator."""
    assert list(empty_bst.post_order()) == []


def test_breadth_first_on_empty(empty_bst):
    """Test breadth first traversal of empty bst returns empty generator."""
    assert list(empty_bst.breadth_first(empty_bst.root)) == []


def test_in_order_returns_generator(bst1):
    """Test in order traversal returns a generator."""
    assert isinstance(bst1.in_order(), types.GeneratorType)


def test_pre_order_returns_generator(bst1):
    """Test pre order traversal returns a generator."""
    assert isinstance(bst1.pre_order(), types.GeneratorType)


def test_post_order_returns_generator(bst1):
    """Test post order traversal returns a generator."""
    assert isinstance(bst1.post_order(), types.GeneratorType)


def test_breadth_first_returns_generator(bst1):
    """Test breadth first traversal returns a generator."""
    assert isinstance(bst1.breadth_first(bst1.root), types.GeneratorType)


def test_in_order_bst1(bst1):
    """Test in order traversal returns nodes in order."""
    assert [n for n in bst1.in_order()] == [1, 2, 3, 4, 5, 8, 9, 11, 12]


def test_in_order_bst2(bst2):
    """Test in order traversal returns nodes in order."""
    assert [n for n in bst2.in_order()] == [4, 5, 6, 8, 11, 12, 17, 19, 31, 43, 49]


def test_pre_order_bst1(bst1):
    """Test pre order traversal does a depth first traversal."""
    assert [n for n in bst1.pre_order()] == [2, 1, 3, 5, 4, 9, 8, 12, 11]


def test_pre_order_bst2(bst2):
    """Test pre order traversal does a depth first traversal on complex bst."""
    assert [n for n in bst2.pre_order()] == [11, 6, 4, 5, 8, 19, 12, 17, 43, 31, 49]


def test_post_order_bst1(bst1):
    """Test post order traversal returns correct order."""
    assert [n for n in bst1.post_order()] == [1, 4, 8, 11, 12, 9, 5, 3, 2]


def test_post_order_bst2(bst2):
    """Test post order on more complex bst."""
    assert [n for n in bst2.post_order()] == [5, 4, 8, 6, 17, 12, 31, 49, 43, 19, 11]


def test_breadth_first_bst1(bst1):
    """Test breadth first traversal of bst."""
    assert [n for n in bst1.breadth_first(bst1.root)] == [2, 1, 3, 5, 4, 9, 8, 12, 11]
    assert len([n for n in bst1.breadth_first(bst1.root)]) == bst1.size()

def test_breadth_first_bst2(bst2):
    """Test breadth first traversal of bst."""
    assert [n for n in bst2.breadth_first(bst2.root)] == [11, 6, 19, 4, 8, 12, 43, 5, 17, 31, 49]
