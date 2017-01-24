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
|                          |       |      |       |                                 |
|                          |       |      |       |                                 |
| -----------------------  |  ---  |  --  | ----  | ------------------------------- |
| TOTAL                    |       |      |       |                                 |


# Comments about implementation:
