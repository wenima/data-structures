#Summary

The assignment was to implement a [Stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
in Python containing 2 methods:
* push(value) - Adds a value to the stack. The parameter is the value to be added to the stack
* pop() - Removes a value from the stack and returns that value. If the stack is empty, attempts to call pop should raise an appropriate Python exception class

For more information:

 https://codefellows.github.io/sea-python-401d5/assignments/stack.html


# Coverage:

* ---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                | Stmts | Miss | Cover | Missing |
| ------------------- | ----- | ---- | ----- | ------- |
| stack.py            |  11   |  0   | 100%  |         |
| test_stack.py       |  25   |  0   | 100%  |         |
| --------------      |  ---  |  --  | ----  | ------- |
| TOTAL               |  36   |  0   | 100%  |         |


# Github:

https://github.com/wenima/data-structures/tree/stack

Pull request: coming

# Comments about implementation:

* allthough the point of the assignment was to inherit, we started out with composition and decided to stick with it. It took a little getting used to figuring out that the container contains the linked list which contains our nodes but once the urge of wanting to inherit to model real world objects (which luckily the assignment didn't have) it makes more sense to use composition although it will take me quite a while to fully understand it, use it and appreciate it

* the original linked_list.py module contain two "helper" functions. ```python _iterate_from()``` takes in a list object from which to iterate (usually head) and returns an iterable which then can be used in different ways, one of them is ```_node_values``` which uses list comprehension to return a list containing all values/data of all the nodes.
