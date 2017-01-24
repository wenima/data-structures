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

    def has_left(self):
        """Returns a bool indicating wether this node as a child smaller in value."""
        return self.left

    def has_right(self):
        """Returns a bool indicating wether this node as a child larger in value."""
        return self.right

    def is_root(self):
        """."""
        return not self.parent

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

    def set_parents_child(self, new_child):
        if self.parent:
            if self.parent.left is self:
                self.parent.left = new_child
            else:
                self.parent.right = new_child

    def __iter__(self):
        if self:
            if self.has_left():
                for n in self.left:
                    yield n
            yield self
            if self.has_right():
                for n in self.right:
                    yield n


class BST(object):
    """Binary search tree."""

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
        """Return number of nodes in bst.."""
        return self._size

    def __len__(self):
        """Return number of nodes in bst."""
        return self.size()

    def __iter__(self):
        """Allow iteration through bst."""
        return self.root.__iter__()

    def _iterate_from(self, node):
        """Return a generator of all the children on the left of starting node."""
        while node is not None:
            yield node
            node = node.left

    def _get_leftmost(self, node_to_delete):
        """Return the leftmost child of the right branch of the target node."""
        left_children = [node for node in self._iterate_from(self.search(node_to_delete.val).right)]
        return left_children[-1]

    def insert(self, val):
        """Insert a new node into the bst."""
        cur = self.root
        if cur is None:
            self.root = TreeNode(val)
            self._size += 1
            return self.root
        else:
            while True:
                if val == cur.val:
                    break
                which = cur.left_or_right(val)
                if which is None:
                    if val < cur.val:
                        cur.left = TreeNode(val, parent=cur)
                        self._size += 1
                        return cur.left
                    else:
                        cur.right = TreeNode(val, parent=cur)
                        self._size += 1
                        return cur.right
                else:
                    cur = which

    def search(self, val, start='root'):
        """Return node with value val if it exists, otherwise None."""
        if start == 'root':
            return self.search(val, start=self.root)
        if start is None:
            return None
        if val == start.val:
            return start
        return self.search(val, start=start.left_or_right(val))

    def contains(self, val):
        """Return whether val in bst."""
        return bool(self.search(val))

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
        return self.depth(start=start.left) - self.depth(start=start.right)

    def pre_order(self, root='root'):
        """."""
        if root == 'root':
            root = self.root
        if root:
            yield root.val
            for node in root.children():
                for child in self.pre_order(root=node):
                    yield child

    def post_order(self, root='root'):
        """."""
        if root == 'root':
            root = self.root
        if root:
            for node in root.children():
                for child in self.post_order(root=node):
                    yield child
            yield root.val

    def in_order(self, root='root'):
        """."""
        if root == 'root':
            root = self.root
        if root:
            for child in self.in_order(root=root.left):
                yield child
            yield root.val
            for child in self.in_order(root=root.right):
                yield child

    def delete(self, val):
        """Delete a node and reorganize tree as needed."""
        to_d = self.search(val)
        if to_d:
            replacement = None
            check_from = to_d.parent
            self._size -= 1
            if to_d.is_leaf():
                to_d.set_parents_child(None)
            else:
                children = to_d.children()
                if len(children) == 1:
                    child = children[0]
                    child.parent = to_d.parent
                    to_d.set_parents_child(child)
                    replacement = child
                else:
                    lmost = self._get_leftmost(to_d)
                    replacement = lmost
                    check_from = lmost
                    if lmost.parent is not to_d:
                        check_from = lmost.parent
                    if lmost.has_right():
                        lmost.right.parent = lmost.parent
                        lmost.set_parents_child(lmost.right)
                    else:
                        lmost.set_parents_child(None)

                    if to_d.right:
                        lmost.right = to_d.right
                        to_d.right.parent = lmost
                    lmost.left = to_d.left
                    to_d.left.parent = lmost

                    to_d.set_parents_child(lmost)
                    lmost.parent = to_d.parent
            if to_d.is_root():
                self.root = replacement
            return check_from

    def breadth_first(self, start='root'):
        """Return a generator of breadth first traversal through tree."""
        if start == 'root':
            start = self.root
        q = Queue()
        visited = []
        if self._size > 0:
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


if __name__ == '__main__':  # pragma: no cover
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
