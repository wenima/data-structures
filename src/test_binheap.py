"""Tests for binheap data structure."""

import pytest

TEST_ITER = [10, 20, 5]


@pytest.fixture
def heap():
    """Prebuilt heap."""
    from binheap import Binheap
    heap = Binheap(TEST_ITER)
    return heap


@pytest.fixture
def empty_heap():
    """Empty heap."""
    from binheap import Binheap
    heap = Binheap()
    return heap


@pytest.fixture
def one_heap():
    """One heap."""
    from binheap import Binheap
    heap = Binheap()
    heap.push(10)
    return heap


def test_binheap_is_initialized():
    """Vaidate the initializationof a binheap."""
    from binheap import Binheap
    heap = Binheap()
    assert heap._heap[0] == 0
    assert heap._size == 0


def test_add_to_empty_binheap(empty_heap):
    """Test that adding to empty heap adds to list."""
    empty_heap.push(10)
    assert empty_heap._heap == [0, 10]


def test_add_larger_value_that_remains(one_heap):
    """Test that adding to a list with a larger value it gets added to the end."""
    one_heap.push(20)
    assert one_heap._heap == [0, 10, 20]


def test_add_smaller_value_that_raises(heap):
    """Test that a heap with the smallest number at the end raises to the top."""
    heap._raise_up(5)
    assert heap._heap == [0, 5, 10, 20]
