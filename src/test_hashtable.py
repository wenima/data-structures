"""Test hashtable get, set, init, and hashing functions."""
import pytest


@pytest.fixture
def test_words(scope='session'):
    """Return a big list of unique words."""
    with open('/usr/share/dict/words', 'r') as phial:
        return phial.read().split()


@pytest.fixture(params=['additive', 'oat', 'fnv', 'custom'])
def hash_table(request):
    """Return hash tables for each hash function."""
    from hashtable import HashTable
    ht = HashTable(hash_func=request.param)
    return ht


def test_ht_initializes_with_correct_num_buckets(hash_table):
    """List of buckets should be initialized to fixed given length."""
    assert len(hash_table.buckets) == 1024


def test_ht_initializes_with_custom_num_buckets():
    """List of buckets should initialize to given size."""
    from hashtable import HashTable
    ht = HashTable(size=433)
    assert len(ht.buckets) == 433


def test_ht_init_raises_error_if_given_hash_not_option():
    """Test error raised if desired hash function is not an option."""
    from hashtable import HashTable
    with pytest.raises(NameError):
        HashTable(hash_func='mnightshamalayan')


def test_hashes_return_numbers(hash_table):
    """Hash functions should return integers."""
    assert type(hash_table.hash_func('key')) is int


def test_set_raises_error_if_key_not_string(hash_table):
    """Set should raise error if given key not a string."""
    with pytest.raises(TypeError):
        hash_table.set(34, 'waka')


def test_set_adds_kv_pair(hash_table):
    """Set should add kv pair to a bucket."""
    hash_table.set('key', 'value')
    assert len([x for x in [y for y in hash_table.buckets if y]]) == 1
    hash_table.set('gretch', 'scd')
    assert sum([len(x) for x in hash_table.buckets]) == 2


def test_set_adds_kv_pair_values(hash_table):
    """Set should add kv pair values, as tuple, to a bucket."""
    hash_table.set('key', 'value')
    assert [x for x in hash_table.buckets if x][0][0] == ('key', 'value')


def test___setitem__adds_kv_pairs(hash_table):
    """Test bracket notation works same as .set."""
    hash_table['key'] = 'value'
    assert len([x for x in [y for y in hash_table.buckets if y]]) == 1
    hash_table['gretch'] = 'scd'
    assert sum([len(x) for x in hash_table.buckets]) == 2


def test__setitem__adds_kv_pair_values(hash_table):
    """Set should add kv pair values, as tuple, to a bucket."""
    hash_table['key'] = 'value'
    assert [x for x in hash_table.buckets if x][0][0] == ('key', 'value')


def test_get_retrieves_right_item(hash_table):
    """Get should return the value paired to given key."""
    hash_table.set('key', 'value')
    assert hash_table.simple_get('key') == 'value'


def test__getitem__retrieves_right_item(hash_table):
    """Get should return the value paired to given key."""
    hash_table.set('key', 'value')
    assert hash_table['key'] == 'value'


def test_get_raises_keyerror_if_key_not_in_table(hash_table):
    """Ht should raise error if given key to get not in table."""
    with pytest.raises(KeyError):
        hash_table['key']


def test_set_overwrites_kv_pair_if_same_key_given(hash_table):
    """Ht should overwrite old kv pair if new pair has same key."""
    hash_table['key'] = 'value'
    hash_table['key'] = 'notvalue'
    assert hash_table['key'] == 'notvalue'
    assert len(hash_table) == 1


def test_len(hash_table):
    """Len should return number of items in hash table."""
    for i in range(30):
        hash_table[str(i)] = 'na' * i
    assert len(hash_table) == 30


def test_findbest():
    """Test findbest returns a list and a number, as a tuple."""
    from hashtable import findbest
    results = findbest(loops=30, ht_size=300)
    assert type(results[0]) is list and len(results[0]) == 5
    assert type(results[1]) is int


# def test_the_words_are_themselves(test_words, hash_table):
#     """Throw a lot (117943) of kvs at a hashtable and see what happens."""
#     array = test_words[:]
#     for i in range(len(test_words)):
#         hash_table[array[i]] = array[i]
#     for i in range(len(test_words)):
#         assert hash_table[array[i]] == array[i]
#     assert len(hash_table) == len(test_words)
#     assert len(hash_table) == sum([len(b) for b in hash_table.buckets])


# def test_the_words(test_words, hash_table):
#     """Throw a lot (117943) of kvs at a hashtable and see what happens."""
#     array = test_words[:]
#     for i in range(0, len(test_words), 2):
#         hash_table[array[i]] = array[i + 1]
#     for i in range(0, len(test_words), 2):
#         assert hash_table[array[i]] == array[i + 1]
