import os

import helpers


def sum_item_priorities(file_path: os.path) -> int:
    all_compartments = _get_compartments(file=file_path)
    elf_items = list()
    for compartments in all_compartments:
        first, second = set(compartments[0]), set(compartments[1])
        elf_items += [item for item in first.intersection(second)]
    priorities = list()
    for item in elf_items:
        priorities.append(_get_item_priority(item=item))
    return sum(priorities)


def _get_item_priority(item: str) -> int:
    if ord(item) >= 97:
        return ord(item) - 96
    else:
        return (ord(item) - 64) + 26


def _get_compartments(file: os.path):
    with open(file) as puzzle_input:
        rucksacks = puzzle_input.read().splitlines()
        all_compartments = list()
        for rucksack in rucksacks:
            half_length = len(rucksack) // 2
            compartment_1, compartment_2 = (
                rucksack[:half_length],
                rucksack[half_length:],
            )
            all_compartments.append((compartment_1, compartment_2))
        return all_compartments


helpers.print_timed_results(solution_func=sum_item_priorities)
