"""Testing the linked_list class - CF 401 Python Week 2 Assignment."""
import pytest

PARAMS_SAMPLE_LIST = ["something", 1, "pear", 3, "apple"]

@pytest.fixture
def init_node():
    from linked_list import Node
    node = Node(0)
    return str(type(node))

@pytest.fixture
def create_empty_node():
    from linked_list import Node
    return Node()

@pytest.fixture
def create_ll_with_list():
    """Given a list, create a new Linked List with all the values."""
    from linked_list import Linked_List
    new_ll = Linked_List(PARAMS_SAMPLE_LIST)
    return new_ll

@pytest.fixture
def create_empty_ll():
    from linked_list import Linked_List
    new_ll = Linked_List()
    return new_ll


def test_node_init():
    """Test the initialization of a node."""
    from linked_list import Node
    assert type(Node) == type


def test_node_instantiation(create_empty_node):
    """Test if the Node objects gets initiated correctly"""
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


def test_linked_list_push():
    """Test the push method of the Linked List class."""
    from linked_list import Linked_List
    new_ll = Linked_List()
    new_ll.push("Something")
    assert new_ll.head.value == "Something" and new_ll._size == 1


def test_linked_list_search_success():
    """Test the search method of the Linked List class with a search query that exists."""
    from linked_list import Linked_List
    new_linked_list = Linked_List(PARAMS_SAMPLE_LIST)
    result = new_linked_list.search('pear')
    assert result.value == 'pear'


def test_linked_list_search_failure():
    """Test the search method of the Linked List class with a search query that DOES NOT exist."""
    from linked_list import Linked_List
    new_linked_list = Linked_List(PARAMS_SAMPLE_LIST)
    result = new_linked_list.search('owt')
    assert result.startswith('That')


def test_linked_list_pop():
    """Test the pop method of the Linked List class."""
    from linked_list import Linked_List
    new_ll = Linked_List(PARAMS_SAMPLE_LIST)
    old_head_val = new_ll.head.value
    new_ll.pop()
    new_head_val = new_ll.head.value
    assert old_head_val == "apple" and new_head_val == 3


def test_linked_list_display():
    """Test the display method of the Linked_List class."""
    from linked_list import Linked_List
    new_linked_list = Linked_List(["something", "something else", "two"])
    result = "('two', 'something else', 'something')"
    assert new_linked_list.display() == result


def test_linked_list_size():
    """Test if the size method of the Linked_List class returns the size
    correctly by independently iterating over the the linked list"""
    from linked_list import Linked_List
    test_l = len(PARAMS_SAMPLE_LIST)
    new_linked_list = Linked_List(PARAMS_SAMPLE_LIST)
    assert new_linked_list._size == test_l
    assert len(new_linked_list) == test_l
    assert new_linked_list.size() == test_l


def test_linked_list_remove_node_exists():
    """Test if the remove method of the Linked_List class is correctly
    removing a node"""
    from linked_list import Linked_List
    ll = Linked_List(PARAMS_SAMPLE_LIST)
    r_node = ll.search("pear")
    ll.remove(r_node)
    assert ll.size() == 4
    #result.startswith("Success")


def test_linked_list_remove_node_not_exists():
    """Test if the remove method of the Linked_List class is correctly behaving
    if the node does not exist"""
    from linked_list import Linked_List
    ll = Linked_List(PARAMS_SAMPLE_LIST)
    with pytest.raises(ValueError):
        r_node = Node("bear")
        ll.remove(r_node)
    
