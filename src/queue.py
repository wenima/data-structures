"""This module defines Queue Data Structure."""

from dbl_linked_list import Dbl_Linked_List


class Queue(object):
    """The Queue Data structure is a compoisition of a Double Linked List.
    
    The Queue method is composed from the Dbl

    """

    def __init__(self, maybe_an_iterable=None):
        """Initialize Queue as a Dbl_Linked_List-esque object."""
        if type(maybe_an_iterable) not in (list, tuple):
            self._container = Dbl_Linked_List(maybe_an_iterable)
        else:
            self._container = Dbl_Linked_List(reversed(maybe_an_iterable))

    def enqueue(self, value):
        """Add a new node with given value to the end (tail) of the queue."""
        self._container.append(value)

    def dequeue(self):
        """Remove the node at the head of the queue and return the value."""
        self._container.pop()

    def peek(self):
        """Return the value at the head of the queue.  None if empty."""
        return self._container.head.value

    def size(self):
        """Return the size of the queue."""
        return self._container._size

    def __len__(self):
        """Allow use of len() function."""
        return self.size()
