"""Testing for dijkstra's algorithm."""


import pytest

TEST_ONE = {
    'a': [('b', 7), ('c', 9), ('f', 14)],
    'b': [('c', 10), ('d', 15)],
    'c': [('d', 11), ('f', 2)],
    'd': [('e', 6)],
    'e': [],
    'f': [('e', 9)],
}

TEST_TWO = {
    'a': [('b', 9), ('c', 3), ('d', 10)],
    'b': [('e', 1)],
    'c': [('e', 7), ('d', 2)],
    'd': [('f', 2), ('g', 5)],
    'e': [('f', 1), ('h', 3)],
    'f': [('h', 3)],
    'g': [('h', 7)],
    'h': [],
}

TEST_THREE = {
    'a': [('b', 5), ('c', 1)],
    'b': [('a', 2), ('d', 5)],
    'c': [('e', 2), ('b', 2)],
    'd': [('f', 2)],
    'e': [('f', 11)],
    'f': [],
}


@pytest.fixture
def graph_one():
    """Graph based on TEST_ONE."""
    from simple_graph import Graph
    g = Graph()
    g._nodes = TEST_ONE
    return g


@pytest.fixture
def graph_two():
    """Graph based on TEST_TWO."""
    from simple_graph import Graph
    g = Graph()
    g._nodes = TEST_TWO
    return g


@pytest.fixture
def graph_three():
    """Graph based on TEST_THREE."""
    from simple_graph import Graph
    g = Graph()
    g._nodes = TEST_THREE
    return g


def test_start_node_must_be_in_graph(graph_one):
    """Test that a node not in graph throws error."""
    with pytest.raises(TypeError):
        graph_one.dijkstras('z', 'b')


def test_end_node_must_be_in_graph(graph_one):
    """Test that a node not in graph throws error."""
    with pytest.raises(TypeError):
        graph_one.dijkstras('a', 'z')


def test_dijkstra_works_on_simple_graph(graph_one):
    """Test on a simple graph."""
    assert graph_one.dijkstras('a', 'e') == (20, ['a', 'c', 'f', 'e'])


def test_dijkstra_works_on_simple_graph_two(graph_two):
    """Test on a simple graph again."""
    assert graph_two.dijkstras('a', 'h') == (10, ['a', 'c', 'd', 'f', 'h'])


def test_dijkstra_works_on_simple_graph_three(graph_three):
    """Test on a simple graph with edges that point back to start."""
    assert graph_three.dijkstras('a', 'f') == (10, ['a', 'c', 'b', 'd', 'f'])

