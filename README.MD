#Summary

The assignment was to implement 2 solutions to the [shortest-path problem](https://en.wikipedia.org/wiki/Shortest_path_problem)

No additional functions have been added but many functions have been modified.

#Definition:
In graph theory, the shortest path problem is the problem of finding a path between two vertices (or nodes) in a graph such that the sum of the weights of its constituent edges is minimized.


For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/graph_4_shortest_path.html


# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing                         |
| -----------------------  | ----- | ---- | ----- | ------------------------------- |
| test_simple_graph.py     |  123  |  5   |  91%  |  75-76, 247-249                 |
| simple_graph.py          |  95   |  9   |  96%  |  53, 143-144, 152, 157, 161-165 |
| -----------------------  |  ---  |  --  | ----  | ------------------------------- |
| TOTAL                    |  118  |  14  |  93%  |                                 |


# Comments about implementation:

## 2 algorithms are implemented to to solve the Shortest_path_problem with [Dijkstra](https://en.wikipedia.org/wiki/Dijkstra's_algorithm) being mandatory
