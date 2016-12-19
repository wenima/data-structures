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


@pytest.fixture
def deq_three(deq_two):
    """Fixture for deque of three."""
    deq_two.append(3)
    return deq_two

# Tests for append


def test_that_deque_is_empty(deq_empty):
    """Test that after initialization a deque is empty."""
    assert deq_empty._container.head is None
    assert deq_empty.size() == 0


def test_append_to_empty_deque(deq_empty):
    """Test append to empty list leaves head and tail pointing to new node."""
    deq_empty.append(1)
    assert deq_empty._container.head.value == 1
    assert deq_empty._container.tail.value == 1
    assert deq_empty.size() == 1


def test_append_to_deque_of_one(deq_one):
    """Test that append to a deque of 1 adds to the tail."""
    deq_one.append(2)
    assert deq_one._container.head.value == 1
    assert deq_one._container.tail.value == 2
    assert deq_one.size() == 2


def test_append_to_deque_of_two(deq_two):
    """Test that you can append to a list of 2."""
    deq_two.append(3)
    assert deq_two._container.head.value == 1
    assert deq_two._container.tail.value == 3
    assert deq_two.size() == 3

# Tests for pop()


def test_pop_from_empty_deque(deq_empty):
    """Test that you cannot pop from an empty deque."""
    with pytest.raises(IndexError):
        deq_empty.pop()


def test_pop_from_deque_of_one(deq_one):
    """Test that popping from list of one returns head and tail to none."""
    deq_one.pop()
    assert deq_one._container.head is None
    assert deq_one._container.tail is None
    assert deq_one.size() == 0


def test_pop_from_deque_of_two(deq_two):
    """Test that popping from a deque of two leaves one element."""
    deq_two.pop()
    assert deq_two._container.tail.value == 1
    assert deq_two._container.head.value == 1
    assert deq_two.size() == 1


def test_pop_from_deque_of_three(deq_three):
    """Test that popping from a deque of three removes the tail element."""
    deq_three.pop()
    assert deq_three._container.tail.value == 2
    assert deq_three._container.head.value == 1
    assert deq_three.size() == 2


# Tests for peek()

def test_peek_at_an_empty_deque(deq_empty):
    """Test that peek of an emty queue returns None."""
    assert deq_empty.peek() is None


def test_peek_at_deque_of_one(deq_one):
    """Test that peeking at deque of one returns value and leaves node."""
    assert deq_one.peek() == 1
    assert deq_one._container.head.value == 1
    assert deq_one.size() == 1


def test_peek_at_deque_of_two(deq_two):
    """Test that peek actually looks at the tail element of the deque."""
    assert deq_two.peek() == 2
    assert deq_two.size() == 2


# Tests for size()

def test_size_of_empty_deque(deq_empty):
    """Test that an empty deque has a size of zero."""
    assert deq_empty.size() == 0
