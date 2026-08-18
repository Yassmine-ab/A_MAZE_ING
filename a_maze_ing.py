#!/usr/bin/env python3


import random
from maze import Maze, Cell
from config_parsing import MazeConfig
from display import user_interaction
from pattern42 import apply_42_pattern, pattern_list


def trace_path(start: Cell, directions: list[str]) -> list[tuple[int, int]]:
    if directions == []:
        return []
    x, y = start.position
    cells: list[tuple[int, int]] = [(x, y)]
    for direction in directions:
        if direction == "North":
            y -= 1
        elif direction == "East":
            x += 1
        elif direction == "South":
            y += 1
        elif direction == "West":
            x -= 1
        cells.append((x, y))
    return cells


def main() -> None:
    config_file_path = "config.txt"
    maze_config = MazeConfig.from_config(config_file_path)
    random.seed(maze_config.seed)
    maze = Maze(maze_config.width, maze_config.height)
    entry = maze_config.entry
    exit_pos = maze_config.exit_pos
    result = apply_42_pattern(maze, entry, exit_pos)
    pattern = []
    if result:
        pattern = pattern_list(maze)
    maze.generate_maze(maze.grid[0][0])
    if not maze_config.perfect:
        maze.add_loops()
    path = trace_path(Cell(entry), maze.find_shortest_path(Cell(entry), Cell(exit_pos)))
    user_interaction(maze, entry, exit_pos, pattern, path)


if __name__ == "__main__":
    main()
