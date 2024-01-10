import os

import helpers


def find_most_calories(file_path: os.path):
    return max(_get_all_elf_calories(file=file_path))


def _get_all_elf_calories(file: os.path) -> list[int]:
    with open(file) as puzzle_input:
        calories_per_elf = puzzle_input.read().split("\n\n")
        total_calories_per_elf = list()
        for elf in calories_per_elf:
            all_calories_strings = elf.strip().split("\n")
            total_calories_per_elf.append(sum(list(map(int, all_calories_strings))))
    return total_calories_per_elf


helpers.print_timed_results(solution_func=find_most_calories)
