"""Hash table module...."""


class HashTable(object):
    """Hash table with multiple hashing functions."""

    def __init__(self, size=1024, hash_func='additive'):
        """Set up hash with specified hash function and size."""
        self.size = size
        self.nums = [10, 6, 3, 11, 15]
        self.buckets = []
        for i in range(self.size):
            self.buckets.append([])
        inpt = hash_func.lower()
        if inpt == 'additive':
            self.hash_func = self._additive_hash
        elif inpt.replace('-', '') == 'oneatatime' or inpt == 'oat':
            self.hash_func = self._oat_hash
        elif inpt == 'fnv':
            self.hash_func = self._fnv_hash
        elif inpt == 'custom':
            self.hash_func = self._custom_oat_hash
        else:
            raise NameError("Hash function " + hash_func + " is not an option.")

    def get(self, key):
        """Return the value stored with the given key."""
        startslot = self._hash(key) % self.size

        data = None
        stop = False
        found = False
        position = startslot
        #bad code; needs refactor
        while self.buckets[position] != None and not found and not stop:
            if self.buckets[position] == key:
                found = True
                data = self.buckets[position]
        else:
            position = self.rehash(position, len(self.slots))
            if position == startslot:
                stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.set(key, data)

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
            h += h << 10
            h ^= h >> 6
        h += h << 3
        h ^= h >> 11
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
            h = (h * 16777619) ^ ord(key[i])
        return h

    def _custom_oat_hash(self, key):
        h = 0

        for i in range(len(key)):
            h += ord(key[i])
            h += h << self.nums[0]
            h ^= h >> self.nums[1]
        h += h << self.nums[2]
        h ^= h >> self.nums[3]
        h += h << self.nums[4]

        return h


def findbest(nums=None, loops=100):
    """Try to find better values for the oat hash."""
    from faker import Faker
    import random
    fake = Faker()
    best = 1000
    bestnums = None
    if nums is None:
        nums = [10, 6, 3, 11, 15]
    for i in range(300):
        ht = HashTable(size=600, hash_func='custom')
        ht.nums = nums
        for i in range(loops):
            ht.set(fake.user_name(), i)
        len_empty = len([x for x in ht.buckets if len(x) == 0])
        if len_empty < best:
            best = len_empty
            bestnums = ht.nums[:]
        for idx, num in enumerate(ht.nums):
            if random.randint(0, 1):
                ht.nums[idx] -= random.randint(0, num)
            else:
                ht.nums[idx] += random.randint(0, 9)
        nums = ht.nums[:]
    return bestnums, best


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        from faker import Faker
        fake = Faker()
        ht_add = HashTable()
        ht_oat = HashTable(hash_func='oat')
        ht_fnv = HashTable(hash_func='fnv')
        for i in range(1024):
            ht_add.set(fake.user_name(), i)
            ht_oat.set(fake.user_name(), i)
            ht_fnv.set(fake.user_name(), i)

        len_empty_add = len([x for x in ht_add.buckets if len(x) == 0])
        len_empty_oat = len([x for x in ht_oat.buckets if len(x) == 0])
        len_empty_fnv = len([x for x in ht_fnv.buckets if len(x) == 0])
        max_length_add = len(max(ht_add.buckets, key=lambda x: len(x)))
        max_length_oat = len(max(ht_oat.buckets, key=lambda x: len(x)))
        max_length_fnv = len(max(ht_fnv.buckets, key=lambda x: len(x)))

        print('\nHash tables of size 1024, with 1024 key-value pairs:')
        print('\nAdditive hash function:')
        print('Empty buckets: ' + str(len_empty_add))
        print('Largest bucket size: ' + str(max_length_add))
        print('\nOne-at-a-time hash function:')
        print('Empty buckets: ' + str(len_empty_oat))
        print('Largest bucket size: ' + str(max_length_oat))
        print('\nFNV hash function:')
        print('Empty buckets: ' + str(len_empty_fnv))
        print('Largest bucket size: ' + str(max_length_fnv))
