import os

import helpers


def find_most_calories(file_path: os.path):
    top_three_elves = [
        _get_all_elf_calories(file=file_path)[i] for i in range(-1, -4, -1)
    ]
    return sum(top_three_elves)


def _get_all_elf_calories(file: os.path) -> list[int]:
    with open(file) as puzzle_input:
        calories_per_elf = puzzle_input.read().split("\n\n")
        total_calories_per_elf = list()
        for elf in calories_per_elf:
            all_calories_strings = elf.strip().split("\n")
            total_calories_per_elf.append(sum(list(map(int, all_calories_strings))))
    return sorted(total_calories_per_elf)


helpers.print_timed_results(solution_func=find_most_calories)
