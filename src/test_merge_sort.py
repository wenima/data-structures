"""Tests for merge sort implementation."""

import pytest

TESTS = [
    ([5, 9, 1, 4, 6, 7, 3, 2, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
]

@pytest.mark.parametrize('l , result', TESTS)
def test_merge_sort(l, result):
    """Test that merge sort returns a sorted list."""
    from merge_sort import merge_sort
    assert merge_sort(l) == result
