"""Creating a Linked List Data Structure.  CF 401 Python Week 2 assignment."""


class Node(object):
    """Create Node objects for use in a Linked List data structure.

    Attributes:
    value:      A value stored in the Node.
    nxt:        Pointer to the next Node, used in a Linked List or Stack
                data structure.
    """
    def __init__(self, value=None, nxt=None):
        """Initialize a Node type object."""
        self.value = value
        self.nxt = nxt


class Linked_List(object):
    """Create a Linked List Data Structure.

    Attributes:
    head:       Always the most recent item added to a Linked List.
    _size:      The length of the Linked List or number of Nodes stored
                in the list.

    push(value):    Given a value, add a new Node object to a Linked List.

    size():         Return _size of the Linked List.

    pop():          Pop the head Node off the list, return the value.

    search():       Given a Node value to search by, return the Node from the
                    Linked List containing that value.  Else, return None.

    remove():       Given a Node, remove that Node from the Linked List.  Else,
                    raise a ValueError.

    display():      Return a string of all Nodes in the Linked List,
                    formatted as a Tuple.
    """
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

    def remove(self, r_node):
        """Remove the given node from the LL."""
        for node in self._iterate_from(self.head):
            if r_node.value == node.value:
                if self.head.value == r_node.value:
                    self.pop()
                    return "Succesfully removed Node with value: \
                    {0}. New head set to {1}".format(r_node.value, self.head.value)
                node.nxt = node.nxt.nxt
                self._size -= 1
                return "Succesfully removed Node with value: {}".format(r_node.value)
        raise ValueError("ERROR: That node is not in this linked list.")

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
        """Helper function to return an iterable of node values."""
        node_values = [node.value for node in self._iterate_from(self.head)]
        return node_values
