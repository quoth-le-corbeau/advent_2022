import os

import helpers

TARGET_DIRECTORY_SIZE = 100000
TARGET_DIRECTORIES = list()


def sum_targed_directories(file_path: os.path):
    file_structure = _build_nested_file_structure(file=file_path)
    for key, value in file_structure.items():
        if isinstance(value, int):
            continue
        else:
            # assume values can only be integers or dictionaries
            size_of_next_inner_directory = _recursive_sum_of_nested_dicts(nested_dict=value)
            if size_of_next_inner_directory <= TARGET_DIRECTORY_SIZE:
                TARGET_DIRECTORIES.append(size_of_next_inner_directory)
    return sum(TARGET_DIRECTORIES)


def _recursive_sum_of_nested_dicts(nested_dict) -> int:
    sum_of_integers_in_outer_dict = 0
    for key, value in nested_dict.items():
        if isinstance(value, int):
            sum_of_integers_in_outer_dict += value
        else:
            sum_of_integers_in_next_inner_dict = _recursive_sum_of_nested_dicts(
                nested_dict=value
            )
            if sum_of_integers_in_next_inner_dict <= TARGET_DIRECTORY_SIZE:
                TARGET_DIRECTORIES.append(sum_of_integers_in_next_inner_dict)
            sum_of_integers_in_outer_dict += sum_of_integers_in_next_inner_dict
    return sum_of_integers_in_outer_dict


def _build_nested_file_structure(file: os.path):
    with open(file) as puzzle_input:
        lines = puzzle_input.read().splitlines()
        current_dir = dict()
        stack = list()
        for line in lines:
            if line.split()[-1] == "ls":
                continue
            elif line.split()[1] == "cd":
                directory_name = line.split()[-1]
                if directory_name == "/":
                    current_dir = dict()
                    stack = list()
                elif directory_name == "..":
                    current_dir = stack.pop()
                else:
                    if directory_name not in current_dir:
                        current_dir[directory_name] = dict()
                    stack.append(current_dir)
                    current_dir = current_dir[directory_name]
            else:
                dir_or_file_size, dir_or_file_name = line.split()
                if dir_or_file_size == "dir":
                    current_dir[dir_or_file_name] = dict()
                else:
                    current_dir[dir_or_file_name] = int(dir_or_file_size)
        return stack[0]


helpers.print_timed_results(
    solution_func=sum_targed_directories, test_path_extension=None
)
