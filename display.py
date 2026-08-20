from typing import Any
from mazegen import MazeGenerator
from config_parsing import MazeConfig
from pattern42 import apply_42_pattern
from pattern42 import pattern_list


def ascii_maze(
    maze: MazeGenerator,
    entry: tuple[int, int],
    exit_pos: tuple[int, int],
    pattern: list[tuple[int, int]],
    path: list[tuple[int, int]],
    params: dict[str, Any] = {
        "WALL_H": "\033[47m   \033[0m",
        "WALL_V": "\033[47m \033[0m",
        "ENTRY_H": "\033[45m   \033[0m",
        "EXIT_H": "\033[41m   \033[0m",
        "FORTY_2": "\033[100m   \033[0m",
        "PATH_H": "   ",
        "ROTATE": False,
    },
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
                first_line += SPACE_H

            if case.walls["West"]:
                second_line += wall_v
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
    print(ascii_maze(maze, entry, exit_pos, pattern, path))
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
            continue

        elif user == 2:
            if params["PATH_H"] == "   ":
                params["PATH_H"] = "\033[44m   \033[0m"
            else:
                params["PATH_H"] = "   "
            print(ascii_maze(maze, entry, exit_pos, new_pattern, path))
            continue

        elif user == 3:
            if params["ROTATE"] is False:
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
            continue

        else:
            return
