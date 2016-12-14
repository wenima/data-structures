"""Creating a Linked List Data Structure.  CF 401 Python Week 2 assignment."""


class Node(object):
    """Create Node objects for use in a Linked List data structure."""
    def __init__(self, value=None, nxt=None):
        self.value = value
        self.nxt = nxt


class Linked_List(object):
    """Create a Linked List Data Structure."""
    def __init__(self, maybe_an_iterable=None):
        """Intialize a Linked List Object."""
        self.head = None
        self._size = 0
        if maybe_an_iterable:
            try:
                for value in maybe_an_iterable:
                    self.push(value)
            except TypeError:
                self.push(maybe_an_iterable)

    def push(self, value):
        """Add a node."""
        self.head = Node(value, self.head)
        self._size += 1

    def size(self):
        """Return the length of the Linked_List."""
        return self._size

    def pop(self):
        """Pop the first value off the head of LL and return it."""
        if self.head is None:
            raise IndexError("Cannot pop from an empty Linked List.")
        val = self.head.value
        self.head = self.head.nxt
        self._size -= 1
        return val

    def search(self, query):
        """Return the node that contains the value."""
        match = [node for node in self._iterate_from(self.head) if node.value == query]
        return match[0] if match else None

    def remove(self, value):
        """Remove the given node from the LL."""
        r_node = self.search(value)
        if r_node is None:
            raise ValueError("ERROR: That node is not in this linked list.")
        for node in self._iterate_from(self.head):
            if r_node.value == node.value:
                if self.head.value == r_node.value:
                    self.pop()
                    return "Succesfully removed Node with value: {0}. New head set to {1}".format(r_node.value, self.head.value)
                else:
                    node.nxt = node.nxt.nxt
                    self._size -= 1
                    return "Succesfully removed Node with value: {}".format(r_node.value)
            else:
                if node.nxt.nxt is None:
                    if node.nxt == r_node:
                        node.nxt = None
                        self._size -= 1
                        return "Succesfully removed Node with value: {}".format(r_node.value)


    def display(self):
        """Return a unicode string representing the Linked List as a tuple."""
        return str(tuple(self._node_values()))

    def __len__(self):
        """Enable use of len() function."""
        return self.size()

    def _iterate_from(self, list_item):
        while list_item is not None:
            yield list_item
            list_item = list_item.nxt

    def _node_values(self):
        """Helper function to return an iterable of node values"""
        node_values = [node.value for node in self._iterate_from(self.head)]
        return node_values
