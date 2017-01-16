"""Module to implement a Binary Search Tree."""
from stack2 import Stack


class TreeNode(object):
    """TreeNode is the root of the tree."""

    def __init__(self, val, left=None, right=None, parent=None):
        """."""
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def is_root(self):
        """."""
        return not self.parent

    def is_leaf(self):
        """."""
        return not (self.right or self.left)

    def has_both_children(self):
        """."""
        return self.right and self.left

    def children(self):
        return [n for n in [self.left, self.right] if n is not None]

    def left_or_right(self, val):
        """."""
        if val < self.val:
            return self.left
        return self.right

    def depth(self, root):
        if self is root:
            return 1
        return 1 + self.parent.depth(root)


class BST(object):
    """Binary search tree."""

    def __init__(self, iterable=None):
        """Initialize bst with root and size."""
        self.root = None
        self.size = 0
        if iterable:
            try:
                for val in iterable:
                    self.insert(val)
            except TypeError:
                self.insert(iterable)

    def size(self):
        """Return number of nodes in bst.."""
        return self.size

    def __len__(self):
        """Return number of nodes in bst."""
        return self.size

    def insert(self, val):
        """Insert a new node into the bst."""
        cur = self.root
        if cur is None:
            self.root = TreeNode(val)
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
                    break
                else:
                    cur = which

    def search(self, val, start='root'):
        """Return node with value val if it exists, otherwise None."""
        if start == 'root':
            return self.search(val, start=self.root)
        elif start is None:
            return None
        elif val == start.val:
            return start
        return self.search(val, start=start.left_or_right(val))

    def contains(self, val):
        """Return whether val in bst."""
        return bool(self.search(val))

    def depth(self, start='root'):
        """Return the max depth of the bst."""
        if start == 'root':
            start = self.root
        stack = Stack([start])
        visited = set()
        max_depth = 0
        while stack.top:
            cur = stack.pop()
            if cur not in visited:
                visited.add(cur)
                if cur.is_leaf():
                    cur_depth = cur.depth(start)
                    if cur_depth > max_depth:
                        max_depth = cur_depth
                else:
                    for child in cur.children():
                        stack.push(child)
        return max_depth
