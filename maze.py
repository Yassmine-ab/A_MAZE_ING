#!/usr/bin/env python3


from typing import Optional
from random import shuffle
from collections import deque


class Cell:
    def __init__(
        self,
        position: tuple[int, int],
        walls: Optional[dict[str, bool]] = None,
        visited: bool = False,
    ):
        self.position = position
        if walls is not None:
            self.walls = walls
        else:
            self.walls = {
                "North": True,
                "East": True,
                "South": True,
                "West": True}
        self.visited = visited


class Maze:
    def __init__(
        self, width: int, height: int, grid: Optional[list[list[Cell]]] = None
    ):
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
            raise ValueError(
                f"Invalid direction: {direction}. "
                "Valid directions are 'North', 'East', 'South', 'West'."
            )
        x, y = cell.position
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

    def restore_wall(self, cell: Cell, direction: str) -> None:
        if direction not in cell.walls:
            raise ValueError(
                f"Invalid direction: {direction}. "
                "Valid directions are 'North', 'East', 'South', 'West'."
            )
        x, y = cell.position
        if direction == "North":
            if y - 1 < 0:
                return
            neighbor_cell = self.grid[y - 1][x]
            neighbor_cell.walls["South"] = True
            cell.walls[direction] = True
        elif direction == "East":
            if x + 1 >= self.width:
                return
            neighbor_cell = self.grid[y][x + 1]
            neighbor_cell.walls["West"] = True
            cell.walls[direction] = True
        elif direction == "South":
            if y + 1 >= self.height:
                return
            neighbor_cell = self.grid[y + 1][x]
            neighbor_cell.walls["North"] = True
            cell.walls[direction] = True
        elif direction == "West":
            if x - 1 < 0:
                return
            neighbor_cell = self.grid[y][x - 1]
            neighbor_cell.walls["East"] = True
            cell.walls[direction] = True

    def get_neighbors(self, cell: Cell) -> dict[str, Cell]:
        x, y = cell.position
        neighbors = {}
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

    def get_open_neighbors(self, cell: Cell) -> dict[str, Cell]:
        neighbors = self.get_neighbors(cell)
        open_neighbors = {}
        for direction, neighbor in neighbors.items():
            if not cell.walls[direction]:
                open_neighbors[direction] = neighbor
        return open_neighbors

    def find_shortest_path(self, start: Cell, end: Cell) -> list[str]:
        queue: deque[tuple[Cell, list[str]]] = deque([(start, [])])
        visited = set()
        visited.add(start.position)
        while queue:
            current_cell, path = queue.popleft()
            if current_cell == end:
                return path
            for direction, neighbor in (
                self.get_open_neighbors(current_cell).items()
            ):
                if neighbor.position not in visited:
                    visited.add(neighbor.position)
                    queue.append((neighbor, path + [direction]))
        return []

    def is_open_area_3x3(self, x: int, y: int) -> bool:
        for dy in range(3):
            for dx in range(2):
                neighbor_cell = self.grid[y + dy][x + dx]
                if neighbor_cell.walls["East"]:
                    return False
        for dx in range(3):
            for dy in range(2):
                neighbor_cell = self.grid[y + dy][x + dx]
                if neighbor_cell.walls["South"]:
                    return False
        return True

    def get_affected_areas_3x3(
        self, x: int, y: int, direction: str
    ) -> list[tuple[int, int]]:
        if direction == "East":
            affected_areas = [
                (x - 1, y),
                (x, y),
                (x - 1, y - 2),
                (x, y - 2),
                (x - 1, y - 1),
                (x, y - 1),
            ]
        elif direction == "South":
            affected_areas = [
                (x, y - 1),
                (x, y),
                (x - 2, y - 1),
                (x - 2, y),
                (x - 1, y - 1),
                (x - 1, y),
            ]
        elif direction == "West":
            affected_areas = [
                (x + 1, y),
                (x, y),
                (x + 1, y - 2),
                (x, y - 2),
                (x + 1, y - 1),
                (x, y - 1),
            ]
        elif direction == "North":
            affected_areas = [
                (x, y + 1),
                (x, y),
                (x - 2, y + 1),
                (x - 2, y),
                (x - 1, y + 1),
                (x - 1, y),
            ]
        else:
            raise ValueError(
                f"Invalid direction: {direction}. "
                "Valid directions are 'North', 'East', 'South', 'West'."
            )
        filtered_areas = []
        for cx, cy in affected_areas:
            if (
                cx >= 0
                and cx + 2 < self.width
                and cy >= 0
                and cy + 2 < self.height
            ):
                filtered_areas.append((cx, cy))
        return filtered_areas

    def try_break_wall_safely(self, cell: Cell, direction: str) -> bool:
        x, y = cell.position
        self.break_wall(cell, direction)
        for cx, cy in self.get_affected_areas_3x3(x, y, direction):
            if self.is_open_area_3x3(cx, cy):
                self.restore_wall(cell, direction)
                return False
        return True

    def get_all_closed_walls(self) -> list[tuple[Cell, str]]:
        closed_walls = []
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                for direction, is_closed in cell.walls.items():
                    if (
                        (
                            direction == "East"
                            or direction == "South"
                        )
                        and is_closed
                    ):
                        closed_walls.append((cell, direction))
        return closed_walls

    def add_loops(self, ratio: float = 0.15) -> None:
        closed_walls = self.get_all_closed_walls()
        shuffle(closed_walls)
        target = int(len(closed_walls) * ratio)
        broken = 0
        for cell, direction in closed_walls:
            if broken >= target:
                break
            if self.try_break_wall_safely(cell, direction):
                broken += 1


def main() -> None:
    m = Maze(5, 5)
    m.generate_maze(m.grid[0][0])
    m.add_loops()
    path = m.find_shortest_path(m.grid[0][0], m.grid[4][4])
    print(path)


if __name__ == "__main__":
    main()
