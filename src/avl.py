"""Module to show the implemenation of an AVL tree."""

from bst import BST
from bst import TreeNode

class AVL(BST):
    def __init__(self):
        super(B, self).__init__()

    def extended_insert_method():
        """insert and calls check method to see if we need to balance."""
        pass


    def rebalance(self,node):
        """Rebalance a tree."""
        #1. If subtree needs LR to balance:
        #   check balance factor for the right child:
        #   If the right child is left heavy, then do a RR on right child,
        #   followed by LR.
        #2. If a subtree needs a RR to balance:
        #   check balance factor of the left child:
        #   if left child is right heavy, do a LR on the left child,
        #   followed by RR.
        if n.bf < 0:
            if node.right.bf > 0:
                self.rr(n.right)
                self.rl(n)
        else:
            self.rl(n)
        elif n.bf > 0:
        if n.lf.bf < 0:
            self.rl(node.leftChild)
            self.rr(node)
        else:
            self.rr(node)
