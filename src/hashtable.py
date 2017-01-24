"""Hash table module...."""


class HashTable(object):
    """Hash table with multiple hashing functions."""

    def __init__(self, size=1024, hash_func='additive'):
        """Set up hash with specified hash function and size."""
        self.size = size
        self.buckets = []
        for i in range(self.size):
            self.buckets.append([])
        if hash_func.lower() == 'additive':
            self.hash_func = self._additive
        elif hash_func.lower().replace('-', '') == 'oneatatime':
            self.hash_func = self._one_at_a_time
        elif hash_func.lower() == 'fnv':
            self.hash_func = self._fnv
        else:
            raise NameError("Hash function " + hash_func + " is not an option.")

    def get(self, key):
        """Return the value stored with the given key."""

    def set(self, key, val):
        """Store the given val using the given key."""

    def _hash(self, key):
        """Hash the provided key."""
