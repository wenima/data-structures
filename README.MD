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


# Thoughts on when to use a singly linked list vs a doubly_linked_list:
it seems that for a really long list, it would be much better to have access to the tail as it would make search algorithms faster as you can climb up and go down. For a Stack data structure it seems that a singly linked list is better as we are happy to just have the option to delete at the head. If we build more complex data structures, it would probably also make sense to use singly linked lists as they woul be more flexible to build more advanced structures?
For doubly_linked_list it seems sine we have the pointer to a deleted node, we could also re-insert as we still know the pre and next. 

# Comments about implementation:

* the keeping state of size of the object is not optimal and it would be better to call it in it own function
* one test has been commented out due to difference of opinion https://github.com/wenima/data-structures/issues/11
