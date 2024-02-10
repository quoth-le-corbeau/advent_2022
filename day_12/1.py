import time
import pathlib
from typing import Any

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import heapq

from numpy import ndarray, dtype


def get_minimal_steps_to_goal(file_path: str) -> int:
    elevation_map_grid = _read_grid_from_file(file=file_path)
    start, goal = _get_start_end_coordinates(grid=elevation_map_grid)
    print(start, goal)
    # f = g + h
    # f = total cost of node
    # g = distance between start and current node
    # h = heuristic (estimated distance from current node to start node)


def _get_start_end_coordinates(
    grid: ndarray[Any, dtype[Any]]
) -> tuple[tuple[int, int], tuple[int, int]]:
    points = dict()
    for y, row in enumerate(grid):
        if "S" in row or "E" in enumerate(row):
            for x, col in row:
                if col == "S" or col == "E":
                    points["start"] = (x, y)
                elif col == "E":
                    points["goal"] = (x, y)
                else:
                    continue

    return points["start"], points["goal"]


def _read_grid_from_file(file: str) -> ndarray[Any, dtype[Any]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        grid = np.array([line.split() for line in lines])
        return grid


start = time.perf_counter()
get_minimal_steps_to_goal("eg.txt")
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
get_minimal_steps_to_goal("input.txt")
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
