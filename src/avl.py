"""Module to show the implemenation of an AVL tree."""

from bst import BST
from bst import TreeNode


class AVL(BST):
    """Self balancing binary search tree."""

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

    def insert(self, val):
        """insert and calls check method to see if we need to balance."""
        node = super(AVL, self).insert(val)
        self.check_balance(node)

    def check_balance(self, node):
        """Bubble up from a node and check for unbalanced trees."""
        while True:
            balance = self.balance(start=node)
            if abs(balance) > 1:
                return node
            if node.parent:
                node = node.parent
            else:
                break

    def rebalance(self,n):
        """Rebalance a tree starting at node n. We assume that a tree heavy on the right side will
        have a postive balance and trees heavy on the left side a negative value."""
        #1. If subtree needs LR to balance:
        #   check balance factor for the right child:
        #   If the right child is left heavy, then do a RR on right child,
        #   followed by LR.
        #2. If a subtree needs a RR to balance:
        #   check balance factor of the left child:
        #   if left child is right heavy, do a LR on the left child,
        #   followed by RR.
        if b.balance(n) > 0:
            if b.balance(n.right) < 0:
                self.rr(n.right)
                self.lr(n)
            else:
                self.lr(n)
        elif b.balance(n) < 0:
            if b.balance(n.left) > 0:
                self.lr(n.left)
                self.rr(n)
            else:
                self.rr(n)

    def lr(self,r_root):
        """Perform a left rotation (lr) around the rotation_root (r_root)."""
        #assume:
        #   a
        #    \
        #     b
        #      \
        #       c
        #1. b becomes the new root
        #2. a takes responsibility of b's left child, in this case None.
        #3. b makes a it's left child
        n_root = r_root.right
        r_root.right = n_root.left
        if n_root.left != None:
            n_root.left.parent = r_root
            n_root.parent = r_root.parent
        if r_root.is_root():
            self.root = n_root
        else:
            if r_root.is_left():
                r_root.parent.left = n_root
            else:
                r_root.parent.right = n_root
        n_root.left = r_root
        r_root.parent = n_root

    def rr(self, r_root):
        """Perform a right rotation (rl) around the rotation_root (r_root)."""
        #assume:
        #           c
        #          /
        #         b
        #        /
        #       a
        #1. b becomes new root
        #2. c takes responsibility of b's right child as it's left child
        #3. b takes responsibility of c as it's right child
        n_root = r_root.left
        r_root.left = n_root.right
        if n_root.right != None:
            n_root.right.parent = r_root
            n_root.parent = r_root.parent
        if r_root.is_root():
            self.root = n_root
        else:
            if r_root.is_right():
                r_root.parent.right = n_root
            else:
                r_root.parent.right = n_root
        n_root.right = r_root
        r_root.parent = n_root
