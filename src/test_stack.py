"""Testing the linked_list class - CF 401 Python Week 2 Assignment."""
import pytest

@pytest.fixture
def new_empty_stack():
    """Create an empty object of type Stack to be used in test functions."""
    from stack import Stack
    this_stack = Stack()
    return this_stack


@pytest.fixture
def stack_123():
    """Return a object of type Stack containing 3 nodes with values 1, 2, 3."""
    from stack import Stack
    this_stack = Stack([1, 2, 3])
    return this_stack


def test_create_new_empty_Stack_out_of_Linked_List():
    """Test if a new object of type Stack gets instantiated correctly."""
    from stack import Stack
    new_stack = Stack()
    assert new_stack._container.head is None


def test_create_empty_Linked_List():
    """Test if a new empty object of type Stack gets created correctly."""
    from linked_list import Linked_List
    new_list = Linked_List()
    assert new_list.head is None


def test_empty_new_node_object_has_none():
    """Test the emptyiness of a node."""
    from linked_list import Node
    new_node = Node()
    assert new_node.value is None
    assert new_node.nxt is None


def test_new_node_has_data():
    """Test if a new node is correctly created with data."""
    from linked_list import Node
    new_node = Node("five")
    assert new_node.value == "five"


def test_when_initialized_with_iterable_makes_nodes():
    """Test if the number of nodes matches the number of elements passed with
    the iterable."""
    from stack import Stack
    my_nodes = [1, 2, 3]
    new_stack = Stack(my_nodes)
    assert len(new_stack._container) == 3


def test_that_pop_fails_when_called_on_empty_stack(new_empty_stack):
    """Test that calling pop on empty Stack raises an exception."""
    from stack import Stack
    with pytest.raises(IndexError):
        new_empty_stack.pop()


def test_that_pop_removes_the_head(stack_123):
    """Test that Stack.pop() removes the top element of the Stack"""
    from stack import Stack
    stack_123.pop()
    assert len(stack_123._container) == 2


def test_that_push_adds_on_top_of_existing_stack(stack_123):
    """Test that Stack.push() adds on top of an existing stack"""
    from stack import Stack
    stack_123.push(4)
    assert stack_123._container.head.value == 4


def test_that_push_adds_on_top_of_an_empty_stack(new_empty_stack):
    """Test that Stack.push() adds on top of an empty stack by moving the head"""
    new_empty_stack._container.head is None
    from stack import Stack
    new_empty_stack.push(1)
    assert new_empty_stack._container.head.value == 1
