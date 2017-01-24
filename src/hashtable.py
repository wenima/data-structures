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
        elif inpt == 'fnv':
            self.hash_func = self._fnv
        else:
            raise NameError("Hash function " + hash_func + " is not an option.")

    def get(self, key):
        """Return the value stored with the given key."""

    def set(self, key, val):
        """Store the given val using the given key."""
        bucket = self._get_bucket(key)
        idx = self._find_idx(key, bucket)
        if idx is not None:
            bucket[idx] = (key, val)
        else:
            bucket.append((key, val))

    def _get_bucket(self, key):
        idx = self._hash(key) % self.size
        return self.buckets[idx]

    def _find_idx(self, key, bucket):
        for idx, kv_pair in enumerate(bucket):
            if kv_pair[0] == key:
                return idx
        return

    def _hash(self, key):
        """Hash the provided key."""
        if type(key) is str:
            return self.hash_func(key)
        else:
            raise TypeError('Key must be a string.')

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

    def _additive_hash(self, key):
        h = 0
        for i in range(len(key)):
            h += ord(key[i])
        return h

    def _fnv_hash(self, key):
        h = 2166136261
        for i in range(len(key)):
            h = (h * 16777619) ^ key[i]
        return h


if __name__ == '__main__':
    ht_add = HashTable()
    ht_oat = HashTable(hash_func='oat')
    ht_fnv = HashTable(hash_func='fnv')