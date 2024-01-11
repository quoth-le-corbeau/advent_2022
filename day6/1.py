import os

import helpers


def count_characters_until_marker_detected(file_path: os.path) -> int:
    data_stream = _get_data_stream(file=file_path)
    count = 0
    for i in range(4, len(data_stream), 1):
        last_four_characters = ""
        for x in range(-4, 0):
            last_four_characters += data_stream[i + x]
        if len(set(last_four_characters)) == 4:
            count = i
            break
    return count


def _get_data_stream(file: os.path) -> str:
    with open(file) as puzzle_input:
        return puzzle_input.read()


helpers.print_timed_results(solution_func=count_characters_until_marker_detected)
