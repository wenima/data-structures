#Summary

The assignment was to implement a [doubly Linked List](https://codefellows.github.io/sea-python-401d5/lectures/double_linked_list.html)
in Python containing 6 methods:

* push(val) will insert the value ‘val’ at the head of the list
* append(val) will append the value ‘val’ at the tail of the list
* pop() will pop the first value off the head of the list and return it.
* shift() will remove the last value from the tail of the list and return it.
* remove(val) will remove the first instance of ‘val’ found in the list, starting from the head. If ‘val’ is not present, it will raise    an  appropriate Python exception.

For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/doubly_linked_list.html


# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | Missing |
| -----------------------  | ----- | ---- | ----- | ------- |
| dbl_linked_list.py       |  75   |  0   | 100%  |         |
| linked_list.py           |  50   |  0   |  96%  |  80-81  |
| stack.py                 |   8   |  0   | 100%  |         |
| test_dbl_linked_list.py  |  185  |  0   | 100%  |         |
| test_linked_list.py      |  73   |  0   |  95%  |         |
| test_stack.py            |  48   |  0   | 100%  | 106-109 |
| -----------------------  |  ---  |  --  | ----  | ------- |
| TOTAL                    |  439  |  6   | 99%   |         |


# Comments about implementation:

* the keeping state of size of the object is not optimal and it would be better to call it in it own function
* one test has been commented out due to difference of opinion https://github.com/wenima/data-structures/issues/11
