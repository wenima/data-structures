"""Module to implement a Binary Search Tree."""
from stack2 import Stack
from queue import Queue

class TreeNode(object):
    """TreeNode is the root of the tree."""

    def __init__(self, val, left=None, right=None, parent=None):
        """."""
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def _has_right(self):
        """Returns a bool indicating wether this node as a child larger in value."""
        return self.right

    def _is_root(self):
        """Return True if the node is the root node of the tree."""
        return not self.parent

    def _is_leaf(self):
        """Return True if the node is a leaf, i.e. has no children."""
        return not (self.right or self.left)

    def _children(self):
        """Return non-none children of node."""
        return [n for n in [self.left, self.right] if n is not None]

    def _left_or_right(self, val):
        """Compare node to a value and return which path to take."""
        if val < self.val:
            return self.left
        return self.right

    def depth(self, root):
        """Return the depth of a node, found recusively."""
        if self is root:
            return 0
        return 1 + self.parent.depth(root)

    def _set_parents_child(self, new_child):
        if self.parent:
            if self.parent.left is self:
                self.parent.left = new_child
            else:
                self.parent.right = new_child


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

    def _iterate_from(self, node):
        """Return a generator of all the children on the left of starting node"""
        while node is not None:
            yield node
            node = node.left

    def _get_leftmost(self, node_to_delete):
        """Return the leftmost child of the right branch of the target node."""
        left_children = [node for node in self._iterate_from(self.search(node_to_delete.val).right)]
        return left_children[-1]

    def insert(self, val):
        """Insert a new node into the tree."""
        cur = self.root
        if cur is None:
            self.root = TreeNode(val)
        else:
            while True:
                if val == cur.val:
                    break
                which = cur._left_or_right(val)
                if which is None:
                    if val < cur.val:
                        cur.left = TreeNode(val, parent=cur)
                    else:
                        cur.right = TreeNode(val, parent=cur)
                    break
                else:
                    cur = which

    def search(self, val, start='root'):
        """Return node with value value if it exists, otherwise None."""
        if start == 'root':
            return self.search(val, start=self.root)
        if start is None:
            return None
        if val == start.val:
            return start
        return self.search(val, start=start._left_or_right(val))

    def contains(self, val):
        """Return True if a node matching the given value is part of the tree."""
        return bool(self.search(val))

    def depth(self, start='root'):
        """Return an integer representing the total height of the tree,
        starting at 0 if the tree only as a root."""
        if start == 'root':
            start = self.root
        if start is None or start._is_leaf():
            return 0
        return max(self.depth(start=start.left), self.depth(start=start.right)) + 1

    def pre_order(self, root='root'):
        """Traverse the tree by visiting the parent first and then left and
        right children."""
        if root == 'root':
            root = self.root
        if root:
            yield root
            for node in root._children():
                for child in self.pre_order(root=node):
                    yield child

    def post_order(self, root='root'):
        """Traverse tree by visiting left child, then the right child and then
        the parent."""
        if root == 'root':
            root = self.root
        if root:
            for node in root._children():
                for child in self.post_order(root=node):
                    yield child
            yield root

    def in_order(self, root='root'):
        """Traverse tree by visiting the left child, then the parent and the
        right child."""
        if root == 'root':
            root = self.root
        if root:
            for child in self.in_order(root=root.left):
                yield child
            yield root
            for child in self.in_order(root=root.right):
                yield child

    def delete(self, val):
        """Delete a node and reorganize tree as needed."""
        to_d = self.search(val)
        replacement = None
        if to_d._is_leaf():
            to_d._set_parents_child(None)
        else:
            children = to_d._children()
            if len(children) == 1:
                child = children[0]
                child.parent = to_d.parent
                to_d._set_parents_child(child)
                replacement = child
            else:
                lmost = self._get_leftmost(to_d)
                replacement = lmost
                if lmost._has_right():
                    lmost.right.parent = lmost.parent
                    lmost._set_parents_child(lmost.right)
                else:
                    lmost._set_parents_child(None)

                if to_d.right:
                    lmost.right = to_d.right
                    to_d.right.parent = lmost
                lmost.left = to_d.left
                to_d.left.parent = lmost

                to_d._set_parents_child(lmost)
                lmost.parent = to_d.parent
        if to_d._is_root():
            self.root = replacement

    def breadth_first(self, start):
        """Return a generator of breadth first traversal through tree."""
        q = Queue()
        visited = []
        if self.size > 0:
            visited = self._explore_bfs(start, q, visited)
        for node in visited:
            yield node

    def _explore_bfs(self, node, queue, visited):
        """Helper function called by breadth_first, yielding each node as
        it's being visited."""
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


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'timeit':
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

        good_case = timeit.timeit(stmt='balanced_bst.search(biggest)',
                                  setup='from __main__ import balanced_bst, biggest',
                                  number=10000)
        worst_case = timeit.timeit(stmt='degenerate_bst.search(99)',
                                   setup='from __main__ import degenerate_bst',
                                   number=10000)

        print('Search balanced BST: ' + str(good_case),
              '\nSearch degenerate BST: ' + str(worst_case))
