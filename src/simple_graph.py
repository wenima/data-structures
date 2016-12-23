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
                edge = str(node) + '-' + str(edge)
                edges.append(edge)
        return edges 


    def add_node(self, n):
        if not self.has_node(n):
            self._nodes[n] = []

    def add_edge(self, n1, n2):
        if not self.has_node(n1):
            self.add_node(n1)
        if not self.has_node(n2):
            self.add_node(n2)
        self._nodes[n1].append(n2)

    def del_node(self, n):
        if self.has_node(n):
            del self._nodes[n]
            for node in self._nodes:
                for edge in self._nodes[node]:
                    if edge == n:
                        self._nodes[node].remove(n)
        else:
            raise(KeyError)

    def del_edge(self, n1, n2):
        if n2 in self._nodes[n1]:
            self._nodes[n1].remove(n2)
        raise (ValueError)

    def has_node(self, n):
        if n in self._nodes:
            return True
        return False

    def neighbors(self, n):
        return self._nodes[n]

    def adjacent(self, n1, n2):
        if not self.has_node(n1) or not self.has_node(n2):
            raise(KeyError)
        if n2 in self._nodes[n1]:
            return True
        return False
