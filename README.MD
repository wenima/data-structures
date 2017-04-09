# Summary
=======
[![Build Status](https://travis-ci.org/wenima/data-structures.svg?branch=bst)]https://travis-ci.org/wenima/data-structures.svg?branch=master

The assignment was to implement a [binary tree search](https://en.wikipedia.org/wiki/Binary_search_tree) in Python containing 6 methods:

* bst.insert(self, val): will insert the value val into the BST. If val is already present, it will be ignored.
* search(self, val): will return the node containing that value, else None
* size(self): will return the integer size of the BST (equal to the total number of values stored in the tree). It will return 0 if the tree is empty.
* depth(self): will return an integer representing the total number of levels in the tree. If there is just root, the depth value is 0, if there is one value, the depth should be 1, if two values it will be 2, if three values it may be 2 or three, depending, etc.
* contains(self, val): will return True if val is in the BST, False if not.
* balance(self): will return an integer, positive or negative that represents how well balanced the tree is. Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value. An ideally-balanced tree should return 0.

# Definition:

A BST is a binary tree where nodes are ordered in the following way:
* each node contains one key (also known as data)
* the keys in the left subtree are less then the key in its parent node, in short L < P;
* the keys in the right subtree are greater the key in its parent node, in short P < R;
* duplicate keys are not allowed.


For more information on the assignment, see here: https://en.wikipedia.org/wiki/Binary_search_tree

# Testing:

=======
| Name                     | Stmts | Miss | Cover | Missing                         |
| -----------------------  | ----- | ---- | ----- | ------------------------------- |
| src/bst.py               |  79   |  16  |  80%  | 135-159                         |
| src/test_bst.py          |  73   |   1  |  99%  | 111                             |
| -----------------------  |  ---  |  --  | ----  | ------------------------------- |
| TOTAL                    | 152   |  17  |  89%  |                                 |


# Comments about implementation:

* the linked_list.py module contains two "helper" functions. ```python _iterate_from()``` takes in a list object from which to iterate (usually head) and returns an iterable which then can be used in different ways, one of them is ```_node_values``` which uses list comprehension to return a list containing all values/data of all the nodes.
