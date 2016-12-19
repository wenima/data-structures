"""This module defines Queue Data Structure.

A Queue works based on the FIFO principle which is based in accounting and it
describes the method of the first item/person/inventory to enter something
to also be the first to leave it.

An example would be a line in a bank where the first customer in the line will
be the first one served and thus the first to exit the bank."""

from dbl_linked_list import DblLinkedList


class Deque(object):

    """The Queue Data structure is a compoisition of a Double Linked List.

    Methods:

            append(val):  Add a new node to the end (tail) of the queue.

            appendleft(val) (was push()): adds a value to the front of the deque

            pop() (was shift): removes a value from the end of the deque and returns it (raises an exception if the deque is empty)

            popleft (was pop): removes a value from the front of the deque and returns it (raises an exception if the deque is empty)

            peek() (aka reverse peek): returns the next value that would be returned by pop but leaves the value in the deque (returns None if the deque is empty)

            peekleft(): returns the next value that would be returned by popleft but leaves the value in the deque (returns None if the deque is empty)

            size(): Return size of queue.

    """

    def __init__(self, maybe_an_iterable=None):
        """Initialize Queue as a DblLinkedList-esque object."""
        try:
            self._container = DblLinkedList(maybe_an_iterable[::-1])
        except TypeError:
            self._container = DblLinkedList(maybe_an_iterable)

    def append(self, value):
        """Add a new node with given value to the end (tail) of the deque."""
        self._container.append(value)

    def appendleft(self, value):
        """Add a new node with a given value to the beginning (head) of the deque"""
        self._container.push(value)

    def pop(self, value):
        """removes a value from the end of the deque and returns it (raises an exception if the deque is empty)"""
        self._container.shift()

    def popleft(self, value):
        """removes a value from the front of the deque and returns it (raises an exception if the deque is empty)"""
        self._container.pop()

    def peek(self):
        """(aka reverse peek): returns the next value that would be returned by pop but leaves the value in the deque (returns None if the deque is empty)"""
        try:
            return self._container.tail.value
        except AttributeError:
            return None

    def peekleft(self):
        """(aka reverse peek): returns the next value that would be returned by pop but leaves the value in the deque (returns None if the deque is empty)"""
        try:
            return self._container.head.value
        except AttributeError:
            return None

    def size(self):
        """Return the size of the queue."""
        return self._container._size

    def __len__(self):
        """Allow use of len() function."""
        return self.size()
