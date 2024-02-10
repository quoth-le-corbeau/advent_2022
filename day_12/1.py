import time
import pathlib
from typing import Any
import numpy as np
import heapq


def get_minimal_steps_to_goal(file_path: str) -> int:
    elevation_map_grid = _read_grid_from_file(file=file_path)
    start, goal = _get_start_end_coordinates(grid=elevation_map_grid)
    return a_star(grid=elevation_map_grid, start=start, goal=goal)
    # f = g + h
    # f = total cost of node
    # g = distance between start and current node
    # h = heuristic (estimated distance from current node to start node)


def a_star(
    grid: np.ndarray[Any, np.dtype[Any]], start: tuple[int, int], goal: tuple[int, int]
) -> list[tuple[int, int]]:
    neighbour_moves = [
        (0, 1),
        (-1, 0),
        (0, -1),
        (1, 0),
    ]  # up left down right N, W, S, E
    closed_set = set()
    parents = dict()
    g_scores = {start: 0}
    f_scores = {start: heuristic(current=start, goal=goal)}  # g = 0
    open_heap = list()
    heapq.heappush(open_heap, (f_scores[start], start))

    while len(open_heap) > 0:
        current = heapq.heappop(open_heap)[1]
        if current == goal:
            data = list()
            while current in parents:
                data.append(current)
                current = parents[current]
            return data
        else:
            closed_set.add(current)
            for x, y in neighbour_moves:
                neighbour = current[0] + x, current[1] + y
                tentative_g_score = g_scores[current] + heuristic(
                    current=current, goal=neighbour
                )
                if 0 <= neighbour[0] <= grid.shape[0]:
                    if 0 <= neighbour[1] < grid.shape[1]:
                        neighbour_value = grid[neighbour[1]][neighbour[0]]
                        current_value = grid[current[1]][current[0]]
                        if (
                            neighbour_value != "S"
                            and abs(ord(neighbour_value) - ord(current_value)) > 1
                        ):
                            continue

                    else:
                        continue
                else:
                    continue

                if neighbour in closed_set and tentative_g_score > g_scores.get(
                    neighbour, 0
                ):
                    continue
                if tentative_g_score < g_scores.get(neighbour, 0) or neighbour not in [
                    heap[1] for heap in open_heap
                ]:
                    parents[neighbour] = current
                    g_scores[neighbour] = tentative_g_score
                    f_scores[neighbour] = tentative_g_score + heuristic(
                        current=neighbour, goal=goal
                    )
                    heapq.heappush(open_heap, (f_scores[neighbour], neighbour))


def heuristic(current: tuple[int, int], goal: tuple[int, int]) -> int:
    horizontal = goal[0] - current[0]
    vertical = goal[1] - current[1]
    return horizontal + vertical


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
