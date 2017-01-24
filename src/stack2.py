"""Module with implementation of stack data structure."""
from ll import LinkedList


class Stack(object):
    """Stack data structure class."""

    def __init__(self, iterable=None):
        """Stack constructor."""
        self._linkedlist = LinkedList(iterable)
        self._update_attr()

    def push(self, val):
        """Add value to top of stack."""
        self._linkedlist.push(val)
        self._update_attr()

    def pop(self):
        """Remove and return top of stack."""
        try:
            res = self._linkedlist.pop()
            self._update_attr()
            return res
        except IndexError:
            raise IndexError("Cannot pop from empty stack.")

    def size(self):
        """Return size of stack."""
        return self._linkedlist.size()

    def __len__(self):
        """Return size of stack with len builtin."""
        return self.size()

    def _update_attr(self):
        self.top = self._linkedlist.head
