"""Petit script de test pour visualiser ascii_maze() dans un vrai terminal.

Usage:
    python3 test_display.py
"""
import random

from maze import Maze
from display import ascii_maze
from pattern42 import apply_42_pattern
from pattern42 import pattern_list


def main() -> None:
    random.seed(5)

    m = Maze(20, 15)

    entry = (0, 0)
    exit_pos = (19, 14)

    #result = apply_42_pattern(m, entry, exit_pos)
    m.generate_maze(m.grid[0][0])

    # if result:
    #     coord_pat = pattern_list(m)

    print(ascii_maze(m, entry, exit_pos))


if __name__ == "__main__":
    main()
