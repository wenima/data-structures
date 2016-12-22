#Summary

The assignment was to implement a [Priority Queue](https://en.wikipedia.org/wiki/Priority_queue)
in Python containing 3 methods:

* insert(value): inserts a value into the queue. Takes an optional argument for that value’s priority, set by default to whatever your lowest        priority is (i.e. 0, -99, whatever).
* pop(): removes the most important item from the queue.
* peek(): returns the most important item without removing it from the queue.

For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/priority_queue.html


# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing |
| -----------------------  | ----- | ---- | ----- | ------- |
| binheap.py               |  49   |  0   | 100%  |         |
| test_binheap.py          |  74   |  0   | 100%  |         |
| -----------------------  |  ---  |  --  | ----  | ------- |
| TOTAL                    |  123  |  0   | 100%  |         |


# Comments about implementation:

* still looking for ways to improve tests and make them more concise
* fixed a bug in the implementation where the init method did not only reorganize once the passed in iterable was exhausted
