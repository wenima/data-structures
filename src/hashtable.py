"""Hash table module...."""


class HashTable(object):
    """Hash table with multiple hashing functions."""

    def __init__(self, size=1024, hash_func='additive'):
        """Set up hash with specified hash function and size."""
        self.size = size
        self.buckets = []
        for i in range(self.size):
            self.buckets.append([])
        inpt = hash_func.lower()
        if inpt == 'additive':
            self.hash_func = self._additive_hash
        elif inpt.replace('-', '') == 'oneatatime' or inpt == 'oat':
            self.hash_func = self._oat_hash
        elif inpt == '':
            self.hash_func = self._
        else:
            raise NameError("Hash function " + hash_func + " is not an option.")

    def get(self, key):
        """Return the value stored with the given key."""

    def set(self, key, val):
        """Store the given val using the given key."""
        if type(key) is str:
            idx = self._hash(key) % self.size
            self.buckets[idx].append(val)

    def _hash(self, key):
        """Hash the provided key."""
        return self.hash_func(key)

    def _oat_hash(self, key):
        h = 0

        for i in range(len(key)):
            h += ord(key[i])
            h += h << 1024
            h = h ^ (h >> 6)
        h += h << 3
        h = h ^ (h >> 11)
        h += h << 15

        return h
