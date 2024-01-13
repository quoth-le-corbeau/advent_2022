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
    for key, value in file_structure["/"].items():
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
        current_directory = dict()
        stack = list()
        for line in lines:
            if line.split()[-1] == "ls":
                continue
            elif line.split()[1] == "cd":
                directory_name = line.split()[-1]
                if directory_name == "/":
                    current_directory = dict()
                    stack = list()
                elif directory_name == "..":
                    current_directory = stack.pop()
                else:
                    if directory_name not in current_directory:
                        current_directory[directory_name] = dict()
                    stack.append(current_directory)
                    current_directory = current_directory[directory_name]
            else:
                size_or_dir, name = line.split()
                if size_or_dir == "dir":
                    current_directory[name] = dict()
                else:
                    current_directory[name] = int(size_or_dir)

        return {"/": stack[0]}




helpers.print_timed_results(solution_func=sum_largest_directories)
# helpers.print_timed_results(
#     solution_func=sum_largest_directories, test_path_extension=None
# )
