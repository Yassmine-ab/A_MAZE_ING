# This script allows to write the file output_maze.txt
# A file that containt the maze using one hexadecimal digit per cell
# Cells are stored row by row, one row per line
# Then the coordinate of the entry and the exit
# Then the shortest valid path using the four letters N , E , S , W


from maze import Maze, Cell

def get_binary(cell: Cell) -> int:
    dico = cell.walls
    bi = int()
    if dico["West"]:
        



def write_output(maze: Maze, entry: tuple[int, int], exit_pos: tuple[int, int],
                 path: list[str], output_file: str) -> None:
    maze.grid







L'objet Maze généré par le module de ton mate (maze.py). Il contient :

maze.width, maze.height → pour savoir combien de lignes/colonnes écrire
maze.grid → une liste de listes de Cell (maze.grid[y][x]),
chaque Cell ayant un dict .walls = {"North": bool, "East": bool, "South": bool, "West": bool}
0 North
1 East
2 South
3 West

maze.grid = [
    # ligne y=0
    [
        Cell(position=(0,0), walls={"North":True,"East":True,"South":True,"West":True}),
        Cell(position=(1,0), walls={"North":True,"East":True,"South":True,"West":True}),
        Cell(position=(2,0), walls={"North":True,"East":True,"South":True,"West":True}),
    ],
    # ligne y=1
    [
        Cell(position=(0,1), walls={"North":True,"East":True,"South":True,"West":True}),
        Cell(position=(1,1), walls={"North":True,"East":True,"South":True,"West":True}),
        Cell(position=(2,1), walls={"North":True,"East":True,"South":True,"West":True}),
    ],
]
