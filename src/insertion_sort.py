"""Implementation of insertion_sort"""


def insertion_sort(arr):
    """Return a sorted list by walking through each element and shifting larger
    values to the right."""
    for idx, n in enumerate(arr):
        while idx > 0 and arr[idx - 1] > n:
            arr[idx] = arr[idx - 1]
            idx = idx - 1
        arr[idx] = n
    return arr
