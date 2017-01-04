#Summary

The assignment was to implement a [weighted Graph](https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms#weighted_graph)

No additional functions have been added but many functions have been modified.

#Definition:
An edge-weighted graph is a pair (G,w) where G = (V,E) is a graph and w : E → IR is a weight function.

The assignment has a longer definition of an edge weighted graph, combined with a possible approach.

For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/graph_3_weighted.html


# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing                         |
| -----------------------  | ----- | ---- | ----- | ------------------------------- |
| test_simple_graph.py     |  123  |  5   |  91%  |  75-76, 247-249                 |
| simple_graph.py          |  95   |  9   |  96%  |  53, 143-144, 152, 157, 161-165 |
| -----------------------  |  ---  |  --  | ----  | ------------------------------- |
| TOTAL                    |  118  |  14  |  93%  |                                 |


# Comments about implementation:

* With the introduction of larger graphs, we probably need to implement an adjency matrix soon rather than relying on a list to hold the nodes
