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
| binheap.py               |  51   |  0   | 100%  |         |
| priorityq.py             |  24   |  0   | 100%  |         |
| test_binheap.py          |  74   |  0   | 100%  |         |
| test_pq.py               |  42   |  0   | 100%  |         |
| -----------------------  |  ---  |  --  | ----  | ------- |
| TOTAL                    |  191  |  0   | 100%  |         |


# Comments about implementation:

* we initialize the list with the first value set to 0 per the request of my partner.
* we did not set a default value for priority yet as this assignment was changed later on. For now, it's referenced in GitHub: https://github.com/wenima/data-structures/issues/52
* after some discussion, we decided to go with my proposal of setting a the index inside the tuple in the list as a way to solve the case where 2 items have the same priority
