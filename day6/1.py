import os

import helpers


def count_characters_until_marker_detected(file_path: os.path) -> int:
    data_stream = _get_data_stream(file=file_path)
    print(data_stream)


def _get_data_stream(file: os.path) -> str:
    with open(file) as puzzle_input:
        return puzzle_input.read()


helpers.print_timed_results(solution_func=count_characters_until_marker_detected)
