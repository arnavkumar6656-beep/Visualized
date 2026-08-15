"""
selection_sort.py
Selection Sort implemented as a generator.

How selection sort works:
- Split the array into a "sorted" part (left) and "unsorted" part (right).
- Repeatedly scan the unsorted part to find its SMALLEST value.
- Swap that smallest value into the front of the unsorted part.
- The sorted part grows by one element each pass.

Instead of returning the sorted array directly, this function `yield`s
an event every time it compares or swaps two elements, so the visualizer
can animate each step.
"""

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            # Show which two elements are currently being compared
            yield ("compare", min_idx, j)

            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            # Show the swap that places the smallest found value at position i
            yield ("swap", i, min_idx)
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # Position i is now guaranteed to be in its final sorted spot
        yield ("sorted", i)

    yield ("done",)
