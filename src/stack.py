"""This module defines the Stack data structure."""

from linked_list import Linked_List


class Stack(object):
    """This class defines a stack data structure.

    The stack will store and return values based on Last-In-First-Out.

    Methods:
        push(val):     Given a value, push a new node onto the stack.
        pop():         Pop the first item off the stack and return the value.

    """
    def __init__(self, iterable=None):
        """Initialize stack as a Linked_List-esque object."""
        self._container = Linked_List(iterable)

    def push(self, val):
        """Given a value, push a new node onto the stack."""
        self._container.push(val)

    def pop(self):
        """Remove first item of stack and return value."""
        try:
            return self._container.pop()
        except IndexError:
            raise IndexError("Cannot pop from empty stack.")


