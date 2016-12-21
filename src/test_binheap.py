"""Tests for binheap data structure."""

import pytest


"""The test dict below contains a list of lists that are used for varying tests throughout this module.  The commented line above each list is the reason for the list followed by the index of that list."""
TEST_DICT = [
    # raise to top - 0
    ([10, 20, 5]),
    # raise all the way to the top - 1
    ([10, 20, 30, 40, 50, 60, 70, 5]),
    # raise part way - 2
    ([10, 20, 30, 40, 50, 60, 70, 15]),
    # sink down - 3
    ([30, 10, 20]),
    # sink way down - 4
    ([80, 10, 20, 30, 40, 50, 60, 70]),
    # sink part way - 5
    ([55, 10, 20, 30, 40, 50, 60, 70]),
    # well formed- 6
    ([5, 10, 20, 25, 30, 35, 40, 55, 60]),
    # child on right is smaller for sink - 7
    ([10, 5, 3]),


]


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


def test_cannot_init_with_non_iterable():
    from binheap import Binheap
    with pytest.raises(TypeError):
        Binheap(8)


def test_add_to_empty_binheap(empty_heap):
    """Test that adding to empty heap adds to list."""
    empty_heap.push(10)
    assert empty_heap._heap == [0, 10]


def test_add_larger_value_that_remains(one_heap):
    """Test that adding to a list with a larger value it gets added to the end."""
    one_heap.push(20)
    assert one_heap._heap == [0, 10, 20]


def test_add_smaller_value_that_raises():
    """Test that a heap with the smallest number at the end raises to the top."""
    from binheap import Binheap
    heap = Binheap(TEST_DICT[0])
    assert heap._raise_up(3) == [0, 5, 20, 10]


def test_raise_up_multiple_rows():
    """Test that raise up works across multiple rows of the heap."""
    from binheap import Binheap
    heap = Binheap(TEST_DICT[1])
    assert heap._raise_up(8) == [0, 5, 10, 30, 20, 50, 60, 70, 40]


def test_raise_up_not_to_top():
    """Test that raise up works across multiple rows of the heap."""
    from binheap import Binheap
    heap = Binheap(TEST_DICT[2])
    assert heap._raise_up(8) == [0, 10, 15, 30, 20, 50, 60, 70, 40]


def test_pop_removes_and_returns_top_value():
    """Test that pop removes top value and returns it."""
    from binheap import Binheap
    heap = Binheap(TEST_DICT[6])
    assert heap.pop() == 5
    assert heap._heap[1] == 60


def test_pop_from_empty_heap_raises_index_error(empty_heap):
    """Test that popping form an empty heap returns a index error."""
    with pytest.raises(IndexError):
        empty_heap.pop()


def test_sink_to_bottom():
    """Test that the larger numbers sink down the tree of small tree."""
    from binheap import Binheap
    heap = Binheap(TEST_DICT[3])
    assert heap._sink_down(1) == [0, 10, 30, 20]


def test_sink_all_the_way_to_bottom():
    """Test that the larger numbers sink down the tree of large tree."""
    from binheap import Binheap
    heap = Binheap(TEST_DICT[4])
    assert heap._sink_down(1) == [0, 10, 30, 20, 70, 40, 50, 60, 80]


def test_sink_part_way_to_bottom():
    """Test that the larger numbers sink down the tree part way."""
    from binheap import Binheap
    heap = Binheap(TEST_DICT[5])
    assert heap._sink_down(1) == [0, 10, 30, 20, 55, 40, 50, 60, 70]


def test_sink_to_the_right():
    """Test that sinking to the right works."""
    from binheap import Binheap
    heap = Binheap(TEST_DICT[7])
    assert heap._sink_down(1) == [0, 3, 5, 10]
