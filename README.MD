#Summary

The assignment was to implement a [Graph Traversal](https://en.wikipedia.org/wiki/Graph_traversal)
in Python containing 2 new methods:

* g.depth_first_traversal(start): Perform a full depth-first traversal of the graph beginning at start. Return the full visited path when traversal is complete.
* g.breadth_first_traversal(start): Perform a full breadth-first traversal of the graph, beginning at start. Return the full visited path when traversal is complete.

For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/graph_2_traversal.html


# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing |
| -----------------------  | ----- | ---- | ----- | ------- |
| dbl_linked_list.py       |  75   |  0   | 100%  |         |
| linked_list.py           |  50   |  0   |  96%  |  80-81  |
| stack.py                 |   8   |  0   | 100%  |         |
| test_dbl_linked_list.py  |  185  |  0   | 100%  |         |
| test_linked_list.py      |  73   |  0   |  95%  |         |
| test_stack.py            |  48   |  0   | 100%  | 106-109 |
| -----------------------  |  ---  |  --  | ----  | ------- |
| TOTAL                    |  439  |  6   | 99%   |         |


# Comments about implementation:

* since this implementation of graph using an adjacency list is used only for sparse graphs, recursion depth of DFS is not a concern.
