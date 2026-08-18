from maze import Maze, Cell


def get_binary(cell: Cell) -> int:
    """Encode a cell's walls as an integer using bit flags.

    Parameters
    ----------
    cell : Cell
        The cell whose walls should be encoded.

    Returns
    -------
    int
        An integer between 0 and 15 representing the closed walls.
    """
    dico = cell.walls
    bit = int()
    if dico["West"]:
        bit = bit << 1 | 1
    else:
        bit = bit << 1

    if dico["South"]:
        bit = bit << 1 | 1
    else:
        bit = bit << 1

    if dico["East"]:
        bit = bit << 1 | 1
    else:
        bit = bit << 1

    if dico["North"]:
        bit = bit << 1 | 1
    else:
        bit = bit << 1

    return bit


def write_output(
    maze: Maze,
    entry: tuple[int, int],
    exit_pos: tuple[int, int],
    path: list[str],
    output_file: str,
) -> None:
    """Write the maze in hexadecimal, entry, exit,
        and shortest path to an output file.

    Parameters
    ----------
    maze : Maze
        The generated maze whose grid will be encoded.
    entry : tuple[int, int]
        The (x, y) coordinates of the maze entry.
    exit_pos : tuple[int, int]
        The (x, y) coordinates of the maze exit.
    path : list[str]
        The shortest path from entry to exit, as a list of full
        direction words (e.g. "North", "East").
    output_file : str
        The path of the file to write the maze data to.
    """
    hexa_lines = str()
    path_line = str()
    for lst in maze.grid:
        for cell in lst:
            hexa_lines += hex(get_binary(cell))[2:].upper()
        hexa_lines += "\n"
    hexa_lines += "\n"

    for coord in path:
        if coord == "North":
            path_line += "N"
        elif coord == "South":
            path_line += "S"
        elif coord == "East":
            path_line += "E"
        else:
            path_line += "W"
    path_line += "\n"

    try:
        with open(output_file, "w") as fd:
            fd.write(hexa_lines)
            fd.write(f"{entry[0]},{entry[1]}\n")
            fd.write(f"{exit_pos[0]},{exit_pos[1]}\n")
            fd.write(path_line)
    except OSError as msg:
        print(f"[STDERR] Error opening file '{output_file}': {msg}\n")
