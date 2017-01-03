"""An implementation of a simple graph."""

from stack import Stack
from queue import Queue
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

    """

    def __init__(self):
        """Initialize a graph with a dict."""
        self._nodes = {}
        self._visited = []

    def nodes(self):
        """Return list of nodes."""
        return list(self._nodes.keys())

    def edges(self):
        """Return list of edges."""
        edges = []
        for node in self._nodes:
            for edge in self._nodes[node]:
                edge = str(node) + '-' + str(edge[0]) + ':' + str(edge[1])
                edges.append(edge)
        return edges

    def add_node(self, n):
        """Add a node to the graph."""
        if not self.has_node(n):
            self._nodes[n] = []

    def add_edge(self, n1, n2, weight=0):
        """Add edge to graph, if nodes not in graph, add them."""
        if self.has_node(n1):
            self._nodes[n1].append((n2, weight))
        else:
            self._nodes.update({n1: [(n2, weight)]})
        self.add_node(n2)

    def del_node(self, n):
        """Delete node from list and remove any reference to it in other nodes."""
        if self.has_node(n):
            del self._nodes[n]
            for node in self._nodes:
                for edge in self._nodes[node]:
                    if edge[0] == n:
                        self._nodes[node].remove(edge)
        else:
            raise(KeyError)

    def del_edge(self, n1, n2):
        """Remove edge from list."""
        for edge in self._nodes[n1]:
            if n2 in edge:
                self._nodes[n1].remove(edge)
                break
        else:
            raise (ValueError)

    def has_node(self, n):
        """.Check if node is in graph."""
        return True if n in self._nodes else False

    def neighbors(self, n):
        """Return list of neighbors nodes to node n."""
        neighbors_list = []
        for edge in self._nodes[n]:
            neighbors_list.append(edge[0])
        return neighbors_list

    def adjacent(self, n1, n2):
        """Return True if n1 and n2 are adjacent to each other."""
        if not self.has_node(n1) or not self.has_node(n2):
            raise(KeyError)
        for edge in self._nodes[n1]:
            if n2 in edge[0]:
                return True
        return False

    def depth_first_traversal(self, start):
        """Launch a dfs search, exploring all nodes."""
        s = Stack()
        self._visited = []
        self._explore(start, s)
        return self._visited

    def _explore(self, node, stack):
        """Explore a given node, updated visited and stack and calls itself with a new unvisited node."""
        # import pdb; pdb.set_trace()
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
        self._visited = []
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
            while len(queue):
                try:
                    self._explore_bfs(queue.dequeue(), queue)
                except IndexError:
                    return queue
        return queue

# Make Random Graph


def make_random_graph():
    """Make a random graph."""
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
