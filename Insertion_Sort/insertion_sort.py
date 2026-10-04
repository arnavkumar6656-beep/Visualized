"""
Insertion Sort implemented as a generator.

Insertion Sort builds the sorted portion of the array one element
at a time. Each new element is compared with the elements before it
and larger elements are shifted one position to the right.

Events:
    ("compare", i, j)
        Two positions are currently being compared.

    ("overwrite", i)
        A value has been written to position i.

    ("sorted", i)
        Position i is currently part of the sorted portion.

    ("done",)
        Sorting is complete.
"""


def insertion_sort(arr):
    n = len(arr)

    # The first element is already considered sorted.
    if n > 0:
        yield ("sorted", 0)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Compare the key with elements in the sorted portion.
        while j >= 0:
            yield ("compare", j, i)

            if arr[j] <= key:
                break

            # Shift the larger element one position to the right.
            arr[j + 1] = arr[j]
            yield ("overwrite", j + 1)

            j -= 1

        # Place the key into its correct position.
        arr[j + 1] = key
        yield ("overwrite", j + 1)

        # The current prefix is now sorted.
        for idx in range(i + 1):
            yield ("sorted", idx)

    yield ("done",)