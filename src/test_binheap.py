"""Tests for binheap data structure."""

import pytest


@pytest.fixture
def empty_heap():
    """Empty heap."""
    from binheap import Binheap
    heap = Binheap()
    return heap


def one_heap(empty_heap):
    """Heap of one."""
    empty_heap.push(10)
    return empty_heap


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


def test_add_smaller_value_that_raises(one_heap):
    """Test that adding to a list with a larger value it gets added to the end."""
    one_heap.push(5)
    assert one_heap._heap == [0, 5, 10]
