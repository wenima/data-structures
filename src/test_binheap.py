"""Tests for binheap data structure."""

import pytest

@pytest.fixture
def empty_heap():
    from binheap import Binheap
    heap = Binheap()
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
