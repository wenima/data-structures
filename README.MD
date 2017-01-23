[![Build Status](https://travis-ci.org/wenima/data-structures.svg?branch=bst-traversal)](https://travis-ci.org/wenima/data-structures)

# Summary

The assignment was to implement a traversal for a [binary tree search](https://en.wikipedia.org/wiki/Binary_search_tree)

in Python containing 4 methods:

* in_order(self): will return a generator that will return the values in the tree using in-order traversal, one at a time.
* pre_order(self): will return a generator that will return the values in the tree using pre-order traversal, one at a time.
* post_order(self): will return a generator that will return the values in the tree using post_order traversal, one at a time.
* breadth_first(self): will return a generator that will return the values in the tree using breadth-first traversal, one at a time.

# Definition:
* PreOrder traversal - visit the parent first and then left and right children;
* InOrder traversal - visit the left child, then the parent and the right child;
* PostOrder traversal - visit left child, then the right child and then the parent;


For more information on the assignment, see here: https://en.wikipedia.org/wiki/Binary_search_tree


# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing                         |
| -----------------------  | ----- | ---- | ----- | ------------------------------- |
| src/bst.py               |  82   |  0   | 100%  |                                 |
| src/dbl_linked_list.py   |  80   |  0   | 100%  |                                 |
| src/queue.py             |  23   |  0   | 100%  |                                 |
| src/test_bst_traversal.py|  49   |  0   | 100%  |                                 |
| -----------------------  |  ---  |  --  | ----  | ------------------------------- |
| TOTAL                    |  234  |  0   | 100%  |                                 |


# Comments about implementation:
stretch goal: Euler walk
