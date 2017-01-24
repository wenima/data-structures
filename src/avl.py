"""Module to show the implemenation of an AVL tree."""

from bst import BST


class AVL(BST):
    """Self balancing binary search tree."""

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

    def insert(self, val):
        """Insert and calls check method to see if we need to balance."""
        node = super(AVL, self).insert(val)
        if node:
            r_root = self._check_balance(node)
            if r_root:
                self.rebalance(r_root)

    def delete(self, val):
        """Insert and calls check method to see if we need to balance."""
        node = super(AVL, self).delete(val)
        if node:
            r_root = self._check_balance(node)
            if r_root:
                self.rebalance(r_root)

    def _check_balance(self, node):
        """Bubble up from a node and check for unbalanced trees."""
        while True:
            balance = self.balance(start=node)
            if abs(balance) > 1:
                return node
            if node.parent:
                node = node.parent
            else:
                break

    def rebalance(self, n):
        """
        Rebalance a tree starting at node n. We assume that a tree heavy on the right side will
        have a postive balance and trees heavy on the left side a negative value.
        """
        # 1. If subtree needs LR to balance:
        #   check balance factor for the right child:
        #   If the right child is left heavy, then do a RR on right child,
        #   followed by LR.
        # 2. If a subtree needs a RR to balance:
        #   check balance factor of the left child:
        #   if left child is right heavy, do a LR on the left child,
        #   followed by RR.
        if self.balance(n) < 0:
            if self.balance(n.right) <= 0:
                self._lr(n)
            else:
                self._rlr(n)
        elif self.balance(n) > 0:
            if self.balance(n.left) >= 0:
                self._rr(n)
            else:
                self._lrr(n)
        next_node = self._check_balance(n)
        if next_node:
            self.rebalance(next_node)

    def _lr(self, r_root):
        """Perform a left rotation (lr) around the rotation_root (r_root)."""
        # assume:
        #   a
        #    \
        #     b
        #      \
        #       c
        # 1. b becomes the new root
        # 2. a takes responsibility of b's left child, in this case None.
        # 3. b makes a it's left child
        n_root = r_root.right
        r_root.right = n_root.left
        if n_root.left:
            n_root.left.parent = r_root
        if r_root.is_root():
            self.root = n_root
        r_root.set_parents_child(n_root)
        n_root.parent = r_root.parent
        n_root.left = r_root
        r_root.parent = n_root

    def _rr(self, r_root):
        """Perform a right rotation (rl) around the rotation_root (r_root)."""
        # assume:
        #           c
        #          /
        #         b
        #        /
        #       a
        # 1. b becomes new root
        # 2. c takes responsibility of b's right child as it's left child
        # 3. b takes responsibility of c as it's right child
        n_root = r_root.left
        r_root.left = n_root.right
        if n_root.right:
            n_root.right.parent = r_root
        if r_root.is_root():
            self.root = n_root
        r_root.set_parents_child(n_root)
        n_root.right = r_root
        n_root.parent = r_root.parent
        r_root.parent = n_root

    def _lrr(self, rotation_root):
        """Perform two phase left-right rotation."""
        left_root = rotation_root.left
        new_root = left_root.right
        rotation_root.left = new_root
        new_root.parent = rotation_root
        left_root.parent = new_root
        left_root.right = new_root.left
        if new_root.left:
            new_root.left.parent = left_root
        new_root.left = left_root
        self._rr(rotation_root)

    def _rlr(self, rotation_root):
        """Perform two phase right-left rotation."""
        right_root = rotation_root.right
        new_root = right_root.left
        rotation_root.right = new_root
        new_root.parent = rotation_root
        right_root.parent = new_root
        right_root.left = new_root.right
        if new_root.right:
            new_root.right.parent = right_root
        new_root.right = right_root
        self._lr(rotation_root)
