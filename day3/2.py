import os

import helpers


def sum_item_priorities(file_path: os.path) -> int:
    groups_of_three = _get_compartments(file=file_path)
    badges = list()
    for group in groups_of_three:
        rucksack_1, rucksack_2, rucksack_3 = set(group[0]), set(group[1]), set(group[2])
        badges += [
            item
            for item in rucksack_1.intersection(rucksack_2).intersection(rucksack_3)
        ]
    priorities = list()
    for badge in badges:
        priorities.append(_get_item_priority(item=badge))
    return sum(priorities)


def _get_item_priority(item: str) -> int:
    if ord(item) >= 97:
        return ord(item) - 96
    else:
        return (ord(item) - 64) + 26


def _get_compartments(file: os.path) -> list[list[str]]:
    with open(file) as puzzle_input:
        rucksacks = puzzle_input.read().splitlines()
        groups_of_three = list()
        for i in range(3, len(rucksacks) + 1, 3):
            groups_of_three.append([rucksacks[j] for j in range(i - 3, i)])

    return groups_of_three


helpers.print_timed_results(solution_func=sum_item_priorities)
