"""Create a Double Linked List Data Structure."""


class Dbl_Node(object):
    """Create Node objects for use in a Linked List data structure.

    Attributes:
    value:      A value stored in the Node.
    nxt:        Pointer to the next Node, used in a Linked List or Stack
                data structure.
    """
    def __init__(self, value=None, nxt=None, prev=None):
        """Initialize a Node type object."""
        self.value = value
        self.nxt = nxt
        self.prev = prev


class Dbl_Linked_List(object):
    """Double Linked List style Data Structure

        Attributes:
        head:       Always the most recent item added to a Linked List.
        _size:      The length of the Linked List or number of Nodes stored
                    in the list.

        Methods:

        push(value):    Given a value, add a new Node object to a Linked List.

        append(value):  Given a value, adds it at the end of the line.

        pop():          Pop the head Node off the list, return the value.

        shift():        will remove the last value from the line and return it.

        remove(val):    Given a Node, remove that Node from the Linked List.  Else,
                        raise a ValueError.
        """

    def __init__(self, maybe_an_iterable=None):
        """Intialize a doubly linked List Object."""
        self.head = None
        self.tail = None
        self._size = 0
        if maybe_an_iterable:
            try:
                for value in maybe_an_iterable:
                    self.push(value)
                nodes = [node for node in self._iterate_from(self.head)]
                self.tail = nodes[-1]
            except TypeError:
                self.push(maybe_an_iterable)

    def push(self, value):
        """Add a node at the beginning of the line."""
        self.head = Dbl_Node(value, self.head)
        self._size += 1
        if self._size == 1:
            self.tail = self.head
        elif self._size == 2:
            nodes = [node for node in self._iterate_from(self.head)]
            self.tail = nodes[-1]
            nodes[-1].prev = self.head
        else:
            self.head.nxt.prev = self.head

    def pop(self):
        """Pop the first value off the head of LL and return it."""
        if self.head is None:
            raise IndexError("Cannot pop from an empty Linked List.")
        val = self.head.value
        self.head = self.head.nxt
        self.head.prev = None
        self._size -= 1
        return val

    def shift(self):
        """will remove the last value from the tail of the list and return it."""
        if self.tail is None:
            raise IndexError("Cannot shift (remove the last node in the line) from an empty Linked List.")
        val = self.tail.value
        self.tail.prev.nxt = None
        self.tail = self.tail.prev
        self._size -= 1
        return val

    def append(self, value):
        """will append a new node at the end of the line and will set the new tail to be this node."""
        new_node = Dbl_Node(value, None, self.tail)
        nodes = [node for node in self._iterate_from(self.head)]
        if nodes:
            self.tail = new_node
            nodes[-1].nxt = self.tail
            self._size += 1
        else:
            self.head = new_node
            self.tail = new_node
            self._size += 1

    def remove(self, value):
        """Remove the given node from the LL."""
        nodes = [node for node in self._iterate_from(self.head)]
        r_node = [node for node in self._iterate_from(self.head) if node.value == value]
        if not r_node:
            raise ValueError("ERROR: That node is not in this linked list.")
        for node in self._iterate_from(self.head):
            if r_node[0].value == node.value:
                if self.head.value == r_node[0].value:
                    self.pop()
                    return "Succesfully removed Node with value: {0}. New head set to {1}".format(r_node[0].value, self.head.value)
                elif node.nxt is None:
                    self.shift()
                    return "Succesfully removed Node with value: {} using Shift()".format(r_node[0].value)
                else:
                    r_node[0].prev.nxt = r_node[0].nxt
                    r_node[0].nxt.prev = r_node[0].prev
                    self._size -= 1
                    return "Succesfully removed Node with value: {}".format(r_node[0].value)

    def _iterate_from(self, list_item):
        """return a generator"""
        while list_item is not None:
            yield list_item
            list_item = list_item.nxt
