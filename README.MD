# Summary

The assignment was to implement a [Linked List](https://en.wikipedia.org/wiki/linked_list)
in Python containing 6 methods:

* push(val) will insert the value ‘val’ at the head of the list
* pop() will pop the first value off the head of the list and return it.
* size() will return the length of the list
* search(val) will return the node containing ‘val’ in the list, if present, else None
* remove(node) will remove the given node from the list, wherever it might be (node must be an item in the list)
* display() will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”

For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/linked_list.html


# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                | Stmts | Miss | Cover | Missing |
| ------------------- | ----- | ---- | ----- | ------- |
| linked_list.py      |  47   |  0   | 100%  |         |
| stack.py            |   8   |  0   | 100%  |         |
| test_linked_list.py |  47   |  0   | 100%  |         |
| test_stack.py       |  47   |  0   | 100%  |         |
| --------------      |  ---  |  --  | ----  | ------- |
| TOTAL               |  174  |  0   | 100%  |         |



# Comments about implementation:

* the linked_list.py module contains two "helper" functions. ```python _iterate_from()``` takes in a list object from which to iterate (usually head) and returns an iterable which then can be used in different ways, one of them is ```_node_values``` which uses list comprehension to return a list containing all values/data of all the nodes.
