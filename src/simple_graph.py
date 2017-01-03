"""An implementation of a simple graph."""

from stack import Stack
from queue import Queue
import string
import timeit
from random import randint

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

    g.depth_first_traversal(start): Perform a full depth-first traversal of the graph
    beginning at start. Return the full visited path when traversal is complete.

    g.breadth_first_traversal(start): Perform a full breadth-first traversal of
    the graph, beginning at start. Return the full visited path when traversal is complete.

    """

    def __init__(self):
        """Initialize a graph with a dict."""
        self._nodes = {}
        self._visited = []

    def nodes(self):
        """Return list of nodes."""
        return self._nodes.keys()

    def edges(self):
        """Return list of edges."""
        return list({str(key) + '-' + str(c) for key, val in self._nodes.items() for c in ''.join(val)})

    def add_node(self, n):
        """Add a node to the graph."""
        if not self.has_node(n):
            self._nodes[n] = []

    def add_edge(self, n1, n2):
        """Add edge to graph, if nodes not in graph, add them."""
        if self.has_node(n1):
            self._nodes[n1].append(n2)
        else:
            self._nodes.update({n1: [n2]})
        self.add_node(n2)

    def del_node(self, n):
        """Delete node from list and remove any reference to it in other nodes."""
        if self.has_node(n):
            self._nodes = {key: list(''.join(val).replace(n, '')) for key, val in self._nodes.items() if key != n}
        else:
            raise(KeyError)

    def del_edge(self, n1, n2):
        """Remove edge from list."""
        if n2 in self._nodes[n1]:
            self._nodes[n1].remove(n2)
        else:
            raise (ValueError)

    def has_node(self, n):
        """.Check if node is in graph."""
        return True if n in self._nodes else False

    def neighbors(self, n):
        """Return list of neighbors nodes to node n."""
        return self._nodes[n]

    def adjacent(self, n1, n2):
        """Return True if n1 and n2 are adjacent to each other."""
        if not self.has_node(n1) or not self.has_node(n2):
            raise(KeyError)
        return True if n2 in self._nodes[n1] else False

    def depth_first_traversal(self, start):
        """Launch a dfs search, exploring all nodes."""
        s = Stack()
        self._explore(start, s)
        return self._visited

    def _explore(self, node, stack):
        """Explore a given node, updated visited and stack and calls itself
        with a new unvisited node."""
        self._visited.append(node)
        if self.neighbors(node):
            stack.push(node)
            for node in self.neighbors(node):
                if node not in self._visited:
                    self._explore(node, stack)
        return stack

    def breadth_first_traversal(self, start):
        """Launch a dfs search, exploring all nodes."""
        q = Queue()
        self._explore_bfs(start, q)
        return self._visited

    def _explore_bfs(self, node, queue):
        if node not in self._visited:
            self._visited.append(node)
        if self.neighbors(node):
            for neighbor in self.neighbors(node):
                if neighbor not in self._visited:
                    self._visited.append(neighbor)
                    queue.enqueue(neighbor)
            try:
                self._explore_bfs(queue.dequeue(), queue)
            except IndexError:
                return queue
        return queue

# Make Random Graph
def make_random_graph():
    g = Graph()
    random = 0
    for i in range(1, 100):
        g.add_node(i)
        for j in range(randint(0, 10)):
            random = randint(1, 100)
            if random != i:
                g.add_edge(i, random)
    return g

g = make_random_graph()


def depth_test(g):
    """Depth Test for timing."""
    return g.depth_first_traversal(1)


def breadth_test(g):
    """Breadth Test for timing."""
    return g.breadth_first_traversal(1)

if __name__ == '__main__':

    print("Depth First Traversal - 100 node graph - between 0 and 10 edges:")
    print(timeit.repeat(stmt="depth_test(g)", setup="from simple_graph import depth_test, g", number=10000))

    print("Breadth First Traversal - 100 node graph - between 0 and 10 edges:")
    print(timeit.repeat(stmt="breadth_test(g)", setup="from simple_graph import breadth_test, g", number=10000))
