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

    def is_leaf(self):
        """."""
        return not (self.right or self.left)

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
            return 0
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
        """Totally came up with this myself."""
        if start == 'root':
            start = self.root
        if start is None or start.is_leaf():
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

    balanced_bst = BST()
    degenerate_bst = BST()
    for i in range(1000):
        balanced_bst.insert(random.randint(0, 1000))
        degenerate_bst.insert(i)

    cur = balanced_bst.root
    while cur:
        if cur.right:
            cur = cur.right
        else:
            break
    biggest = cur.val

    best_case = timeit.timeit(stmt='balanced_bst.search(biggest)',
                              setup='from __main__ import balanced_bst, biggest',
                              number=10000)
    worst_case = timeit.timeit(stmt='degenerate_bst.search(99)',
                               setup='from __main__ import degenerate_bst',
                               number=10000)

    print('Search balanced BST: ' + str(best_case),
          '\nSearch degenerate BST: ' + str(worst_case))
