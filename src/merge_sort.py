"""Module for implementation of merge_sort."""

def merge_sort(arr):
    """Return a sorted list using merge_sort algorithm."""
    if len(arr) < 2 :
        return arr
    return merge(merge_sort(arr[:len(arr) // 2]), merge_sort(arr[len(arr) // 2:]))

def merge(l, r):
    """Return an accumulated list after elements have been swapped."""
    result = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result += l[i:]
    result += r[j:]
    return result
