#!/usr/bin/env python3


import random
from maze import Maze
from config_parsing import MazeConfig
from display import ascii_maze, user_interaction
from pattern42 import apply_42_pattern, pattern_list


def main() -> None:
    config_file_path = "config.txt"
    maze_config = MazeConfig.from_config(config_file_path)
    random.seed(maze_config.seed)
    m = Maze(maze_config.width, maze_config.height)
    entry = maze_config.entry
    exit_pos = maze_config.exit_pos
    result = apply_42_pattern(m, entry, exit_pos)
    if result:
        coord_pat = pattern_list(m)
    m.generate_maze(m.grid[0][0])
    if not maze_config.perfect:
        m.add_loops()
    user_interaction(m, entry, exit_pos)
    print(ascii_maze(m, entry, exit_pos, coord_pat))


if __name__ == "__main__":
    main()
