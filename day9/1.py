import math
import os
from dataclasses import dataclass
import helpers


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


class Tail(Head):

    def follow_head(self, head: Head):
        horizontal_distance = abs(self.x - head.x)
        vertical_distance = abs(self.y - head.y)
        hypoteneuse = math.sqrt(horizontal_distance ** 2 + vertical_distance ** 2)
        move_condition = hypoteneuse > math.sqrt(2)
        is_horizontal_move = self.y - head.y == 0
        is_vertical_move = self.x - head.x == 0
        is_diagonal_move = not (is_horizontal_move or is_vertical_move)
        head_coordinates = head.x, head.y
        if move_condition and is_diagonal_move:
            self.x, self.y = head_coordinates
        elif horizontal_distance > 1:
            assert vertical_distance == 0
            if self.x > head.x:
                self.x -= 1
            else:
                self.x += 1
        else:
            if self.y > head.y:
                self.y -= 1
            else:
                self.y += 1



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
