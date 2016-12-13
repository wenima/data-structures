"""Creating a Linked List Data Structure.  CF 401 Python Week 2 assignment."""


class Node(object):
    """Create Node objects for use in a Linked List data structure."""
    def __init__(self, value=None, nxt=None):
        self.value = value
        self.nxt = nxt


class Linked_List(object):
    """Create a Linked List Data Structure."""
    def __init__(self, iterable=None):
        """Intialize a Linked List Object."""
        self.head = None
        self._size = 0
        if iterable and hasattr(iterable, "__iter__"):
            for value in iterable:
                self.push(value)
        elif iterable:
            raise TypeError

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
        return match[0] if match else "That value is not in this linked list."

    def remove(self, r_node):
        """Remove the given node from the LL."""
        cur_node = self.head
        if self.head is r_node:
            self.head = self.head.nxt
            self._size -= 1
            return "Succesfully removed Node with value: \
            {0}. New head set to {1}".format(r_node.value, self.head.value)
        while cur_node:
            if r_node == cur_node.nxt:
                cur_node.nxt = cur_node.nxt.nxt
                self._size -= 1
                return "Succesfully removed Node with value: {}".format(r_node.value)
            else:
                cur_node = cur_node.nxt
        else:
            print("ERROR: That node is not in this linked list.")
            return r_node

    def display(self):
        """Return a unicode string representing the Linked List as a tuple."""
        return str(tuple(self._node_values()))

    def __len__(self):
        """Enable use of len() function."""
        return self._size()

    def _iterate_from(self, list_item):
        while list_item is not None:
            yield list_item
            list_item = list_item.nxt

    def _node_values(self):
        """Helper function to return an iterable of node values"""
        node_values = [node.value for node in self._iterate_from(self.head)]
        return node_values



def init_node():
    node = Node(0)
    return str(type(node))


def create_ll():
    values = ["something", "something else", "two"]
    new_ll = Linked_List()
    for value in values:
        new_ll.push(value)
    return new_ll

