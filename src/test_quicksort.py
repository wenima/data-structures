"""Tests for insertion sort implementation."""

import pytest

arr = [9, 7, 5, 11, 11, 12, 2, 14, 3, 10, 6]

TESTS = [
    (arr, 0, len(arr) - 1, [2, 3, 5, 6, 7, 9, 10, 11, 11, 12, 14]),
]

@pytest.mark.parametrize('l, s, e, result', TESTS)
def test_quicksort(l, s, e, result):
    """Test that quick sort returns a sorted list."""
    from quicksort import quicksort
    assert quicksort(l, s, e) == result
