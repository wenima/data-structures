#Summary

The assignment was to implement a [Simple Graph](https://www.python.org/doc/essays/graphs/)
in Python containing 9 methods:

* g.nodes(): return a list of all nodes in the graph
* g.edges(): return a list of all edges in the graph
* g.add_node(n): adds a new node ‘n’ to the graph
* g.add_edge(n1, n2): adds a new edge to the graph connecting ‘n1’ and ‘n2’, if either n1 or n2 are not already present in the graph, they should be added.
* g.del_node(n): deletes the node ‘n’ from the graph, raises an error if no such node exists
* g.del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the graph, raises an error if no such edge exists
* g.has_node(n): True if node ‘n’ is contained in the graph, False if not.
* g.neighbors(n): returns the list of all nodes connected to ‘n’ by edges, raises an error if n is not in g
* g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g


For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/graph_1.html


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


# Thoughts on when to use a singly linked list vs a doubly_linked_list:

# Comments about implementation:
