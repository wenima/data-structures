"""An implementation of a simple graph."""


class Graph(object):
    """A graph class.

    nodes() - Return list of nodes in graph

    edges() - Return all edges in graph

    add_node(n) -add node n to graph

    add_edge(n1. n2) - add edge between n1 and n2 add nodes if not already in graph

    del_node(n) - delete node n

    del_edge(n1, n2) - del edge between n1 and n2

    has_node(n) - check if node n is in graph

    neighbors(n) - return list of neighbors of n

    adjacent(n1, n2) - check if n1 and n2 are adjacent.

    """

    def __init__(self):
        """Initialize a graph with a dict."""
        self._nodes = {}

    def nodes(self):
        """Return list of nodes."""
        return list(self._nodes.keys())

    def edges(self):
        """Return list of edges."""
        return list({key + '-' + c for key, val in self._nodes.items() for c in ''.join(val)})

    def add_node(self, n):
        """Add a node to the graph."""
        if not self.has_node(n):
            self._nodes[n] = []

    def add_edge(self, n1, n2):
        """Add edge to graph, if nodes not in graph, add them."""
        if self.has_node(n1):
            self._nodes[n1].append(n2)
        else:
            self._nodes.update({n1:[n2]})
        self.add_node(n2)

    def del_node(self, n):
        """Delete node from list and remove any reference to it in other nodes."""
        if self.has_node(n):
            self._nodes = {key : list(''.join(val).replace(n, '')) for key, val in self._nodes.items() if key != n}
        else:
            raise KeyError

    def del_edge(self, n1, n2):
        """Remove edge from list."""
        if n2 in self._nodes[n1]:
            self._nodes[n1].remove(n2)
        else:
            raise ValueError

    def has_node(self, n):
        """.Check if node is in graph."""
        return n in self._nodes

    def neighbors(self, n):
        """Return list of neighbors nodes to node n."""
        return self._nodes[n]

    def adjacent(self, n1, n2):
        """Return True if n1 and n2 are adjacent to each other."""
        if not self.has_node(n1) or not self.has_node(n2):
            raise KeyError
        return True if n2 in self._nodes[n1] else False
