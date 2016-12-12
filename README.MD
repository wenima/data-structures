#Summary

the repository *code-katas* includes the following completed coding challenges from the [CodeWars Python challenges] (http://wwww.codewars.com)

# Python coding challenges:

## Mandatory coding challenges at various levls to sum up to 16 where kyu8 counts for 1pt, kyu7 for 2pts and kyu6 for 3pts.

* kata_string_to_array
* Taking a Vacaction --> Vacation.py
* A Day at the Supermarket --> DayAtSupermarket.py
* Student Becomes The Teacher --> StudentBecomesTeacher.py
* Battleship! --> Battleship.py

## Details for each kata completed
Descripton of Kata: Write a function to split a string and convert it into an array of words.
Difficulty: kyu8
Module: kata_string_to_array
Tests: test_katas_8thkyu8.py
Link: https://www.codewars.com/kata/convert-a-string-to-an-array/train/python
Most interesting solution/best practice:
```python
def string_to_array(string):
    return string.split(" ")
```

Description: Given a string of digits, function will replace each char with 0 if char < 5 or 1 if char >=5
Difficulty: kyu8
Module: kata_fake_bin.py
Tests: test_kata_fake_bin.py
Link: https://www.codewars.com/kata/fake-binary/train/python
Most interesting solution/best practice:
```python
#using generator expression
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
```

Description: Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
Difficulty: kyu8
Module: kata_even_or_odd.py
Tests: test_kata_even_or_odd.py
Link: https://www.codewars.com/kata/even-or-odd/python
Most interesting solution/best practice:
```python
#interesting solution, have to admit I don't understand why this works
def even_or_odd(number):
  return ["Even", "Odd"][number % 2]
  ```

Description: Create a function that consumes an integer and returns an array of ints in reversed order
Difficulty: kyu8
Module: kata_digitize.py
Tests: test_kata_digitize.py
Link: https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/python
Most interesting solution/best practice:
```python
#super smooth, I like it!
def digitize(n):
    return [int(x) for x in reversed(str(n))]
```

Description: Create a function that is given a list which may or may not contain another list. Flatten all lists where they exist and return a flattend list
Difficulty: kyu7
Module: kata_flatten_me.py
Tests: test_kata_flatten_me.py
Link: https://www.codewars.com/kata/flatten-me/python
Most interesting solution/best practice:
```python
#didn't know about extend, seems like a good solution
def flatten_me(lst):
    res = []
    for l in lst:
        if isinstance(l, list):
            res.extend(l)
        else:
            res.append(l)
    return res
```

Description: Create a function that returns True if the given integer is a power of 2, False if it's not
Difficulty: kyu7
Module: kata_power_of_two.py
Tests: test_kata_power_of_two.py
Link: https://www.codewars.com/kata/power-of-two/python
Most interesting solution/best practice:
I think my solution is pretty good, other solutions had issues like returning True for 0 or readability with bitwise operation so I like:
```python
def power_of_two(n):
    """Take an integer n and return True if n is a power of 2, False if not"""
    return True if str(bin(n)).count('1') == 1 else False
```

Description: Create a function which returns multiples of 2 given numbers bound to an upper range
Difficulty: kyu7
Module: kata_multiples.py
Tests: test_kata_multiples.py
Link: https://www.codewars.com/kata/show-multiples-of-2-numbers-within-a-range/python
Most interesting solution/best practice:
very clever solution I could not come up with. My solution definitely feels very clunky
```python
def multiples(s1, s2, s3):
    return [a for a in xrange(1, s3) if not(a % s1 or a % s2)]
```

Description: Create a function which returns True if both lists have one common element
Difficulty: kyu7
Module: kata_duplicate_elements.py
Tests: test_kata_duplicate_elements.py
Link: https://www.codewars.com/kata/identical-elements
Most interesting solution/best practice:
very clear & readable
```python
def duplicate_elements(m, n):
    return any(x in n for x in m)
```






## Optional at level lower than kyu8

* AreaCalculator.py
* rockpaperscissors.py

# Motivation

* the completed coding challenges were part of the Codefellows 401 Python Course snow-day assignment

# General comments
