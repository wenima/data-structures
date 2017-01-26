"""Module to implement a Ternary Search Tree."""


class TreeNode(object):
    """Create Node objects for use in a binary tree data structure.

    Attributes:
        val:            A hash stored in the node.
        char:           A character as part of the search string.
        left:           A pointer to the left node.
        right:          A pointer to a right node.
        match:          A pointer to the node matching the current character
        parent:         A pointer to the parent node.
    """

    def __init__(self, char, left=None, right=None, parent=None):
        """."""
        self.hash = None
        self.char = char
        self.left = left
        self.right = right
        self.center = None
        self.parent = parent

    def is_leaf(self):
        """Return True if node has no children (is a leaf)."""
        return not (self.right or self.left)

    def is_root(self):
        """Return whether node is the root node."""
        return not self.parent

    def left_or_right(self, char):
        """Compare node to a value and return which path to take."""
        if char == self.char:
            return self.center
        elif char < self.char:
            return self.left
        else:
            return self.right


class TST(object):
    """Ternary Search Treet (TST) style data structure.

    If initialized with an iterable, will create nodes for each item in
    the iterable.

    Attributes:
        root:       Node sitting at the top of the tree.

        _size:      The number of nodes in the BST.

    Methods
        insert(self, string): will insert the input string into the trie. If
        character in the input string is already present, it will be ignored.

        contains(self, string): will return True if the string is in the trie,
        False if not.

        size(self): will return the total number of words contained within the trie.
        0 if empty.

        remove(self, string): will remove the given string from the trie. If the
        word doesn’t exist, will raise an appropriate exception.
    """

    def __init__(self, iterable=None):
        """Initialize bst with root and size."""
        self.root = None
        self._size = 0
        if iterable:
            try:
                for w in iterable:
                    self.insert(w)
            except TypeError:
                self.insert(iterable)

    def size(self):
        """Return number of nodes in tree."""
        return self._size

    def _additive_hash(self, key):
        """Return the additive hash for a given key."""
        h = 0
        for i in range(len(key)):
            h += ord(key[i])
        return h

    def insert(self, word):
        """Insert a new node into the tst."""
        furthest, idx = self._find_furthest(word)
        if not furthest:
            new_node = TreeNode(word[idx])
            self.root = new_node
            start = new_node
            idx += 1
        else:
            if word[idx] < furthest.char:
                furthest.left = TreeNode(word[idx], parent=furthest)
            else:
                furthest.right = TreeNode(word[idx], parent=furthest)
            start = furthest.left_or_right(word[idx])
            idx += 1
        for char in word[idx:]:
            start.center = TreeNode(char, parent=start)
            start = start.center
        start.hash = self._additive_hash(word)

    def _find_furthest(self, word):
        cur = self.root
        prev = None
        idx = 0
        while cur and idx < len(word):
            prev = cur
            cur = cur.left_or_right(word[idx])
            if prev.char == word[idx]:
                idx += 1
        return prev, idx

    def search(self, val, start='root'):
        """Return node with value val if it exists, otherwise None."""
        if start == 'root':
            return self.search(val, start=self.root)
        elif start is None:
            return None
        elif val == start.val:
            return start
        return self.search(val, start=start.left_or_right(val))

    def contains(self, word):
        """Return whether val in bst."""
        furthest = self._find_furthest(word)[0]
        return furthest.hash == self._additive_hash(word)

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
        return self.depth(start=start.left) - self.depth(start=start.right)


# if __name__ == '__main__':  # pragma: no cover
#     import timeit
#     import random

#     balanced_bst = BST()
#     degenerate_bst = BST()
#     for i in range(1000):
#         balanced_bst.insert(random.randint(0, 1000))
#         degenerate_bst.insert(i)

#     cur = balanced_bst.root
#     while cur:
#         if cur.right:
#             cur = cur.right
#         else:
#             break
#     biggest = cur.val

#     best_case = timeit.timeit(stmt='balanced_bst.search(biggest)',
#                               setup='from __main__ import balanced_bst, biggest',
#                               number=10000)
#     worst_case = timeit.timeit(stmt='degenerate_bst.search(99)',
#                                setup='from __main__ import degenerate_bst',
#                                number=10000)

#     print('Search balanced BST: ' + str(best_case),
#           '\nSearch degenerate BST: ' + str(worst_case))
