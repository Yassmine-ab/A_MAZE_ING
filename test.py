"""Petit script de test pour visualiser ascii_maze() dans un vrai terminal.

Usage:
    python3 test_display.py
"""
# import random

# from maze import Maze
# from display import ascii_maze


# def main() -> None:
#     random.seed(4)
#     m = Maze(10, 6)
#     m.generate_maze(m.grid[0][0])
#     print(ascii_maze(m))


# if __name__ == "__main__":
#     main()


import random

from maze import Maze
from display import ascii_maze
from pattern42 import apply_42_pattern


def main() -> None:
    random.seed(1)

    m = Maze(15, 20)

    entry = (1, 1)
    exit_pos = (7, 5)

    result = apply_42_pattern(m, entry, exit_pos)
    m.generate_maze(m.grid[0][0])

    #print(f"42 pattern applied: {result}")
    print(ascii_maze(m, entry, exit_pos))


if __name__ == "__main__":
    main()
