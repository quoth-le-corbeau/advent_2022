import os

import helpers


def calculate_signal_strength(file_path: os.path) -> int:
    program = _parse_program_file(file=file_path)
    cycle_count = 0
    register = 1
    signal_strengths = list()
    for line in program:
        i = 0
        while i < line[0]:
            cycle_count += 1
            if (
                cycle_count == 20
                or cycle_count == 60
                or cycle_count == 100
                or cycle_count == 140
                or cycle_count == 180
                or cycle_count == 220
            ):
                signal_strengths.append(register * cycle_count)
            i += 1
        register += line[1]
    return sum(signal_strengths)


def _parse_program_file(file: os.path) -> list[tuple[int, int]]:
    with open(file) as puzzle_input:
        lines = puzzle_input.read().splitlines()
        program = list()
        for line in lines:
            if line.split()[0] == "noop":
                program.append((1, 0))
            else:
                program.append((2, int(line.split()[1])))
        return program


helpers.print_timed_results(solution_func=calculate_signal_strength)
