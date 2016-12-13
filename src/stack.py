"""This module defines the Stack data structure."""

from linked_list import Linked_List


class Stack(object):
    """The stack data structure is a composition of the Linked List structure."""
    def __init__(self, iterable=None):
        """Initialize stack as a Linked_List-esque object."""
        self._container = Linked_List(iterable)

    def push(self, val):
        """Use Linked List push method to add one Node to stack."""
        self._container.push(val)

    def pop(self):
        """Use Linked List pop() method to remove one from stack."""
        return self._container.pop()
