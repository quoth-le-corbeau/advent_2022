import os
import re

import helpers


def find_fully_contained_ranges(file_path: os.path):
    range_pairs = _get_range_pairs(file=file_path)
    fully_contained_count = 0
    for pair in range_pairs:
        range_1_start, range_1_end = pair[0][0], pair[0][1]
        range_2_start, range_2_end = pair[1][0], pair[1][1]
        if (range_1_start >= range_2_start and range_1_end <= range_2_end) or (
            range_2_start >= range_1_start and range_2_end <= range_1_end
        ):
            fully_contained_count += 1
    return fully_contained_count


def _get_range_pairs(file: os.path) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    with open(file) as puzzle_input:
        lines = puzzle_input.read().splitlines()
        range_pairs: list[tuple[tuple[int, int], tuple[int, int]]] = list()
        for line in lines:
            range_1, range_2 = (
                re.findall(r"\d+", line.split(",")[0]),
                re.findall(r"\d+", line.split(",")[1]),
            )
            range_1_pair = int(range_1[0]), int(range_1[1])
            range_2_pair = int(range_2[0]), int(range_2[1])
            range_pairs.append((range_1_pair, range_2_pair))
        return range_pairs


helpers.print_timed_results(solution_func=find_fully_contained_ranges)
