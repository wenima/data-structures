"""Test hashtable get, set, init, and hashing functions."""
import pytest


@pytest.fixture
def additive_ht():
    """Return hash table with additive hash function."""
    from hashtable import HashTable
    ht = HashTable()
    return ht


@pytest.fixture
def oat_ht():
    """Return hash table with one-at-a-time hash function."""
    from hashtable import HashTable
    ht = HashTable(hash_func='oat')
    return ht


@pytest.fixture
def fnv_ht():
    """Return hash table with FNV hash function."""
    from hashtable import HashTable
    ht = HashTable(hash_func='fnv')
    return ht


@pytest.fixture(params=['additive', 'oat', 'fnv'])
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


def test_hashes_return_numbers(hash_table):
    """Hash functions should return integers."""
    assert type(hash_table.hash_func('key')) is int


