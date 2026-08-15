"""
main.py
Entry point for the Sorting Visualizer.

- Builds a hardcoded array of 100 elements, ascending, each value strictly
  bigger than the last (so every bar is visibly a different height).
- Lets the user keep it sorted or randomize it.
- Runs Selection Sort with animation.
"""

import random
from .visualizer import run_visualization
from Selection_Sort.selection_sort import selection_sort
from .merge_sort import merge_sort


def build_array():
    # 100 values, each bigger than the last: 5, 10, 15, ... 500
    return [i * 5 for i in range(1, 101)]


def randomize(arr):
    shuffled = arr[:]
    random.shuffle(shuffled)
    return shuffled


ALGORITHMS = {
    "1": ("Selection Sort", selection_sort),
    "2": ("Merge Sort", merge_sort),
}


def main():
    array = build_array()

    print("Sorting Visualizer")
    print("Choose an algorithm:")
    for key, (name, _) in ALGORITHMS.items():
        print(f"{key}. {name}")
    algo_choice = input(f"Algorithm ({'/'.join(ALGORITHMS.keys())}): ").strip()
    algo_name, algo_func = ALGORITHMS.get(algo_choice, ALGORITHMS["1"])

    print("\n1. Keep array in ascending order")
    print("2. Randomize the array")
    order_choice = input("Choose an option (1/2): ").strip()

    if order_choice == "2":
        array = randomize(array)

    run_visualization(array, algo_func, title=f"{algo_name} Visualizer")


if __name__ == "__main__":
    main()
