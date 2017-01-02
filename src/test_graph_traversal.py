"""Test the implementation of a graph traversal"""

import pytest

@pytest.fixture
def g_empty():
    """Fixture for an empty Graph object."""
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
                    'A': ['E', 'B', 'C'],
                    'B': ['D', 'A'],
                    'C': ['D', 'A'],
                    'D': ['C', 'E', 'B'],
                    'E': ['A', 'D']
                    }
    return new_g

@pytest.fixture
def new_empty_stack():
    """Create an empty object of type Stack to be used in test functions."""
    from stack import Stack
    this_stack = Stack()
    return this_stack
