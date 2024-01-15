import os
from dataclasses import dataclass
import helpers


@dataclass(frozen=True)
class Head:
    x: int
    y: int

    def move(self, direction: str, spaces: int):
        if direction == "U":
            self.y += spaces
        elif direction == "D":
            self.y -= spaces
        elif direction == "R":
            self.x += spaces
        elif direction == "L":
            self.x -= spaces

@dataclass(frozen=True)
class Tail(Head):

    def follow_head(self, head: Head):
        head_coordinates = head.x, head.y
        is_horizontal = self.y - head.y == 0
        is_vertical = self.x - head.x == 0



def count_tail_positions(file_path: os.path) -> int:
    instructions = _get_instructions(file=file_path)
    print(instructions)


def _get_instructions(file: os.path) -> list[tuple[str, int]]:
    with open(file) as puzzle_input:
        lines = puzzle_input.read().splitlines()
        instructions = list()
        for line in lines:
            direction, spaces = line.split()
            instructions.append((direction, int(spaces)))
        return instructions


helpers.print_timed_results(solution_func=count_tail_positions)
