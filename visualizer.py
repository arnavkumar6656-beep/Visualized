import pygame
import sys

# ---------------- CONFIG ----------------
WIDTH, HEIGHT = 1200, 650
BG_COLOR = (25, 25, 25)
DEFAULT_COLOR = (100, 180, 255)   # sky blue - untouched
COMPARE_COLOR = (255, 220, 0)     # yellow - being compared
SWAP_COLOR = (255, 60, 60)        # red - being swapped
OVERWRITE_COLOR = (255, 140, 0)   # orange - value written (e.g. merge sort)
SORTED_COLOR = (60, 220, 100)     # green - finalized

FPS_DELAY_MS = 5   # lower = faster animation

# ---------------- DRAWING ----------------
def draw_bars(screen, array, color_map):
    """
    array: list of ints to visualize
    color_map: dict {index: (r,g,b)} for special colored bars,
               any index not in color_map uses DEFAULT_COLOR
    """
    screen.fill(BG_COLOR)

    n = len(array)
    max_val = max(array)
    bar_width = WIDTH / n
    usable_height = HEIGHT - 40  # leave margin at bottom

    for i, val in enumerate(array):
        bar_height = (val / max_val) * usable_height
        x = i * bar_width
        y = HEIGHT - bar_height

        color = color_map.get(i, DEFAULT_COLOR)
        pygame.draw.rect(screen, color, (x, y, bar_width - 1, bar_height))

    pygame.display.flip()


# ---------------- MAIN ANIMATION LOOP ----------------
def run_visualization(array, sort_generator, title="Sorting Visualizer"):
    """
    array: the list to sort (will be modified in place by the generator)
    sort_generator: a generator function that yields events like:
        ("compare", i, j)
        ("swap", i, j)
        ("overwrite", i)       -> arr[i] was written with a new value
                                   (used by algorithms like merge sort that
                                   copy values instead of swapping them)
        ("sorted", i)          -> mark index i as finalized/sorted
        ("done",)              -> sorting finished
    """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(title)
    clock = pygame.time.Clock()

    color_map = {}
    sorted_indices = set()
    gen = sort_generator(array)
    finished = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        if not finished:
            try:
                step = next(gen)
                color_map = {}  # reset transient highlight colors each step

                if step[0] == "compare":
                    _, i, j = step
                    color_map[i] = COMPARE_COLOR
                    color_map[j] = COMPARE_COLOR

                elif step[0] == "swap":
                    _, i, j = step
                    color_map[i] = SWAP_COLOR
                    color_map[j] = SWAP_COLOR

                elif step[0] == "overwrite":
                    _, i = step
                    color_map[i] = OVERWRITE_COLOR

                elif step[0] == "sorted":
                    _, i = step
                    sorted_indices.add(i)

                elif step[0] == "done":
                    sorted_indices.update(range(len(array)))
                    finished = True

            except StopIteration:
                sorted_indices.update(range(len(array)))
                finished = True

        # sorted indices always shown green, overriding transient colors
        display_colors = dict(color_map)
        for idx in sorted_indices:
            display_colors[idx] = SORTED_COLOR

        draw_bars(screen, array, display_colors)
        clock.tick(1000 // FPS_DELAY_MS if FPS_DELAY_MS else 60)
        pygame.time.delay(FPS_DELAY_MS)

    pygame.quit()
