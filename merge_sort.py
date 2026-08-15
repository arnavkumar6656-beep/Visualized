"""
merge_sort.py
Merge Sort implemented as a generator.

How merge sort works:
- Recursively split the array in half until each piece has 1 element
  (a single element is trivially "sorted").
- Merge each pair of sorted halves back together, always taking the
  smaller of the two "front" elements first.
- Because both halves are already sorted, the merge itself only needs
  one pass through each.

Note on events: unlike selection sort, merge sort doesn't swap two known
elements in place — it copies values from a left/right half into the next
open slot one at a time. So alongside ("compare", i, j) this yields
("overwrite", i) right after arr[i] has been written with its next merged
value, instead of ("swap", i, j). visualizer.py has been given a small,
additive update to color this the same way it colors a swap.
"""

def merge_sort(arr):
    n = len(arr)

    def sort(lo, hi):
        # Sorts arr[lo:hi] in place, recursively.
        if hi - lo <= 1:
            return

        mid = (lo + hi) // 2
        yield from sort(lo, mid)
        yield from sort(mid, hi)
        yield from merge(lo, mid, hi)

    def merge(lo, mid, hi):
        # arr[lo:mid] and arr[mid:hi] are each already sorted.
        # Merge them back into arr[lo:hi], smallest-first.
        left = arr[lo:mid]
        right = arr[mid:hi]

        i, j, k = 0, 0, lo  # i -> left, j -> right, k -> write position

        while i < len(left) and j < len(right):
            # Show which two "front" elements are currently being compared
            yield ("compare", lo + i, mid + j)

            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            yield ("overwrite", k)
            k += 1

        # Drain whichever half still has leftovers (the other is exhausted,
        # so there's nothing left to compare against).
        while i < len(left):
            arr[k] = left[i]
            yield ("overwrite", k)
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            yield ("overwrite", k)
            j += 1
            k += 1

        # arr[lo:hi] is now fully merged and sorted.
        for idx in range(lo, hi):
            yield ("sorted", idx)

    yield from sort(0, n)
    yield ("done",)
