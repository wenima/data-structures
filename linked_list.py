"""Creating a Linked List Data Structure.  CF 401 Python Week 2 assignment."""


class Node(object):
    """Create Node objects for use in a Linked List data structure."""
    def __init__(self, value, nxt=None):
        self.value = value
        self.nxt = None

def init_node():
    node = Node(0)
    return str(type(node))

class Linked_List(object):
    """Create a Linked List Data Structure."""
    def __init__():
        self.head = None
        self.tail = None
        self.length = 0


    def add(self, value):
        """Add a node"""
        node = Node(value, self.head)