[![Build Status](https://travis-ci.org/wenima/data-structures.svg?branch=hash-table)](https://travis-ci.org/wenima/data-structures)

# Summary

The assignment was to implement a [hash table](https://en.wikipedia.org/wiki/Hash_table)
using 2 hash functions. The first can be a simpler Additive Hash.

The implementation should contain the following

* get(key) - should return the value stored with the given key
* set(key, val) - should store the given val using the given key
* \_hash(key) - should hash the key provided (note that this is an internal api)

# Definition:
A hash table should have the following properties:
* It should be of fixed size. The number of slots in the table should be determined when the table is initialized, by passing an argument: foo = HashTable(1024)
* It should handle hash collisions by using ‘buckets’ to contain any values that share a hash
* It should accept only strings as keys. If a non-string is provided, the ‘set’ method should raise an appropriate Python exception.


For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/hash_table.html


# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing                         |
| -----------------------  | ----- | ---- | ----- | ------------------------------- |
|      hashtable.py        |  104  |  1   | 99%   |  59                             |
| -----------------------  |  ---  |  --  | ----  | ------------------------------- |


# Comments about implementation:

Our goal is to create a hash function that minimizes the number of collisions, is easy to compute, and evenly distributes the items in the hash table. It should not be too complex to become the main part of the storage&search process.

## Different hash functions:
For integers:
* folding method: divide the item into equal size pieces and add these back together.
Using the remainder method, this would create a slot to put in the value.
* mid-square method: square the item, extract some portion of it and use remainder method.
For strings:
* ord method: use the ordinal value on each character, add up the numbers, and find the slot
by using the remainder method.
