"""Module to implement a Binary Search Tree."""
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

    def depth(self, root):
        """Return the depth of a node, found recusively."""
        if self is root:
            return 0
        return 1 + self.parent.depth(root)

    def __iter__(self):
        if self:
            if self.has_left():
                for n in self.left:
                    yield n
            yield self.val
            result.append(self.val)
            if self.has_right():
                for n in self.right:
                    yield n


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

    def __iter__(self):
        return self.root.__iter__()

    def in_order(self):
        if self.root:
            return self.root.__iter__()
        yield None

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

    def pre_order(self, root='root'):
        """."""
        if root == 'root':
            root = self.root
        if root:
            yield root
            for node in root.children():
                yield from self.pre_order(root=node)

    def post_order(self, root='root'):
        """."""
        if root == 'root':
            root = self.root
        if root:
            for node in root.children():
                yield from self.post_order(root=node)
            yield root

    def breadth_first_traversal(self, start):
        """Launch a dfs search, exploring all nodes."""
        q = Queue()
        visited = []
        self._explore_bfs(start, q, visited)
        return visited

    def _explore_bfs(self, node, queue, visited):
        if node not in visited:
            visited.append(node)
        if node.children():
            for c in node.children():
                if c not in visited:
                    visited.append(c)
                    queue.enqueue(c)
            while len(queue):
                self._explore_bfs(queue.dequeue(), queue, visited)
        return visited
