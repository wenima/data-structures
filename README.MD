[![Build Status](https://travis-ci.org/wenima/data-structures.svg?branch=bst-balance)](https://travis-ci.org/wenima/data-structures)

#Summary

The assignment was to implement a self-balancing tree in Python. We chose to
implement an AVL tree. A new module has been created called avl.py containing
altered methods:

* insert(val): Insert val into the tree, and if tree has become unbalanced,
  rebalance with proper rotation.
* delete(val): If val is in the tree, delete val from the tree. If tree has 
  become unbalanced, rebalance with proper rotation.
* rebalance(node): Assess the balance around node and perform the correct rotation
  to rebalance the subtree.

For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/bst_4_balancing.html


# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing                         |
| -----------------------  | ----- | ---- | ----- | ------------------------------- |
|                          |       |      |       |                                 |
|                          |       |      |       |                                 |
| -----------------------  |  ---  |  --  | ----  | ------------------------------- |
| TOTAL                    |       |      |       |                                 |


# Comments about implementation:
stretch goal: implement one other solution of a self-balancing tree

# Tools we found useful:

* [AVL visualization](https://www.cs.usfca.edu/~galles/visualization/AVLtree.html)
