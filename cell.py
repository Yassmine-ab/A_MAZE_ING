#!/usr/bin/env python3


from typing import Optional
from random import shuffle


class Cell:
    def __init__(self, position: tuple[int, int], walls: Optional[dict[str, bool]] = None, visited: bool = False):
        self.position = position
        if walls is not None:
            self.walls = walls
        else:
            self.walls = {"North": True, "East": True, "South": True, "West": True}
        self.visited = visited


class Maze:
    def __init__(self, width: int, height: int, grid: Optional[list[list[Cell]]] = None):
        self.width = width
        self.height = height
        if grid is not None:
            self.grid = grid
        else:
            self.grid = []
            for y in range(height):
                row: list[Cell] = []
                for x in range(width):
                    row.append(Cell((x, y)))
                self.grid.append(row)

    def break_wall(self, cell: Cell, direction: str) -> None:
            if direction not in cell.walls:
                raise ValueError(f"Invalid direction: {direction}. Valid directions are 'North', 'East', 'South', 'West'.")
            (x, y) = cell.position
            if direction == "North":
                if y - 1 < 0:
                    return
                neighbor_cell = self.grid[y - 1][x]
                neighbor_cell.walls["South"] = False
                cell.walls[direction] = False
            elif direction == "East":
                if x + 1 >= self.width:
                    return
                neighbor_cell = self.grid[y][x + 1]
                neighbor_cell.walls["West"] = False
                cell.walls[direction] = False
            elif direction == "South":
                if y + 1 >= self.height:
                    return
                neighbor_cell = self.grid[y + 1][x]
                neighbor_cell.walls["North"] = False
                cell.walls[direction] = False
            elif direction == "West":
                if x - 1 < 0:
                    return
                neighbor_cell = self.grid[y][x - 1]
                neighbor_cell.walls["East"] = False
                cell.walls[direction] = False

    def get_neighbors(self, cell: Cell) -> dict[str, Cell]:
        (x, y) = cell.position
        neighbors: dict[str, Cell] = {}
        if y - 1 >= 0:
            neighbors["North"] = self.grid[y - 1][x]
        if x + 1 < self.width:
            neighbors["East"] = self.grid[y][x + 1]
        if y + 1 < self.height:
            neighbors["South"] = self.grid[y + 1][x]
        if x - 1 >= 0:
            neighbors["West"] = self.grid[y][x - 1]
        return neighbors

    def generate_maze(self, current_cell: Cell) -> None:
        current_cell.visited = True
        neighbors_list = list(self.get_neighbors(current_cell).items())
        shuffle(neighbors_list)
        for direction, neighbor in neighbors_list:
            if not neighbor.visited:
                self.break_wall(current_cell, direction)
                self.generate_maze(neighbor)


def main() -> None:
    m = Maze(5, 5)
    m.generate_maze(m.grid[0][0])


if __name__ == "__main__":
    main()