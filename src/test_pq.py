"""Test dbl_linked_list data structures."""

import pytest

ROUTINES = [
    ("get_up", 1),
    ("make_coffee", 2),
    ("shower", 3),
    ("shave", 4),
    ("get_dressed", 5),
    ("walk_the_dog", 6),
    ("make_breakfast", 7),
    ("read_newspaper", 8),
    ("commute", 9),
]


@pytest.fixture
def pq_empty():
    """Fixture for empty pq."""
    from priorityq import PriorityQueue
    new_pq = PriorityQueue()
    return new_pq


@pytest.fixture
def pq():
    """Fixture for pq filled with ROUTINES."""
    from priorityq import PriorityQueue
    new_pq = PriorityQueue(ROUTINES)
    return new_pq


def test_create_empty_pq(pq_empty):
    """Test creation of empty PriorityQueue."""
    assert pq_empty._binheap._heap[0] == 0
    assert len(pq_empty) == 0


def test_create_priority_queue_with_one_value():
    """Test that a PriorityQueue cannot be created with one value and throws an error."""
    from priorityq import PriorityQueue
    with pytest.raises(TypeError):
        PriorityQueue(ROUTINES[-1])


def test_that_popping_and_peeking_gives_an_error_message(pq_empty):
    """Test that popping and peeking on a queue with 1 element is None."""
    pq_empty.insert(("sleep", 1))
    pq_empty.pop()
    assert pq_empty.peek() is None


def test_that_popping_on_an_empty_queue_raises_an_error(pq_empty):
    """Test that popping on an empty queue raises an exception."""
    with pytest.raises(IndexError):
        pq_empty.pop()


def test_peek_returns_item_of_highest_prio(pq):
    """Test that peek returns item of highest prio but keeps it in the list."""
    assert pq.peek() == ROUTINES[0][0]
    assert ROUTINES[0][0] in pq._binheap._heap[1]


def test_pop_from_pq_returns_top_prio_item_and_removes_from_heap(pq):
    """Test that popping from PriorityQueue returns the item with the highest prio and remove it from the queue."""
    cur_len = len(pq)
    assert ROUTINES[0][0] in pq.pop()
    assert ROUTINES[1][0] in pq._binheap._heap[1]
    assert len(pq) == cur_len - 1


def test_that_items_are_returned_in_correct_order(pq):
    """Test that items are returned in the correct order."""
    cur_len = len(pq)
    pq.insert(("wake_kids", 5))
    pq.insert(("check_critical_news", 1))
    pq.insert(("check_emails", 10))
    assert ROUTINES[0][0] in pq.pop()
    assert "check_critical_news" in pq.pop()
    assert "check_emails" in pq._binheap._heap[8]
    assert "wake_kids" in pq._binheap._heap[-1]
    assert len(pq) == cur_len + 1
