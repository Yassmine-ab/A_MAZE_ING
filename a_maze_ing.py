#!/usr/bin/env python3


import sys
from config_parsing import MazeConfig
from display import build_maze, user_interaction


def main() -> None:
    if len(sys.argv) != 2:
        print("[STDERR] Usage: python3 a_maze_ing.py config.txt")

    config_file_path = sys.argv[1]
    try:
        maze_config = MazeConfig.from_config(config_file_path)
        maze, pattern = build_maze(maze_config)
        entry = maze_config.entry
        exit_pos = maze_config.exit_pos
        start_cell = maze.grid[entry[1]][entry[0]]
        end_cell = maze.grid[exit_pos[1]][exit_pos[0]]
        directions = maze.find_shortest_path(start_cell, end_cell)
        path = maze.trace_path(start_cell, directions)
        maze.write_output(
            maze,
            entry,
            exit_pos,
            directions,
            maze_config.output_file,
        )
        user_interaction(maze, maze_config, entry, exit_pos, pattern, path)
        return 0
    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"[STDERR] {error}")


if __name__ == "__main__":
    main()
