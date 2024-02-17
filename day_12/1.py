import time
import pathlib
from typing import Any
import numpy as np
import astar


def get_minimal_steps_to_goal(file_path: str) -> int:
    elevation_map_grid = _read_grid_from_file(file=file_path)
    start, goal = _get_start_end_coordinates(grid=elevation_map_grid)
    # print(elevation_map_grid)
    a_star = astar.AStar(
        start=start,
        grid=elevation_map_grid,
        height=len(elevation_map_grid),
        width=len(elevation_map_grid[0]),
    )
    # print(f"{a_star.grid=}")
    # print(f"{a_star.start=}")
    # print(f"{ord(a_star.grid[a_star.start[1]][a_star.start[0]])=}")
    # print(f"{a_star.height=}")
    # print(f"{a_star.width=}")
    # print(f"{a_star.heuristic_manhattan(end_node=astar.Node(position=goal))=}")
    # print(f"{a_star.node_neighbours(node=astar.Node(position=start))=}")
    # print(f"{a_star.node_neighbours(node=astar.Node(position=goal))=}")
    # print(f"{a_star.get_grid_value(position=(4, 2))=}")
    # print(f"{a_star.neighbour_is_not_wall('x', 'y')=}")
    # print(f"{a_star.neighbour_is_not_wall('f', 'e')=}")
    # print(f"{a_star.neighbour_is_not_wall('s', 't')=}")
    # print(f"{a_star.neighbour_is_not_wall('x', 'z')=}")
    # print(f"{a_star.neighbour_is_not_wall('s', 'e')=}")

    print(f"{a_star.compute_path(end_node=astar.Node(position=goal))=}")


def _get_start_end_coordinates(
    grid: np.ndarray[Any, np.dtype[Any]]
) -> tuple[tuple[int, int], tuple[int, int]]:
    points = dict()
    for y, row in enumerate(grid):
        if "S" in row or "E" in row:
            for x, col in enumerate(row):
                if col == "S":
                    points["start"] = (x, y)
                elif col == "E":
                    points["goal"] = (x, y)
                else:
                    continue

    return points["start"], points["goal"]


def _read_grid_from_file(file: str) -> np.ndarray[Any, np.dtype[Any]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        grid = np.array([[s for s in line] for line in lines])
        return grid


start = time.perf_counter()
get_minimal_steps_to_goal("eg.txt")
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
get_minimal_steps_to_goal("input.txt")
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
