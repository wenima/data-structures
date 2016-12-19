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

"""APPENDLEFT specific Test"""

def test_appendleft_empty_list(deq_empty):
    """Test appendlefted val is new head and tail."""
    deq_empty.appendleft(5)
    assert deq_empty._container.head.value == 5
    assert deq_empty._container.tail.value == 5


def test_appendleft_empty_list_new_head_tail(deq_empty):
    """Test that appendleft on an empty list results in a new head, tail."""
    deq_empty.appendleft(5)
    assert deq_empty._container.head is deq_empty._container.tail
    assert deq_empty._container.head.nxt is None
    assert deq_empty._container.head.prev is None


def test_appendleft_assigns_new_head(deq_empty):
    """Test new head assigned."""
    deq_empty.appendleft(6)
    assert deq_empty._container.head.value == 6


def test_appendleft_reassigns_prev_nxt(deq_two):
    """Test that appendlefting to a full list correctly assigns prev, nxt."""
    old_head = deq_two._container.head
    deq_two.appendleft(6)
    assert deq_two._container.head.nxt.value == old_head.value
    assert deq_two._container.head.nxt.prev is deq_two._container.head
