from maze import Maze

def ascii_maze(
    maze: Maze,
    entry: tuple[int, int],
    exit_pos: tuple[int, int],
    pattern_list: list[tuple] = [],
    path: list[str] | None = None,
) -> str:
    maze_display = str()

    WALL_H = "\033[47m   \033[0m"
    WALL_V = "\033[47m \033[0m"
    ENTRY_H = "\033[45m   \033[0m"
    EXIT_H = "\033[41m   \033[0m"
    GRAY = "\033[100m   \033[0m"
    SPACE_H = "   "
    SPACE_V = " "

    for row in maze.grid:
        first_line = str()
        second_line = str()

        for case in row:
            first_line += WALL_V
            if case.walls["North"]:
                first_line += WALL_H
            else:
                first_line += SPACE_H

            if case.walls["West"]:
                second_line += WALL_V
            else:
                second_line += SPACE_V
            if case.position == entry:
                second_line += ENTRY_H
            elif case.position == exit_pos:
                second_line += EXIT_H
            else:
                if case.position in pattern_list:
                    second_line += GRAY
                else:
                    second_line += SPACE_H

        first_line += WALL_V
        if row[-1].walls["East"]:
            second_line += WALL_V
        else:
            second_line += SPACE_V

        maze_display += first_line + "\n" + second_line + "\n"

    last_line = str()
    for case in maze.grid[-1]:
        last_line += WALL_V
        if case.walls["South"]:
            last_line += WALL_H
        else:
            last_line += SPACE_H
    last_line += WALL_V

    maze_display += last_line
    return maze_display
