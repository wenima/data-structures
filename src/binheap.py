"""Implementation of the binheap data structure.

A binary heap is defined as a binary tree with two additional constraints:

Shape property: a binary heap is a complete binary tree; that is, all levels of the tree, except possibly the last one (deepest) are fully filled, and, if the last level of the tree is not complete, the nodes of that level are filled from left to right.
Heap property: the key stored in each node is either greater than or equal to or less than or equal to the keys in the node's children, according to some total order.

Taken from: https://en.wikipedia.org/wiki/Binary_heap
"""


class Binheap(object):
    """Create a binary heap tree structure."""

    def __init__(self, maybe_an_iterable=None):
        """Initialize an instance of the binheap."""
        self._heap = [0]
        self._size = 0
        if maybe_an_iterable:
            try:
                for value in maybe_an_iterable:
                    value + 0
                    self._heap.append(value)
            except TypeError:
                return "Only an iterable of integers is an accepted input"
            for item in reversed(maybe_an_iterable):
                self._raise_up(self._heap[1:].index(item) + 1)
        self._size = len(self._heap) - 1


    def push(self, value):
        """Push a new value to the heap."""
        self._heap.append(value)
        self._raise_up(len(self._heap) - 1)
        self._size += 1

    def pop(self):
        """Remove the root node from the tree."""
        if self._size == 0:
            raise IndexError("You can't remove the head of an empty binary heap")
        root = self._heap[1]
        self._heap[1] = self._heap[-1]
        del self._heap[-1]
        self._size -= 1
        self._sink_down(1)
        return root

    def _raise_up(self, i):
        """Raise i into the tree until the tree structure is satisfied."""
        while i // 2 > 0:
            if self._heap[i] < self._heap[i // 2]:
                self._heap[i], self._heap[i // 2] = self._heap[i // 2], self._heap[i]
            i = i // 2
        return self._heap

    def _sink_down(self, i):
        """Sink the input node down the tree until the tree structure is satisfied."""
        if self._size != 0:
            parent = self._heap[i]
            while i * 2 < len(self._heap):
                child = self._heap[self._get_min_child(i)]
                idx_child = self._get_min_child(i)
                if parent > child:
                    self._heap[i], self._heap[idx_child] = self._heap[idx_child], self._heap[i]
                parent = self._heap[idx_child]
                i = idx_child
            return self._heap
        return self._heap

    def _get_min_child(self, i):
        """Determine the smaller of two children."""
        if i * 2 == self._size:
            return i * 2
        if self._heap[i * 2] > self._heap[i * 2 + 1]:
            return i * 2 + 1
        else:
            return i * 2
