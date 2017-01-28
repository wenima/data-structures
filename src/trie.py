"""Module to implement a Ternary Search Tree."""

from stack import Stack

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

    def __init__(self, char='', left=None, right=None, center=None, parent=None):
        """."""
        self.hash = None
        self.char = char
        self.left = left
        self.right = right
        self.center = center
        self.parent = parent

    def is_leaf(self):
        """Return True if node has no children (is a leaf)."""
        return not (self.right or self.left)

    def is_root(self):
        """Return whether node is the root node."""
        return not self.parent

    def left_right_center(self, char):
        """Compare node to a value and return which path to take."""
        if char == self.char:
            return self.center
        elif char < self.char:
            return self.left
        else:
            return self.right

    def children(self):
        """Return non-none children of node."""
        return [n for n in [self.left, self.right, self.center] if n is not None]


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

    def __init__(self, input_string=''):
        """Initialize bst with root and size."""
        self.root = None
        self._size = 0
        if input_string:
            try:
                iterable = input_string.split()
            except AttributeError:
                raise AttributeError("Only strings are allowed as input.")
        else:
            iterable = input_string
        for w in iterable:
            self.insert(w)

    def size(self):
        """Return number of nodes in tree."""
        return self._size

    def _additive_hash(self, key):
        """Return the additive hash for a given key."""
        return sum([ord(c) for c in key])

    def insert(self, word):
        furthest, idx = self._find_furthest(word)
        if not furthest:
            new_node = TreeNode(word[idx])
            self._size = 1
            self.root = new_node
            start = new_node
            idx += 1
        elif furthest.hash == self._additive_hash(word):
            return
        else:
            if word[idx] < furthest.char:
                furthest.left = TreeNode(word[idx], parent=furthest)
            elif word[idx] > furthest.char:
                furthest.right = TreeNode(word[idx], parent=furthest)
            else:
                furthest.center = TreeNode(word[idx], parent=furthest)
            self._size += 1
            start = furthest.left_right_center(word[idx])
            idx += 1
        for char in word[idx:]:
            start.center = TreeNode(char, parent=start)
            self._size += 1
            start = start.center
        start.hash = self._additive_hash(word)


    def _find_furthest(self, word):
        cur = self.root
        prev = None
        idx = 0
        while cur and idx < len(word):
            prev = cur
            cur = cur.left_right_center(word[idx])
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
        return self.search(val, start=start.left_right_center(val))

    def contains(self, word):
        if not self._size:
            return False
        furthest = self._find_furthest(word)[0]
        return furthest.hash == self._additive_hash(word)

    def depth_first_traversal(self, start, returnval=None):
        """Launch a dfs search, exploring all nodes. Return either all visited
        nodes or return only the nodes that contain hashes."""
        visited = []
        words = []
        s = Stack()
        self._explore(start, s, visited)
        if returnval == 'words':
            return words
        return visited

    def _explore(self, node, stack, visited, words):
        """Explore a given node, updated visited and stack and calls itself
        with a new unvisited node."""
        if node.hash:
            words.append(node)
        visited.append(node)
        if node.children():
            stack.push(node)
            for child in node.children():
                if child not in visited:
                    self._explore(node, stack, visited, words)
        return visited, words


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
