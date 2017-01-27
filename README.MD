# Summary

The assignment was to implement a [trie](https://en.wikipedia.org/wiki/Trie)
as a class with 4 public methods:

* insert(self, string): will insert the input string into the trie. If character in the input string is already present, it will be ignored.
* contains(self, string): will return True if the string is in the trie, False if not.
* size(self): will return the total number of words contained within the trie. 0 if empty.
* remove(self, string): will remove the given string from the trie. If the word doesn’t exist, will raise an appropriate exception.


# Definition:
A trie is a tree data structure in which the root holds references to all following characters eventually leading down
to leaves which either hold the complete string or the end is signaled by '$'. Trie nodes can have the following representations:
* an array
* a Binary-Search-Tree
* a hash-table

For more information on the assignment, see here:
https://codefellows.github.io/sea-python-401d5/assignments/trie_implementation.html


# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing                         |
| -----------------------  | ----- | ---- | ----- | ------------------------------- |
|                          |       |      |       |                                 |
|                          |       |      |       |                                 |
| -----------------------  |  ---  |  --  | ----  | ------------------------------- |
| TOTAL                    |       |      |       |                                 |


# Comments about implementation:

For all implementations, the assignment also requires to state the time and space complexity.
