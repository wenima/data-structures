"""Test the implementation of a simple graph"""

import pytest

@pytest.fixture
def new_empty_stack():
    """Create an empty object of type Stack to be used in test functions."""
    from stack import Stack
    this_stack = Stack()
    return this_stack

@pytest.fixture
def g_empty():
    """Fixture for empty pq."""
    from simple_graph import Graph
    new_g = Graph()
    return new_g

@pytest.fixture
def g1():
    """Fixture for graph containing a single element, no edges"""
    from simple_graph import Graph
    new_g = Graph()
    new_g.add_node('A')
    return new_g

@pytest.fixture
def g():
    """Fixture for graph containing multiples nodes with multiples edges"""
    from simple_graph import Graph
    new_g = Graph()
    new_g._nodes = {
                    'A': ['B', 'C'],
                    'B': ['C', 'D'],
                    'C': ['D'],
                    'D': ['C'],
                    'E': ['F'],
                    'F': ['C']
                    }
    return new_g

@pytest.fixture
def g_traverse():
    """Fixture for graph containing multiples nodes with multiples edges"""
    from simple_graph import Graph
    new_g = Graph()
    new_g._nodes = {
                    'A': ['E', 'B', 'C'],
                    'B': ['D', 'A'],
                    'C': ['D', 'A'],
                    'D': ['C', 'E', 'B'],
                    'E': ['A', 'D']
                    }
    return new_g


@pytest.fixture
def dag():
    """Fixture for direct acyclic graph."""
    from simple_graph import Graph
    new_g = Graph()
    new_g._nodes = {'A': ['B', 'D'],
                    'B': ['C', 'G'],
                    'C': [],
                    'D': ['E', 'F', 'I'],
                    'E': ['H', 'I'],
                    'F': ['G'],
                    'G': ['H'],
                    'H': [],
                    'I': []
                    }
    return new_g

DEPTH_TABLE = [
    ('A', ['A', 'B', 'C', 'G', 'H', 'D', 'E', 'I', 'F']),
    ('B', ['B', 'C', 'G', 'H']),
    ('C', ['C']),
    ('D', ['D', 'E', 'H', 'I', 'F', 'G']),
    ('E', ['E', 'H', 'I']),
    ('F', ['F', 'G', 'H']),
    ('G', ['G', 'H']),
    ('H', ['H']),
    ('I', ['I'])
]


def test_create_empty_g(g_empty):
    """Test creation of empty Graph."""
    assert len(g_empty._nodes) == 0

def test_adding_node(g_empty):
    """Test adding a node to an empty Graph and calling the node method of
    class Graph."""
    g_empty.add_node('A')
    assert 'A' in g_empty.nodes()
    assert len(g_empty._nodes) == 1

def test_adding_edge_to_empty_graph(g_empty):
    """Test that adding an edge to empty graph adds new nodes if they don't
    exist and tests that calling all nodes works."""
    new_nodes = ['A', 'B']
    g_empty.add_edge('A', 'B')
    for n in new_nodes:
        assert n in g_empty._nodes.keys()
    assert len(g_empty._nodes) == 2

#parametrize the next tests into the one above

def test_adding_edge_to_graph_w_1_node(g1):
    """Test that adding an edge to empty graph adds new node where one of the 2
    doesn't exist."""
    new_nodes = ['A', 'B']
    g1.add_edge('A', 'B')
    for n in new_nodes:
        assert n in g1._nodes.keys()
    assert len(g1._nodes) == 2
    assert g1._nodes['A'] == ['B']

def test_egdges_returns_all_edges(g):
    """Test that calling class method edges returns all edges."""
    edges = g.edges()
    assert ['A-B', 'A-C', 'C-D'] not in edges
    assert 'B-A' not in edges

def test_delete_node_raises_error_if_node_doesn_exist(g1):
    """Test that deleting a node which doesn't exist raises an error message of
    type KeyError."""
    with pytest.raises(KeyError):
        g1.del_node('B')

def test_delete_node_removed_from_graph(g1):
    """Test that deleting a node removes it from the graph structure."""
    g1.add_edge('A', 'C')
    g1.del_node('A')
    result = 'A' in g1._nodes.keys()
    assert len(g1._nodes) == 1
    assert g1._nodes['C'] == [] #! figure out why can't be is False
    assert g1.has_node('C')
    assert result == False

def test_delete_node_removed_from_all_nodes(g):
    """Test that deleting a node deletes it from all edges."""
    g.del_node('C')
    assert 'C' not in g._nodes['A']
    assert 'C' not in g._nodes['B']
    assert 'C' not in g._nodes['D']
    assert 'C' not in g._nodes['F']



def test_delete_edge_deletes_edge_or_raises_error_if_not_exist(g):
    """Test that deleting an edge raises a ValueError if the edge doesn't exist.
    """
    g.del_edge('A', 'B')
    assert g._nodes['A'] == ['C']
    with pytest.raises(ValueError):
        g.del_edge('A', 'F')

def test_neighbors_returns_correct_list(g):
    """Test that neighbors returns the correct list."""
    assert g.neighbors('B') == ['C', 'D']
    with pytest.raises(KeyError):
        g.neighbors('Z')

def test_adjacent(g):
    """Test that adjacent returns correct value."""
    assert g.adjacent('B', 'C') == True
    assert g.adjacent('D', 'A') == False
    with pytest.raises(KeyError):
        g.adjacent('Z', 'A')

#Testing for Depth First Search


def test_dfs_on_node_with_no_edges(g1):
    """Test that depth first search on node with no edges returns only node."""
    assert g.depth_first_traversal == ['A']

@pytest.mark.parametrize('start, result', DEPTH_TABLE)
def test_depth_first_on_dag(dag, start, result):
    assert dag.depth_first_traversal(start) == result



# #cyclic
# {
#     'A' : ['B'],
#     'B' : ['C'],
#     'C' : ['D'],
#     'D' : ['A']
# }
