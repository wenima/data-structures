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
| simple_graph.py          |  31   |  0   | 100%  |         |
| test_simple_graph.py     |  72   |  0   | 100%  |         |
| -----------------------  |  ---  |  --  | ----  | ------- |
| TOTAL                    |  103  |  0   | 100%  |         |


# Comments about implementation:
* We decided to implement using a [Adjacency List](https://en.wikipedia.org/wiki/Adjacency_list) as we assume a spare graph.
* The implementation is for an unweighted, directed graph.
