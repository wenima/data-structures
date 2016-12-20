"""Tests for binheap data structure."""

import pytest

TEST_TABLE = [
    (5, [0, 5, 20, 10]),
    (8, [5, 10, 30, 20, 50, 60, 70, 40]),
]

TEST_ITER = [10, 20, 5]

TEST_ITER_MANY = [10, 20, 30, 40, 50, 60, 70, 5]


@pytest.fixture
def heap():
    """Prebuilt heap."""
    from binheap import Binheap
    heap = Binheap(TEST_ITER)
    return heap


@pytest.fixture
def heap_many():
    """Prebuilt heap with multiple values."""
    from binheap import Binheap
    heap = Binheap(TEST_ITER_MANY)
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
    assert heap._raise_up(3) == [0, 5, 20, 10]


def test_raise_up_multiple_rows(heap_many):
    """Test that raise up works across multiple rows of the heap."""
    assert heap_many._raise_up(8) == [0, 5, 10, 30, 20, 50, 60, 70, 40]


def test_raise_up_not_to_top():
    """Test that raise up works across multiple rows of the heap."""
    from binheap import Binheap
    heap = Binheap([10, 20, 30, 40, 50, 60, 70, 15])
    assert heap._raise_up(8) == [0, 10, 15, 30, 20, 50, 60, 70, 40]


def test_pop_removes_and_returns_top_value(heap_many):
    """Test that pop removes top value and returns it."""
    assert heap_many.pop() == 10
    assert heap_many._heap[1] == 5
