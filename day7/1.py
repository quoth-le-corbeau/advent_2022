import os

import helpers

GOAL = {
    "/": {
        "a": {
            "e": {"i": 584},
            "f": 29116,
            "g": 2557,
            "h.lst": 62596,
        },
        "b.txt": 14848514,
        "c.dat": 8504156,
        "d": {
            "j": 4060174,
            "d.log": 8033020,
            "d.ext": 5626152,
            "k": 7214296,
        },
    },
}

TARGET_DIRS = list()
TARGET_SIZE = 100000


def sum_largest_directories(file_path: os.path):
    file_structure = _get_structure(file=file_path)
    print(file_structure)
    for key, value in GOAL["/"].items():
        if isinstance(value, int):
            continue
        elif isinstance(value, dict):
            dir_size = _recursive_sum(directory=value)
            if dir_size <= TARGET_SIZE:
                TARGET_DIRS.append(dir_size)
    return sum(TARGET_DIRS)


def _recursive_sum(directory):
    size = 0
    for key, value in directory.items():
        if not isinstance(value, dict):
            size += value
        else:
            next_directory_sum = _recursive_sum(directory=value)
            size += next_directory_sum
            if next_directory_sum <= TARGET_SIZE:
                TARGET_DIRS.append(next_directory_sum)
    return size


def _get_structure(file: os.path):
    with open(file) as puzzle_input:
        lines = puzzle_input.read().splitlines()
        current_directory = "/"
        structure = {"/": {}}
        lines = lines[1:]
        for i, line in enumerate(lines):
            previous_directory = current_directory
            if line == "$ ls":
                continue
            elif line == "$ cd ..":
                current_directory = previous_directory
                continue
            elif line.split()[0] == "dir":
                new_directory = line.split()[1]
                structure[current_directory][new_directory] = {}
            elif line.split()[1] == "cd" and line.split()[2] != "..":
                directory = line.split()[2]
                


        return structure


helpers.print_timed_results(solution_func=sum_largest_directories)
# helpers.print_timed_results(
#     solution_func=sum_largest_directories, test_path_extension=None
# )
