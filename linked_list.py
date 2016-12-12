"""Creating a Linked List Data Structure.  CF 401 Python Week 2 assignment."""


class Node(object):
    """Create Node objects for use in a Linked List data structure."""
    def __init__(self, value, nxt=None):
        self.value = value
        self.nxt = nxt


class Linked_List(object):
    """Create a Linked List Data Structure."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def push(self, value):
        """Add a node."""
        self.head = Node(value, self.head)
        if self.tail is None:
            self.tail = self.head

        self.length += 1


    def size(self):
        """Return the length of the Linked_List."""
        return self.length


    def pop(self):
        """Pop the first value off the head of LL and return it."""


    def search(self, value):
        """Return the node that contains the value."""


    def remove(node):
        """Remove the given node from the LL."""


    def display():
        """Return a unicode string representing the Linked List as a tuple."""

def init_node():
    node = Node(0)
    return str(type(node))


def create_ll():
    values = ["something", "something else", "two"]
    new_ll = Linked_List()
    for value in values:
        new_ll.push(value)

    return new_ll