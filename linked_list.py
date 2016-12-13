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
        val = self.head.value
        self.head = self.head.nxt
        self.length -= 1

        return val


    def search(self, query):
        """Return the node that contains the value."""
        cur_node = self.head
        while True:
            if cur_node.value == query:
                return cur_node
            elif cur_node == self.tail:
                print("Value is not in this linked list.")
                break
            else:
                cur_node = cur_node.nxt


    def remove(self, node):
        """Remove the given node from the LL."""


    def display(self):
        """Return a unicode string representing the Linked List as a tuple."""
        cur_node = self.head
        out_str = "("
        for i in range(self.length):
            out_str += str(cur_node.value) + ', '
            cur_node = cur_node.nxt

        return out_str + ')'


def init_node():
    node = Node(0)
    return str(type(node))


def create_ll():
    values = ["something", "something else", "two"]
    new_ll = Linked_List()
    for value in values:
        new_ll.push(value)

    return new_ll