"""Module to implement a Binary Search Tree."""
from queue import Queue
import sys


class TreeNode(object):
    """TreeNode is the root of the tree."""

    def __init__(self, val, left=None, right=None, parent=None):
        """."""
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def children(self):
        """Return non-none children of node."""
        return [n for n in [self.left, self.right] if n is not None]

    def left_or_right(self, val):
        """Compare node to a value and return which path to take."""
        if val < self.val:
            return self.left
        return self.right


class BST(object):
    """Binary search tree."""

    def __init__(self, iterable=None):
        """Initialize bst with root and size."""
        self.root = None
        self._size = 0
        if iterable:
            for val in iterable:
                self.insert(val)

    def size(self):
        """Return number of nodes in bst."""
        return self._size

    def insert(self, val):
        """Insert a new node into the tree."""
        cur = self.root
        if cur is None:
            self.root = TreeNode(val)
            self._size += 1
        else:
            while True:
                if val == cur.val:
                    break
                which = cur.left_or_right(val)
                if which is None:
                    if val < cur.val:
                        cur.left = TreeNode(val, parent=cur)
                    else:
                        cur.right = TreeNode(val, parent=cur)
                    self._size += 1
                    break
                else:
                    cur = which

    def pre_order(self, root='root'):
        """Traverse the tree by visiting the parent first and then left and
        right children."""
        if root == 'root':
            root = self.root
        if root:
            yield root.val
            for node in root.children():
                    # yield from self.pre_order(root=node)
                for node in self.pre_order(root=node):
                    yield node


    def in_order(self, root='root'):
        """Traverse tree by visiting the left child, then the parent and the
        right child."""
        if root == 'root':
            root = self.root
        if root:
            for child in self.in_order(root=root.left):
                yield child
            yield root.val
            for child in self.in_order(root=root.right):
                yield child

    def post_order(self, root='root'):
        """Traverse tree by visiting left child, then the right child and then
        the parent."""
        if root == 'root':
            root = self.root
        if root:
            for node in root.children():
                for node in self.post_order(root=node):
                    yield node
            yield root.val

    def breadth_first(self, start):
        q = Queue()
        visited = []
        if self.size() > 0:
            visited = self._explore_bfs(start, q, visited)
        for node in visited:
            yield node.val

    def _explore_bfs(self, node, queue, visited):
        if node not in visited:
            visited.append(node)
        if node.children():
            for child in node.children():
                if child not in visited:
                    visited.append(child)
                    queue.enqueue(child)
            while len(queue):
                self._explore_bfs(queue.dequeue(), queue, visited)
        return visited
