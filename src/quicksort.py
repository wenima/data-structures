"""Implementation of quicksort.
Source: http://hetland.org/coding/python/quicksort.html"""


def partition(arr, start, end):
    pivot = arr[end]                           # Partition around the last value
    bottom = start-1                           # Start outside the area to be partitioned
    top = end                                  # Ditto

    done = 0
    while not done:                            # Until all elements are partitioned...

        while not done:                        # Until we find an out of place element...
            bottom = bottom+1                  # ... move the bottom up.

            if bottom == top:                  # If we hit the top...
                done = 1                       # ... we are done.
                break

            if arr[bottom] > pivot:            # Is the bottom out of place?
                arr[top] = arr[bottom]         # Then put it at the top...
                break                          # ... and start searching from the top.

        while not done:                        # Until we find an out of place element...
            top = top-1                        # ... move the top down.

            if top == bottom:                  # If we hit the bottom...
                done = 1                       # ... we are done.
                break

            if arr[top] < pivot:              # Is the top out of place?
                arr[bottom] = arr[top]        # Then put it at the bottom...
                break                         # ...and start searching from the bottom.

    arr[top] = pivot                          # Put the pivot in its place.
    return top

def quicksort(arr, start, end):
    """Return a sorted list by partioning around the pivot, swap all elements
    which are smaller than pivot to the left and larger than pivot to the right.
    Then sort these lists by recursively repeating the step."""
    if start < end:                           # If there are two or more elements...
        split = partition(arr, start, end)    # ... partition the sublist...
        quicksort(arr, start, split-1)        # ... and sort both halves.
        quicksort(arr, split+1, end)
    else:
        return arr
    return arr
