"""An implementation of a simple graph."""

class Graph(object):
    """A graph class."""

    def __init__(self):
        self._nodes = {}


    def nodes(self):
        return self._nodes.keys()

    def edges(self):
        edges = []
        for node in self._nodes:
            for edge in self._nodes[node]:
                edge = str(node + '-' + edge)
                edges.append(edge)
        return edges 


    def add_node(self, n):
        self._nodes['n'] = []

    def add_edge(self, n1, n2):
        self._nodes['n1'].append(n2)

    def del_node(self, n)
        del self._nodes[n]
        for node in self._nodes:
            for edge in self._nodes[node]:
                if edge == n:
                    self._nodes[node].remove(n)

    def del_edge(self, n1, n2)
        self[n1].remove(n2)

    def has_node(self, n):
        if self._node[n]:
            return True
        return False

    def neighbors(self, n):
        return self._nodes[n]

    def adjacent(self, n1, n2):
        if n2 in self._nodes[n1]:
            return True
        return False
