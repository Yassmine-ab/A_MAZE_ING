from typing import Any
<<<<<<< HEAD
from maze import Maze, Cell
from writer import write_output
=======
from mazegen import MazeGenerator
>>>>>>> 75fc1956ebf68f914dad5c48b0959c7c0d50ebfa
from config_parsing import MazeConfig
from pattern42 import apply_42_pattern
from pattern42 import pattern_list


def ascii_maze(
    maze: MazeGenerator,
    entry: tuple[int, int],
    exit_pos: tuple[int, int],
    pattern: list[tuple[int, int]],
    path: list[tuple[int, int]],
<<<<<<< HEAD
    params: dict[str, Any] = {"WALL_H":"\033[47m   \033[0m",
                              "WALL_V":"\033[47m \033[0m",
                              "ENTRY_H":"\033[45m   \033[0m",
                              "EXIT_H":"\033[41m   \033[0m",
                              "FORTY_2":"\033[100m   \033[0m",
                              "PATH_H":"   ",
                              "PATH_V":" ",
                              "ROTATE":False},
=======
    params: dict[str, Any] = {
        "WALL_H": "\033[47m   \033[0m",
        "WALL_V": "\033[47m \033[0m",
        "ENTRY_H": "\033[45m   \033[0m",
        "EXIT_H": "\033[41m   \033[0m",
        "FORTY_2": "\033[100m   \033[0m",
        "PATH_H": "   ",
        "ROTATE": False,
    },
>>>>>>> 75fc1956ebf68f914dad5c48b0959c7c0d50ebfa
) -> str:
    wall_h = str(params["WALL_H"])
    wall_v = str(params["WALL_V"])
    entry_h = str(params["ENTRY_H"])
    exit_h = str(params["EXIT_H"])
    forty_two = str(params["FORTY_2"])
    path_h = str(params["PATH_H"])
    maze_display = str()
    SPACE_H = "   "
    SPACE_V = " "

    for row in maze.grid:
        first_line = str()
        second_line = str()

        for case in row:
            first_line += wall_v
            if case.walls["North"]:
                first_line += wall_h
            else:
                if case.position in path:
                    first_line += params["PATH_H"]
                else:
                    first_line += SPACE_H

            if case.walls["West"]:
                second_line += wall_v
            else:
                if case.position in path:
                    second_line += params["PATH_V"]
                else:
                    second_line += SPACE_V
            if case.position == entry:
                second_line += entry_h
            elif case.position == exit_pos:
                second_line += exit_h
            else:
                if case.position in pattern:
                    second_line += forty_two
                elif case.position in path:
                    second_line += path_h
                else:
                    second_line += SPACE_H

        first_line += wall_v
        if row[-1].walls["East"]:
            second_line += wall_v
        else:
            second_line += SPACE_V

        maze_display += first_line + "\n" + second_line + "\n"

    last_line = str()
    for case in maze.grid[-1]:
        last_line += wall_v
        if case.walls["South"]:
            last_line += wall_h
        else:
            last_line += SPACE_H
    last_line += wall_v

    maze_display += last_line
    return maze_display


def build_maze(
    maze_config: MazeConfig,
) -> tuple[MazeGenerator, list[tuple[int, int]]]:
    """Build a maze and return it with the optional 42 pattern coordinates."""
    maze = MazeGenerator(
        maze_config.width,
        maze_config.height,
        seed=maze_config.seed,
        entry=maze_config.entry,
        exit_pos=maze_config.exit_pos,
        perfect=maze_config.perfect,
    )
    result = apply_42_pattern(maze, maze_config.entry, maze_config.exit_pos)
    pattern: list[tuple[int, int]] = []
    if result:
        pattern = pattern_list(maze)
    maze.generate(set(pattern) if result else None)
    return maze, pattern


def user_interaction(
    maze: MazeGenerator,
    maze_config: MazeConfig,
    entry: tuple[int, int],
    exit_pos: tuple[int, int],
    pattern: list[tuple[int, int]],
    path: list[tuple[int, int]],
<<<<<<< HEAD
    params: dict[str, Any] = {"WALL_H":"\033[47m   \033[0m",
                              "WALL_V":"\033[47m \033[0m",
                              "ENTRY_H":"\033[45m   \033[0m",
                              "EXIT_H":"\033[41m   \033[0m",
                              "FORTY_2":"\033[100m   \033[0m",
                              "PATH_H":"   ",
                              "PATH_V":" ",
                              "ROTATE":False},
)-> None:
=======
    params: dict[str, Any] = {
        "WALL_H": "\033[47m   \033[0m",
        "WALL_V": "\033[47m \033[0m",
        "ENTRY_H": "\033[45m   \033[0m",
        "EXIT_H": "\033[41m   \033[0m",
        "FORTY_2": "\033[100m   \033[0m",
        "PATH_H": "   ",
        "ROTATE": False,
    },
) -> None:
    new_pattern = pattern
>>>>>>> 75fc1956ebf68f914dad5c48b0959c7c0d50ebfa
    print(ascii_maze(maze, entry, exit_pos, pattern, path))
    start = maze.grid[entry[1]][entry[0]]
    end = maze.grid[exit_pos[1]][exit_pos[0]]
    path_list = maze.find_shortest_path(start, end)
    write_output(maze, entry, exit_pos, path_list, "output_maze.txt")
    while True:
        print("\n=== A-Maze-ing ====")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")
        try:
            user = int(input("Choice? (1-4):  "))
            if user < 1 or user > 4:
                raise ValueError()
        except ValueError:
            print("\n[ERROR] You must enter an int between 1 and 4")
            continue

        if user == 1:
            maze, new_pattern = build_maze(maze_config)
            print()
            print(ascii_maze(maze, entry, exit_pos, new_pattern, path))
            start = maze.grid[entry[1]][entry[0]]
            end = maze.grid[exit_pos[1]][exit_pos[0]]
            path_list = maze.find_shortest_path(start, end)
            write_output(maze, entry, exit_pos, path_list, "output_maze.txt")
            continue

        elif user == 2:
            result = apply_42_pattern(maze, entry, exit_pos)
            maze.generate_maze(maze.grid[0][0])
            new_pattern = []
            if result:
                new_pattern = pattern_list(maze)
            if params["PATH_H"] == "   ":
                if params["ROTATE"]:
                    params["PATH_H"] = "\033[41m   \033[0m"
                    params["PATH_V"] = "\033[41m \033[0m"
                else:
                    params["PATH_H"] = "\033[44m   \033[0m"
                    params["PATH_V"] = "\033[44m \033[0m"
            else:
                params["PATH_H"] = "   "
                params["PATH_V"] = " "
            print(ascii_maze(maze, entry, exit_pos, new_pattern, path, params))
            continue

        elif user == 3:
            if params["ROTATE"] is False:
<<<<<<< HEAD
                params["WALL_H"] = "\033[44m   \033[0m"
                params["WALL_V"] = "\033[44m \033[0m"
                params["ENTRY_H"] = "\033[47m   \033[0m"
                params["EXIT_H"] = "\033[42m   \033[0m"
                params["FORTY_2"] = "\033[43m   \033[0m"
                params["ROTATE"] = True
                if params["PATH_H"] != "   ":
                    params["PATH_H"] = "\033[41m   \033[0m"
                    params["PATH_V"] = "\033[41m \033[0m"

            else:
                params["WALL_H"] = "\033[47m   \033[0m"
                params["WALL_V"] = "\033[47m \033[0m"
                params["ENTRY_H"] = "\033[45m   \033[0m"
                params["EXIT_H"] = "\033[41m   \033[0m"
                params["FORTY_2"] = "\033[100m   \033[0m"
                params["ROTATE"] = False
                if params["PATH_H"] != "   ":
                    params["PATH_H"] = "\033[44m   \033[0m"
                    params["PATH_V"] = "\033[44m \033[0m"
            print(ascii_maze(maze, entry, exit_pos, pattern, path, params))
=======
                params = {
                    "WALL_H": "\033[44m   \033[0m",
                    "WALL_V": "\033[44m \033[0m",
                    "ENTRY_H": "\033[47m   \033[0m",
                    "EXIT_H": "\033[42m   \033[0m",
                    "FORTY_2": "\033[43m   \033[0m",
                    "PATH_H": "   ",
                    "ROTATE": True,
                }
            else:
                params = {
                    "WALL_H": "\033[47m   \033[0m",
                    "WALL_V": "\033[47m \033[0m",
                    "ENTRY_H": "\033[45m   \033[0m",
                    "EXIT_H": "\033[41m   \033[0m",
                    "FORTY_2": "\033[100m   \033[0m",
                    "PATH_H": "\033[44m   \033[0m",
                    "ROTATE": False,
                }
            print(ascii_maze(maze, entry, exit_pos, new_pattern, path, params))
>>>>>>> 75fc1956ebf68f914dad5c48b0959c7c0d50ebfa
            continue

        else:
            return
