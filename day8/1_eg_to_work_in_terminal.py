import re
import os
import sys

# needed for running from terminal or in vscode
sys.dont_write_bytecode = True
sys.path.append(os.getcwd())

from result_printer import print_timed_results


def count_visible_trees(file_path: os.path):
    grid = _get_tree_height_grid(file=file_path)
    return _count_visible_trees_in_grid(grid=grid)


def _count_visible_trees_in_grid(grid: list[list[int]]) -> int:
    return 1


def _get_tree_height_grid(file: os.path) -> list[list[int]]:
    with open(file) as puzzle_input:
        lines = puzzle_input.read().splitlines()
        grid = list()
        for line in lines:
            grid.append(list(map(int, re.findall(r"\d+", line))))
        return grid


print_timed_results(day_number="8", solution_func=count_visible_trees)
