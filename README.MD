#Summary

The assignment was to implement a [Deque](https://codefellows.github.io/sea-python-401d5/assignments/deque.html)
in Python containing 7 methods:

* append(val): adds value to the end of the deque
* appendleft(val): adds a value to the front of the deque
* pop(): removes a value from the end of the deque and returns it (raises an exception if the deque is empty)
* popleft(): removes a value from the front of the deque and returns it (raises an exception if the deque is empty)
* peek(): returns the next value that would be returned by pop but leaves the value in the deque (returns None if the deque is empty)
* peekleft(): returns the next value that would be returned by popleft but leaves the value in the deque (returns None if the deque is empty)
* size(): returns the count of items in the queue (returns 0 if the queue is empty)

For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/doubly_linked_list.html


# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing |
| -----------------------  | ----- | ---- | ----- | ------- |
| dbl_linked_list.py       |  80   |  0   | 100%  |         |
| deque.py                 |  26   |  0   | 100%  |         |
| test_deque.py            |   8   |  0   | 100%  |         |
| -----------------------  |  ---  |  --  | ----  | ------- |
| TOTAL                    |  114  |  0   | 100%  |         |


# Comments about implementation:

* still looking for ways to improve tests and make them more concise
