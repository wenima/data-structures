"""Test the implementation of a simple graph"""

import pytest

TEST_GRAPH_V_E = {
                'A': ['B', 'C'],
                'B': ['C', 'D'],
                'C': ['D'],
                'D': ['C'],
                'E': ['F'],
                'F': ['C']
                }

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
    new_g._nodes = TEST_GRAPH_V_E
    return new_g

def test_create_empty_g(g_empty):
    """Test creation of empty Graph."""
    assert len(g_empty._nodes) == 0

def test_adding_node(g_empty):
    """Test adding a node to an empty Graph."""
    g_empty.add_node('A')
    assert 'A' in g_empty._nodes.keys()
    assert len(g_empty._nodes) == 1

def test_adding_edge_to_empty_graph(g_empty):
    """Test that adding an edge to empty graph adds new nodes if they don't
    exist and tests that calling all nodes works."""
    new_nodes = ['A', 'B']
    g_empty.add_edge('A', 'B')
    for n in new_nodes:
        assert n in g_empty._nodes.keys()
    assert len(g_empty._nodes) == 2
    assert g_empty._nodes['B'] == ['A']

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



def test_delete_edge_deletes_edge_or_raises_error_if_not_exist(g):
    """Test that deleting an edge raises a ValueError if the edge doesn't exist.
    """
    g.del_edge('A', 'B')
    assert g._nodes['A'] == ['C']
    with pytest.raises(ValueError):
        g1.del_edge('A', 'F')

def test_neighbors_returns_correct_list(g):
    """Test that neighbors returns the correct list"""
    assert g.neighbors('B') == ['C', 'D']
    with pytest.raises(KeyError):
        g.neighbors('Z')

# def test_neighbors_raises_error(g):
#     """Test that calling neighbors when node does not exist returns an error"""
#     with pytest_ra

def test_adjacent(g):
    """Test that adjacent returns correct value"""
    assert g.adjacent('B', 'C') == True
    assert g.adjacent('D', 'A') == False
    with pytest.raises(KeyError):
        g.adjacent('Z', 'A')
