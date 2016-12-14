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
        self.tail = None
        self._size = 0
        if maybe_an_iterable:
            try:
                for value in maybe_an_iterable:
                    self.push(value)
                self.tail = maybe_an_iterable[-1]
            except TypeError:
                self.push(maybe_an_iterable)
                self.tail = maybe_an_iterable[-1] #make dry

    def push(self, value):
        """Add a node."""
        self.head = Dbl_Node(value, self.head)
        self._size += 1
        if self._size == 1:
            print(self.head)
            self.tail = self.head
        else:
            nodes = [node for node in self._iterate_from(self.head)]
            self.tail = nodes[-1]
            nodes[-1].prev = self.head

    def _iterate_from(self, list_item):
        while list_item is not None:
            yield list_item
            list_item = list_item.nxt
