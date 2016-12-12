"""Creating a Linked List Data Structure.  CF 401 Python Week 2 assignment."""


class Node(object):
    """Create Node objects for use in a Linked List data structure."""
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def print_backward(self):
        if self.next != None:
            tail = self.next
            tail.print_backward()
        print self.value,

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head   = None

    def print_backward(self):
        print "[",
        if self.head != None:
            self.head.print_backward()
        print "]",

    def addFirst(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length = self.length + 1


def init_node():
    node = Node('test')
    print(node)
