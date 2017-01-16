"""Module to implement a Binary Search Tree."""


class TreeNode:
    """TreeNode is the root of the treet."""
   def __init__(self,val,left=None,right=None,parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right or self.left)

    def has_both_children(self):
        return self.right and self.left

class bst:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size
