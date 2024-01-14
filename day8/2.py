import os

import helpers


def find_most_scenic_tree(file_path: os.path):
    grid = _get_tree_height_grid(file=file_path)
    return find_highest_scenic_score(grid=grid)


def find_highest_scenic_score(grid: list[list[int]]) -> int:
    scenic_scores = list()
    for y, row in enumerate(grid):
        for x, tree in enumerate(row):
            if y == 0 or x == 0 or y == len(grid) - 1 or x == len(row) - 1:
                continue
            else:
                left = 0
                right = 0
                up = 0
                down = 0
                # look left
                i = 1
                while x - i >= 0 and row[x - i] < tree:
                    left += 1
                    i += 1
                if x - i >= 0:
                    left += 1
                # look right
                i = 1
                while x + i < len(row) and row[x + i] < tree:
                    right += 1
                    i += 1
                if x + i <= len(row) - 1:
                    right += 1
                # look up
                j = 1
                while y - j >= 0 and grid[y - j][x] < tree:
                    up += 1
                    j += 1
                if y - j >= 0:
                    up += 1
                # look down
                j = 1
                while y + j < len(grid) and grid[y + j][x] < tree:
                    down += 1
                    j += 1
                if y + j <= len(grid) - 1:
                    down += 1
                scenic_score = left * right * up * down
                scenic_scores.append(scenic_score)
    return max(scenic_scores)


def _get_tree_height_grid(file: os.path) -> list[list[int]]:
    with open(file) as puzzle_input:
        lines = puzzle_input.read().split("\n")
        grid = list()
        for line in lines:
            line = line.split()
            for string in line:
                row = list()
                for char in string:
                    row.append(int(char))
                grid.append(row)

        return grid


helpers.print_timed_results(solution_func=find_most_scenic_tree)
