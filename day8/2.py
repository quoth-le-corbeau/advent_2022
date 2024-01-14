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
                left_count = 0
                right_count = 0
                up_count = 0
                down_count = 0
                # look left
                i = 1
                while x - i >= 0 and row[x - i] < tree:
                    left_count += 1
                    i += 1
                # look right
                k = 1
                while x + k < len(row) and row[x + k] < tree:
                    right_count += 1
                    k += 1
                # look up
                j = 1
                while y - j >= 0 and grid[y - j][x] < tree:
                    up_count += 1
                    j += 1
                # look down
                l = 1
                while y + l < len(grid) and grid[y + l][x] < tree:
                    down_count += 1
                    l += 1
                left_count += 1
                right_count += 1
                up_count += 1
                down_count += 1
                scenic_scores.append(left_count * right_count * up_count * down_count)
    print(f"{scenic_scores=}")
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
