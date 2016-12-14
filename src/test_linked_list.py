"""Testing the linked_list class - CF 401 Python Week 2 Assignment."""
import pytest
import random

PARAMS_SAMPLE_LIST = ["something", 1, "pear", 3, "apple"]
sample_from_the_midde_of_iterable = random.choice(PARAMS_SAMPLE_LIST[1:len(PARAMS_SAMPLE_LIST) - 1])

REMOVE_TESTS = [
    (PARAMS_SAMPLE_LIST[0], "Succesfully removed Node with value: something"), #PARAMS_SAMPLE_LIST[0]
    (sample_from_the_midde_of_iterable, "Succesfully removed Node with value: {0}".format(sample_from_the_midde_of_iterable)),
    (PARAMS_SAMPLE_LIST[len(PARAMS_SAMPLE_LIST) - 1], "Succesfully removed Node with value: apple. New head set to 3"),
]


@pytest.fixture
def create_empty_node():
    from linked_list import Node
    return Node()

@pytest.fixture
def new_ll():
    """Given a list, create a new Linked List with all the values."""
    from linked_list import Linked_List
    this_ll = Linked_List(PARAMS_SAMPLE_LIST)
    return this_ll

@pytest.fixture
def new_empty_ll():
    """Create an empty object of type Stack to be used in test functions."""
    from linked_list import Linked_List
    this_empty_ll = Linked_List()
    return this_empty_ll


def test_node_init():
    """Test the initialization of a node."""
    from linked_list import Node
    assert type(Node) == type


def test_node_instantiation(create_empty_node):
    """Test if the Node objects gets initiated correctly."""
    from linked_list import Node
    assert create_empty_node.value is None


def test_node_value():
    """Test the contents of nodes created with given input."""
    from linked_list import Node
    node2 = Node("Something")
    assert node2.value == "Something" and node2.nxt == None


def test_linked_list_init():
    """Test initialization of the linked_list."""
    from linked_list import Linked_List
    assert type(Linked_List) == type


def test_linked_list_push(new_empty_ll):
    """Test the push method of the Linked List class."""
    from linked_list import Linked_List
    new_empty_ll.push("Something")
    assert new_empty_ll.head.value == "Something" and new_empty_ll._size == 1


def test_linked_list_search_success(new_ll):
    """Test the search method of the Linked List class with a search query that exists."""
    from linked_list import Linked_List
    result = new_ll.search('pear')
    assert result.value == 'pear'


def test_linked_list_search_failure(new_ll):
    """Test the search method of the Linked List class with a search query that DOES NOT exist."""
    from linked_list import Linked_List
    result = new_ll.search('owt')
    assert result is None


def test_linked_list_pop(new_ll):
    """Test the pop method of the Linked List class."""
    from linked_list import Linked_List
    old_head_val = new_ll.head.value
    new_ll.pop()
    new_head_val = new_ll.head.value
    assert new_head_val == 3

def test_pop_from_empty_list(new_empty_ll):
    """Tests behaviour of Linked_List.pop function when executed on empty
    linked list."""
    from linked_list import Linked_List
    with pytest.raises(IndexError):
        new_empty_ll.pop()


def test_linked_list_display(new_ll):
    """Test the display method of the Linked_List class."""
    from linked_list import Linked_List
    result = str(("apple", 3, "pear", 1, "something"))
    assert new_ll.display() == result


def test_linked_list_size(new_ll):
    """Test if the size method of the Linked_List class returns the size
    correctly by independently iterating over the the linked list."""
    from linked_list import Linked_List
    assert new_ll._size == len(PARAMS_SAMPLE_LIST)
    assert len(new_ll) == len(PARAMS_SAMPLE_LIST)
    assert new_ll.size() == len(PARAMS_SAMPLE_LIST)


@pytest.mark.parametrize('s , out', REMOVE_TESTS)
def test_linked_list_remove_node_exists(s, out):
    """Test if the remove method of the Linked_List class is correctly
    removing the head of a linked list."""
    from linked_list import Linked_List
    new_ll = Linked_List(PARAMS_SAMPLE_LIST)
    assert new_ll.remove(s) == out


def test_linked_list_remove_node_not_exists(new_ll):
    """Test if the remove method of the Linked_List class is correctly behaving
    if the node does not exist."""
    from linked_list import Linked_List, Node
    r_node = Node("bear")
    with pytest.raises(ValueError):
        new_ll.remove(r_node)


def test_lined_list_create_with_non_iterable():
    """Test that passing a non iterable gets still added as a node."""
    from linked_list import Linked_List
    new_linked_list = Linked_List(-100)
    assert new_linked_list.head.value == -100
