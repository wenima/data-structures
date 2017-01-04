"""Test the implementation of a simple graph."""

import pytest
import string
import random

simple_graph_scaffold = {
                        'A': ['B', 'C'],
                        'B': ['C', 'D'],
                        'C': ['D'],
                        'D': ['C'],
                        'E': ['F'],
                        'F': ['C']
                        }

nodes_scaffold_dag = {
                'A': ['B', 'D'],
                'B': ['C', 'G'],
                'C': [],
                'D': ['E', 'F', 'I'],
                'E': ['H', 'I'],
                'F': ['G'],
                'G': ['H'],
                'H': [],
                'I': [],
                'X': ['Y'],
                'Y': ['Z'],
                'Z': ['X'],
                }

DEPTH_TABLE = [
    ('A', ['A', 'B', 'C', 'G', 'H', 'D', 'E', 'I', 'F']),
    ('B', ['B', 'C', 'G', 'H']),
    ('C', ['C']),
    ('D', ['D', 'E', 'H', 'I', 'F', 'G']),
    ('E', ['E', 'H', 'I']),
    ('F', ['F', 'G', 'H']),
    ('G', ['G', 'H']),
    ('H', ['H']),
    ('I', ['I']),
    ('X', ['X', 'Y', 'Z']),
    ('Y', ['Y', 'Z', 'X']),
    ('Z', ['Z', 'X', 'Y']),
]

BREADTH_TABLE = [
    ('A', ['A', 'B', 'D', 'C', 'G', 'E', 'F', 'I', 'H']),
    ('B', ['B', 'C', 'G', 'H']),
    ('C', ['C']),
    ('D', ['D', 'E', 'F', 'I', 'H', 'G']),
    ('E', ['E', 'H', 'I']),
    ('F', ['F', 'G', 'H']),
    ('G', ['G', 'H']),
    ('H', ['H']),
    ('I', ['I']),
    ('X', ['X', 'Y', 'Z']),
    ('Y', ['Y', 'Z', 'X']),
    ('Z', ['Z', 'X', 'Y']),
]

def build_graph(d, weight=0):
    from simple_graph import Graph
    weighted_g = Graph()
    for k, v in d.items():
        for edge in v:
            weighted_g.add_edge(k, edge, weight)
    return weighted_g

def make_random_graph():
    from simple_graph import Graph
    rnd_g = Graph()
    for i in range(1, random.randint(1, 100)):
        try:
            rnd_g.add_edge(i, random.randint(1, 100))
        except ValueError:
            pass
    return rnd_g


@pytest.fixture
def g_empty():
    """Fixture for empty pq."""
    from simple_graph import Graph
    new_g = Graph()
    return new_g


@pytest.fixture
def g1():
    """Fixture for graph containing a single element, no edges."""
    from simple_graph import Graph
    new_g = Graph()
    new_g.add_node('A')
    return new_g


@pytest.fixture
def g():
    """Fixture for graph containing multiples nodes with multiples edges."""
    from simple_graph import Graph
    new_g = build_graph(simple_graph_scaffold)
    return new_g


@pytest.fixture
def dag():
    """Fixture for direct acyclic graph."""
    from simple_graph import Graph
    new_g = build_graph(nodes_scaffold_dag)
    return new_g

@pytest.fixture
def weighted_dag():
    """Fixture for direct acyclic graph with all weights set to a value."""
    from simple_graph import Graph
    new_g = build_graph(nodes_scaffold_dag, 1)
    return new_g

@pytest.fixture
def random_graph():
    """Fixture to provide a randomly created graph."""
    new_g = make_random_graph()
    return new_g

def test_create_empty_g(g_empty):
    """Test creation of empty Graph."""
    assert len(g_empty._nodes) == 0


def test_adding_node(g_empty):
    """Test adding a node to an empty Graph and calling the node method of class Graph."""
    g_empty.add_node('A')
    assert 'A' in g_empty.nodes()
    assert len(g_empty._nodes) == 1


def test_adding_edge_to_empty_graph(g_empty):
    """Test that adding an edge to empty graph adds new nodes if they don't exist and tests that calling all nodes works."""
    new_nodes = ['A', 'B']
    g_empty.add_edge('A', 'B')
    for n in new_nodes:
        assert n in g_empty._nodes.keys()
    assert len(g_empty._nodes) == 2

# parametrize the next tests into the one above


def test_adding_edge_to_graph_w_1_node(g1):
    """Test that adding an edge to empty graph adds new node where one of the 2 doesn't exist."""
    new_nodes = ['A', 'B']
    g1.add_edge('A', 'B')
    for n in new_nodes:
        assert n in g1._nodes.keys()
    node, weight = g1._nodes['A'][0]
    assert len(g1._nodes) == 2
    assert node == 'B'


def test_egdges_returns_all_edges(g):
    """Test that calling class method edges returns all edges."""
    edges = g.edges()
    assert ['A-B', 'A-C', 'C-D'] not in edges
    assert 'B-A' not in edges


def test_delete_node_raises_error_if_node_doesn_exist(g1):
    """Test that deleting a node which doesn't exist raises an error message of type KeyError."""
    with pytest.raises(KeyError):
        g1.del_node('B')


def test_delete_node_removed_from_graph(g1):
    """Test that deleting a node removes it from the graph structure."""
    g1.add_edge('A', 'C')
    g1.del_node('A')
    result = 'A' in g1._nodes.keys()
    assert len(g1._nodes) == 1
    assert g1._nodes['C'] == []  # figure out why can't be is False
    assert g1.has_node('C')
    assert result is False


def test_delete_node_removed_from_all_nodes(g):
    """Test that deleting a node deletes it from all edges."""
    g.del_node('C')
    assert 'C' not in g.nodes()

def test_delete_node_removed_from_all_nodes_in_random_graph(random_graph):
    """Test that deleting a node deletes it from all edges."""
    if random_graph.neighbors(1):
        random_graph.del_node(1)
    assert 1 not in random_graph.nodes()


def test_delete_edge_deletes_edge_or_raises_error_if_not_exist(g):
    """Test that deleting an edge raises a ValueError if the edge doesn't exist."""
    g.del_edge('A', 'B')
    node, weight = g._nodes['A'][0]
    assert node == 'C'
    with pytest.raises(ValueError):
        g.del_edge('A', 'F')


def test_neighbors_returns_correct_list(g):
    """Test that neighbors returns the correct list."""
    assert g.neighbors('B') == ['C', 'D']
    with pytest.raises(KeyError):
        g.neighbors('Z')


def test_adjacent(g):
    """Test that adjacent returns correct value."""
    assert g.adjacent('B', 'C') is True
    assert g.adjacent('D', 'A') is False
    with pytest.raises(KeyError):
        g.adjacent('Z', 'A')


# Testing for Depth First Search


def test_dfs_on_node_with_no_edges(g1):
    """Test that depth first search on node with no edges returns only node."""
    assert g1.depth_first_traversal('A') == ['A']


@pytest.mark.parametrize('start, result', DEPTH_TABLE)
def test_depth_first_on_dag(dag, start, result):
    """Test on depth first search on directed acyclic and cyclic graphs."""
    assert dag.depth_first_traversal(start) == result


@pytest.mark.parametrize('start, result', BREADTH_TABLE)
def test_breadth_first_on_dag(dag, start, result):
    """Test on breadth first search on directed acyclic and cyclic graphs."""
    assert dag.breadth_first_traversal(start) == result

def test_edges_have_weights(weighted_dag):
    """Test that every edge has a weight assigned."""
    error = False
    all_weights = []
    sum_weight = 0
    for we in weighted_dag.edges():
        try:
            all_weights.append(we[-1])
            sum_weight += float(we[-1])
        except ValueError:
            error = True
            raise ValueError('Missing weight')
    assert sum_weight == len(all_weights)
    assert error == False
