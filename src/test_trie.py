"""Unit tests for Ternary Search Trie."""

import pytest
import types


TEST_TST_INSERT = [
    #insert into the TEST, giving a string and check for no. of leaves and
    #size (no of unique chars in the path to a word represents a node)
    # ('sea'), [3],
    # ('sea shells', [8]),
    # ('the quick brown fox jumped over the lazy dog'),
    # ('sea shells by the ocean with sand'),
    ('sea shells from the seaside by the ocean with sand surrounded by seahawks\
    sitting on top of sandcastles and sanddunes')
    ]

TEST_TST = [
(3),
(8),
(36),
]

# TEST_TST = [
# (1, [3]),
# (2, [8]),
# (8, [36]),
# ]

TEST_HASHES = [
# ('sea', [313]),
('sea shells by the ocean', [313, 651, 219, 321, 518]),
('the quick brown fox jumped over the lazy dog', [321, 541, 552, 333, 645, 444, 321, 448, 314]),
('zzzyyyyccc zz zzaazz qwerstsbt rrraaarrr racecar a', [1147, 244, 682, 1007, 975, 721, 97]),
]

@pytest.fixture
def create_empty_node():
    """Return an empty node."""
    from trie import TreeNode
    new_node = TreeNode()
    return new_node

@pytest.fixture
def empty_tst():
    """Return empty tst."""
    from trie import TST
    empty_tst = TST()
    return empty_tst

@pytest.fixture(params=TEST_TST_INSERT)
def tst(request):
    from trie import TST
    new_tst = TST(request.param)
    return new_tst


def test_create_empty_treenode(create_empty_node):
    """Test creation of an empty node."""
    assert create_empty_node.hash is None
    assert create_empty_node.left is None
    assert create_empty_node.right is None
    assert create_empty_node.center is None
    assert create_empty_node.parent is None
    assert create_empty_node.char is ''


def test_insert_at_end_of_tree(empty_tst):
    """Test insert node at end of tree."""
    empty_tst.insert('xyz')
    assert empty_tst.contains('xyz')
    assert empty_tst._size == 3


@pytest.mark.parametrize('sentence, result', TEST_HASHES)
def test_hash_values_are_correct_and_present(sentence, result, empty_tst):
    """Test hash values are correct and present in the tree."""
    empty_tst.insert(sentence)
    assert [empty_tst._find_furthest(w)[0].hash for w in sentence.split()] == result



# @pytest.mark.parametrize('nodes', TEST_TST)
def test_inserts_multiple_words(tst):
    """Test of insertion into the tree using different inputs."""
    children_val = [c.char for c in tst.root.children()]
    assert tst.root.char is not None
    # assert sorted(['b', 'e', 't']) == sorted(children_val)
    assert sorted(['e', 'f', 't']) == sorted(children_val)
    assert tst.root.char == 's'
