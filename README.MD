[![Build Status](https://travis-ci.org/wenima/data-structures.svg?branch=bst-delete)](https://travis-ci.org/wenima/data-structures)

#Summary

The assignment was to implement deletion for a [binary search tree](https://en.wikipedia.org/wiki/Binary_search_tree)

in Python containing 1 new method:

* delete(self, val): remove val from the tree if present, if not present this method is a no-op. Return None in all cases.

#Definition:
* The node is a leaf (has no descendants)
* The node has one descendant (either left or right)
* The node has two descendants (both left and right)

For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/bst_3_delete.html


# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing                         |
| -----------------------  | ----- | ---- | ----- | ------------------------------- |
| src/bst.py               |  130  |  20  |  85%  | 97, 106, 161-187                |
| src/dbl_linked_list.py   |   80  |   0  | 100%  |                                 |
| src/queue.py             |   23  |   0  | 100%  |                                 |
| -----------------------  |  ---  |  --  | ----  | ------------------------------- |
| TOTAL                    |  233  |  20  |  91%  |                                 |


# Comments about implementation:
