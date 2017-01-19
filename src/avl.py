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



    # def rebalance(self,node):
    #     """Rebalance a tree."""
    #     #1. If subtree needs LR to balance:
    #     #   check balance factor for the right child:
    #     #   If the right child is left heavy, then do a RR on right child,
    #     #   followed by LR.
    #     #2. If a subtree needs a RR to balance:
    #     #   check balance factor of the left child:
    #     #   if left child is right heavy, do a LR on the left child,
    #     #   followed by RR.
    #     if n.bf < 0:
    #         if node.right.bf > 0:
    #             self.rr(n.right)
    #             self.rl(n)
    #     else:
    #         self.rl(n)
    #     elif n.bf > 0:
    #     if n.lf.bf < 0:
    #         self.rl(node.leftChild)
    #         self.rr(node)
    #     else:
    #         self.rr(node)
