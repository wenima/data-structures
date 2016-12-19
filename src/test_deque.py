"""Tests for deque data structure."""

import pytest


@pytest.fixture
def deq_empty():
    """Fixture for empty deque."""
    from deque import Deque
    deque = Deque()
    return deque


@pytest.fixture
def deq_one(deq_empty):
    """Fixture for deque of one."""
    deq_empty.append(1)
    return deq_empty


@pytest.fixture
def deq_two(deq_one):
    """Fixture for deque of one."""
    deq_one.append(2)
    return deq_one


def test_that_deque_is_empty(deq_empty):
    """Test that after initialization a deque is empty."""
    assert deq_empty._container.head is None


def test_append_to_empty_deque(deq_empty):
    """Test append to empty list leaves head and tail pointing to new node."""
    deq_empty.append(1)
    assert deq_empty._container.head.value == 1
    assert deq_empty._container.tail.value == 1


def test_append_to_deque_of_one(deq_one):
    """Test that you can append to a list of 1."""
    deq_one.append(2)
    assert deq_one._container.head.value == 1
    assert deq_one._container.tail.value == 2


def test_append_to_deque_of_two(deq_two):
    """Test that you can append to a list of 2."""
    deq_two.append(3)
    assert deq_two._container.head.value == 1
    assert deq_two._container.tail.value == 3


