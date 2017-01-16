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
        """Return non-none children of node."""
        return [n for n in [self.left, self.right] if n is not None]

    def left_or_right(self, val):
        """Compare node to a value and return which path to take."""
        if val < self.val:
            return self.left
        return self.right

    def depth(self, root):
        """Return the depth of a node, found recusively."""
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

    def depth_bad(self, start='root'):
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

    def depth(self, start='root'):
        """Totally came up with this myself."""
        if start == 'root':
            start = self.root
        if start is None:
            return 0
        return max(self.depth(start=start.left), self.depth(start=start.right)) + 1

    def balance(self, start='root'):
        """Return left vs right balance from a node on the bst."""
        if start == 'root':
            start = self.root
        if start is None:
            return 0
        return self.depth(start=start.right) - self.depth(start=start.left)

if __name__ == '__main__':
    import timeit
    import random

    bst = BST()
    for i in range(100):
        bst.insert(random.randint(0, 100))

    depth = timeit.timeit(
        stmt="bst.depth()",
        setup="from __main__ import bst",
        number=10000,
    )
    depthbad = timeit.timeit(
        stmt="bst.depth_bad()",
        setup="from __main__ import bst",
        number=10000,
    )
    print(depth, depthbad)
