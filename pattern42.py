from maze import Maze, Cell


def apply_42_pattern(
    maze: Maze,
    entry: tuple[int, int],
    exit: tuple[int, int],
) -> bool:
    if maze.width < 7 or maze.height < 5:
        print("[STDERR] The maze size does not allow the '42' pattern")
        return False
    y_start = (maze.height - 5) // 2
    x_start = (maze.width - 7) // 2
    QUARANTE_DEUX_SHAPE = [
        (0, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (0, 1),
        (6, 1),
        (0, 2),
        (1, 2),
        (2, 2),
        (4, 2),
        (5, 2),
        (6, 2),
        (2, 3),
        (4, 3),
        (2, 4),
        (4, 4),
        (5, 4),
        (6, 4),
    ]
    QUARANTE_DEUX_SHAPE = [(x + x_start, y + y_start) for x, y in QUARANTE_DEUX_SHAPE]
    if entry in QUARANTE_DEUX_SHAPE or exit in QUARANTE_DEUX_SHAPE:
        print("[STDERR] The entry/exit can not be in the '42' pattern")
        return False
