"""Module to implement a Binary Search Tree."""

class TreeNode(object):

    """Create Node objects for use in a binary tree data structure.

    Attributes:
        val:            A value or data stored in the node.
        left:           A pointer to the left node.
        right:          A pointer to a right node.
        parent:         A pointer to the parent node.
    """

    def __init__(self, val, left=None, right=None, parent=None):
        """."""
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def is_leaf(self):
        """Return True if node has no children (is a leaf)."""
        return not (self.right or self.left)

    def left_or_right(self, val):
        """Compare node to a value and return which path to take."""
        if val < self.val:
            return self.left
        return self.right


class BST(object):

    """Binary Search Treet (BST) style data structure.

    If initialized with an iterable, will create nodes for each item in
    the iterable.

    Attributes:
        root:       Node sitting at the top of the tree.

        _size:      The number of nodes in the BST.

    Methods:
        insert(self, val): will insert the value val into the BST. If val is
        already present, it will be ignored.

        search(self, val): will return the node containing that value, else None

        size(self): will return the integer size of the BST (equal to the total
        number of values stored in the tree). It will return 0 if the tree is empty.

        depth(self): will return an integer representing the total number of
        levels in the tree. If there is just root, the depth value is 0, if
        there is one value, the depth should be 1, if two values it will be 2,
        if three values it may be 2 or three, depending, etc.

        contains(self, val): will return True if val is in the BST, False if not.

        balance(self): will return an integer, positive or negative that
        represents how well balanced the tree is. Trees which are higher on the
        left than the right should return a positive value, trees which are
        higher on the right than the left should return a negative value. An
        ideally-balanced tree should return 0.
    """

    def __init__(self, iterable=None):
        """Initialize bst with root and size."""
        self.root = None
        self._size = 0
        if iterable:
            try:
                for val in iterable:
                    self.insert(val)
            except TypeError:
                self.insert(iterable)

    def size(self):
        """Return number of nodes in tree"""
        return self._size

    def insert(self, val):
        """Insert a new node into the bst."""
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
        """Return the depth of the tree."""
        if start == 'root':
            start = self.root
        if start is None or start.is_leaf():
            return 0
        return max(self.depth(start=start.left), self.depth(start=start.right)) + 1

    def balance(self, start='root'):
        """Return an integer, positive or negative that represents how well
        balanced the tree is."""
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
