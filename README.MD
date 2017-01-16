#Summary

The assignment was to implement a [binary tree search](https://en.wikipedia.org/wiki/Binary_search_tree)

in Python containing 6 methods:

* bst.insert(self, val): will insert the value val into the BST. If val is already present, it will be ignored.
* search(self, val): will return the node containing that value, else None
* size(self): will return the integer size of the BST (equal to the total number of values stored in the tree). It will return 0 if the tree is empty.
* depth(self): will return an integer representing the total number of levels in the tree. If there is one value, the depth should be 1, if two values it will be 2, if three values it may be 2 or three, depending, etc.
* contains(self, val): will return True if val is in the BST, False if not.
* balance(self): will return an integer, positive or negative that represents how well balanced the tree is. Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value. An ideally-balanced tree should return 0.

#Definition:
A binary tree is made of nodes, where each node contains a "left" reference, a "right" reference, and a data element. The topmost node in the tree is called the root.

Every node (excluding a root) in a tree is connected by a directed edge from exactly one other node. This node is called a parent. On the other hand, each node can be connected to arbitrary number of nodes, called children. Nodes with no children are called leaves, or external nodes. Nodes which are not leaves are called internal nodes. Nodes with the same parent are called siblings.

A full binary tree is a binary tree in which each node has exactly zero or two children.
A complete binary tree is a binary tree, which is completely filled, with the possible exception of the bottom level, which is filled from left to right.


For more information on the assignment, see here: https://en.wikipedia.org/wiki/Binary_search_tree


# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing                         |
| -----------------------  | ----- | ---- | ----- | ------------------------------- |
|                          |       |      |       |                                 |
|                          |       |      |       |                                 |
| -----------------------  |  ---  |  --  | ----  | ------------------------------- |
| TOTAL                    |       |      |       |                                 |


# Comments about implementation:
