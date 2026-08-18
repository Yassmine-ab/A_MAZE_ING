import random
from maze import Cell, Maze
from pattern42 import apply_42_pattern
from pattern42 import pattern_list


def ascii_maze(
    maze: Maze,
    entry: tuple[int, int],
    exit_pos: tuple[int, int],
    pattern_list: list[tuple[int, int]] = [],
    params: dict[str, str] = {"WALL_H":"\033[47m   \033[0m",
                              "WALL_V":"\033[47m \033[0m",
                              "ENTRY_H":"\033[45m   \033[0m",
                              "EXIT_H":"\033[41m   \033[0m",
                              "FORTY_2":"\033[100m   \033[0m"},
    path: list[tuple[int, int]] = []
) -> str:
    maze_display = str()
    SPACE_H = "   "
    SPACE_V = " "

    for row in maze.grid:
        first_line = str()
        second_line = str()

        for case in row:
            first_line += params["WALL_V"]
            if case.walls["North"]:
                first_line += params["WALL_H"]
            else:
                first_line += SPACE_H

            if case.walls["West"]:
                second_line += params["WALL_V"]
            else:
                second_line += SPACE_V
            if case.position == entry:
                second_line += params["ENTRY_H"]
            elif case.position == exit_pos:
                second_line += params["EXIT_H"]
            else:
                if case.position in pattern_list:
                    second_line += params["FORTY_2"]
                else:
                    second_line += SPACE_H

        first_line += params["WALL_V"]
        if row[-1].walls["East"]:
            second_line += params["WALL_V"]
        else:
            second_line += SPACE_V

        maze_display += first_line + "\n" + second_line + "\n"

    last_line = str()
    for case in maze.grid[-1]:
        last_line += params["WALL_V"]
        if case.walls["South"]:
            last_line += params["WALL_H"]
        else:
            last_line += SPACE_H
    last_line += params["WALL_V"]

    maze_display += last_line
    return maze_display

def trace_path(start: Cell, directions: list[str]) -> list[tuple[int, int]]:
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


def user_interaction(
    maze: Maze,
    entry: tuple[int, int],
    exit_pos: tuple[int, int],
    pattern: list[tuple[int, int]] = [],
    params: dict[str, str] = {"WALL_H":"\033[47m   \033[0m",
                              "WALL_V":"\033[47m \033[0m",
                              "ENTRY_H":"\033[45m   \033[0m",
                              "EXIT_H":"\033[41m   \033[0m",
                              "FORTY_2":"\033[100m   \033[0m"},
    path: list[tuple[int, int]] = []
)-> None:
    print(ascii_maze(maze, entry, exit_pos, params))
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
            random.seed(4)
            maze = Maze(20, 15)
            entry = (0, 0)
            exit_pos = (19, 14)
            result = apply_42_pattern(maze, entry, exit_pos)
            maze.generate_maze(maze.grid[0][0])
            if result:
                coord_pat = pattern_list(maze)
            print(ascii_maze(maze, entry, exit_pos, coord_pat))
            continue

        elif user == 2:
            pass # a faire

        elif user == 3:
            params = {"WALL_H":"\033[44m   \033[0m",
                      "WALL_V":"\033[44m \033[0m",
                      "ENTRY_H":"\033[47m   \033[0m",
                      "EXIT_H":"\033[42m   \033[0m",
                      "FORTY_2":"\033[43m   \033[0m"}
            coord_pat = pattern_list(maze)
            print(ascii_maze(maze, entry, exit_pos, coord_pat, params))
            continue
        else:
            return
