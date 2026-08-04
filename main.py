"""
main.py
Entry point for the Sorting Visualizer.

- Builds a hardcoded array of 100 elements, ascending, each value strictly
  bigger than the last (so every bar is visibly a different height).
- Lets the user keep it sorted or randomize it.
- Runs Selection Sort with animation.
"""

import random
from visualizer import run_visualization
from selection_sort import selection_sort


def build_array():
    # 100 values, each bigger than the last: 5, 10, 15, ... 500
    return [i * 5 for i in range(1, 101)]


def randomize(arr):
    shuffled = arr[:]
    random.shuffle(shuffled)
    return shuffled


def main():
    array = build_array()

    print("Sorting Visualizer — Selection Sort")
    print("1. Keep array in ascending order")
    print("2. Randomize the array")
    choice = input("Choose an option (1/2): ").strip()

    if choice == "2":
        array = randomize(array)

    run_visualization(array, selection_sort, title="Selection Sort Visualizer")


if __name__ == "__main__":
    main()
