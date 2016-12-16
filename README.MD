#Summary

The assignment was to implement a [Queue](https://codefellows.github.io/sea-python-401d5/assignments/queue.html)
in Python containing 6 methods:

* enqueue(value): adds value to the queue
* dequeue(): removes the correct item from the queue and returns its value (should raise an error if the queue is empty)
* peek(): returns the next value in the queue without dequeueing it. If the queue is empty, returns None
* size(): return the size of the queue. Should return 0 if the queue is empty.

For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/queue.html



# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing |
| -----------------------  | ----- | ---- | ----- | ------- |
| dbl_linked_list.py       |  75   |  0   | 100%  |         |
| linked_list.py           |  50   |  0   |  96%  |  80-81  |
| queue.py                 |  22   |  2   | 91%   |  47, 51 |
| stack.py                 |   8   |  0   | 100%  |         |
| test_dbl_linked_list.py  |  185  |  0   | 100%  |         |
| test_linked_list.py      |  73   |  0   |  95%  |         |
| test_queue.py            |  87   |  0   | 100%  |         |
| test_stack.py            |  48   |  0   | 100%  | 106-109 |
| -----------------------  |  ---  |  --  | ----  | ------- |
| TOTAL                    |  552  |  8   | 99%   |         |


# Thoughts on when to use a queue vs a doubly_linked_list:
 * When you explicity want to add to the end of a list and remove from the top (e.g. a task list)


# Comments about implementation:
 * Had to make a decision at the beginning on whether or not to maintain the head/tail convention of the doubly linked list.  Once we made that decision, we needed to find a way to reverse any iterables that are passed in on intialization of a new queue.
