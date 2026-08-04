# Sorting Algorithm Visualizer

A Python + Pygame application that visually animates how different sorting algorithms work. The array is rendered as a bar graph, and every comparison and swap the algorithm makes is animated in real time, so you can *see* the logic instead of just reading code.

---

## Features

- Hardcoded starting array (ascending order)
- Option to randomize the array before sorting
- Animated bar-graph visualization of the sorting process
- Color-coded bars to show what the algorithm is doing at each step:
  - **White / default** — untouched
  - **Yellow** — currently being compared
  - **Red** — currently being swapped
  - **Green** — in its final sorted position
- Individual, standalone implementations for each algorithm

---

## Algorithms Included

| Algorithm      | File                  | Time Complexity (avg) |
|----------------|------------------------|-------------------------|
| Bubble Sort    | `bubble_sort.py`      | O(n²) |
| Selection Sort | `selection_sort.py`   | O(n²) |
| Insertion Sort | `insertion_sort.py`   | O(n²) |
| Merge Sort     | `merge_sort.py`       | O(n log n) |
| Quick Sort     | `quick_sort.py`       | O(n log n) |

---

## Tech Stack

- **Language:** Python 3
- **Library:** [Pygame](https://www.pygame.org/) — for the window, drawing bars, and the animation loop

---

## Project Structure

```
sorting-visualizer/
│
├── main.py                # Entry point — menu, array setup, launches visualizer
├── visualizer.py           # Shared drawing/animation engine (draws bars, handles colors & delay)
├── bubble_sort.py          # Bubble sort logic + step generation
├── selection_sort.py       # Selection sort logic + step generation
├── insertion_sort.py       # Insertion sort logic + step generation
├── merge_sort.py           # Merge sort logic + step generation
├── quick_sort.py           # Quick sort logic + step generation
└── README.md
```

Each algorithm file contains the sorting logic written as a **generator** (using `yield`) that pauses after every comparison or swap and reports what just happened. `visualizer.py` consumes these steps one at a time and redraws the bars accordingly — this keeps the sorting logic completely separate from the animation/drawing code.

---

## How It Works

1. The array starts hardcoded in ascending order.
2. A menu lets you choose to:
   - Keep the array as is, or
   - Randomize it (Fisher–Yates shuffle)
3. You select which algorithm to run.
4. The chosen algorithm runs as a generator, yielding an event after every comparison or swap, e.g.:
   ```python
   yield ("compare", i, j)
   yield ("swap", i, j)
   ```
5. The visualizer reads these events one at a time, updates bar heights/colors, and redraws the screen with a short delay between steps — creating the animation.

---

## Installation

1. Make sure Python 3 is installed.
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Clone or download this project folder.

---

## Usage

Run the main file:
```bash
python main.py
```

Follow the on-screen menu to:
1. Keep the array sorted or randomize it
2. Select a sorting algorithm
3. Watch the bars animate as the array gets sorted

---

## Controls (planned)

| Key         | Action                     |
|-------------|-----------------------------|
| `R`         | Randomize the array         |
| `1`–`5`     | Select an algorithm to run  |
| `SPACE`     | Start / Pause the animation |
| `+` / `-`   | Increase / decrease speed   |
| `ESC`       | Return to menu              |

---

## Future Improvements

- Side-by-side race mode (compare two algorithms at once)
- Adjustable array size
- Step counter / comparison & swap counter displayed on screen
- Sound effects tied to comparisons/swaps
- Custom array input from the user

---

## License

This project is open for educational use and modification.
