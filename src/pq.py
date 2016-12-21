"""Implentation of the priority queue."""

from binheap import Binheap


class PriorityQueue(object):
    """A priority queue.

    An item in the priority list is a tuple with the object at index 0 being the item or data being held and the integer in index 1 is the priority of the item.

    insert(item) - insert an item into the priority queue.

    pop() remove the item with the highest priority and return its item.

    peek() view the item of the next object in the priority queue.


    """

    def __init__(self):
        """Initialize a Priority Queue with an underlying binary heap data structure."""
        self._heap = Binheap()

    def insert(self, item):
        """Insert an item into the priority queue and order it by priority."""
        self._heap.push(item)

    def pop(self):
        """Remove the top item from return its item."""
        return self._heap.pop()

    def peek(self):
        """Look at the item that is next on the priority queue."""
        return self._heap._heap[1]
