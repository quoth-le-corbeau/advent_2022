import math
import os
from dataclasses import dataclass
import helpers


class Head:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, direction: str):
        if direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1


class Tail(Head):
    def has_to_move(self, head: Head) -> bool:
        hypotenuse = self.get_hypotenuse(head)
        return hypotenuse > math.sqrt(2)

    def get_hypotenuse(self, head: Head) -> float:
        horizontal_distance = abs(self.x - head.x)
        vertical_distance = abs(self.y - head.y)
        return math.sqrt(horizontal_distance**2 + vertical_distance**2)

    def follow_head(self, head: Head):
        is_diagonal_move = (
            abs(self.y - head.y) == 2 and abs(self.x - head.x) == 1
        ) or (abs(self.y - head.y) == 1 and abs(self.x - head.x)) == 2
        if is_diagonal_move:
            if abs(head.y - self.y) == 1:
                if head.x - self.x == 2:
                    self.x, self.y = head.x - 1, head.y
                elif head.x - self.x == -2:
                    self.x, self.y = head.x + 1, head.y
            elif abs(head.x - self.x) == 1:
                if head.y - self.y == 2:
                    self.x, self.y = head.x, head.y - 1
                elif head.y - self.y == -2:
                    self.x, self.y = head.x, head.y + 1
        elif self.y == head.y:
            if self.x > head.x:
                self.x = head.x + 1
            else:
                self.x = head.x - 1
        else:
            if self.y > head.y:
                self.y = head.y + 1
            else:
                self.y = head.y - 1


def count_tail_positions(file_path: os.path) -> int:
    instructions = _get_instructions(file=file_path)
    head = Head(x=0, y=0)
    tail = Tail(x=0, y=0)
    positions: set[tuple[int, int]] = {(tail.x, tail.y)}
    for instruction in instructions:
        spaces = 0
        direction = instruction[0]
        while spaces < instruction[1]:
            head.move(direction=direction)
            if tail.has_to_move(head):
                tail.follow_head(head)
                positions.add((tail.x, tail.y))
            spaces += 1
    return len(positions)


def _get_instructions(file: os.path) -> list[tuple[str, int]]:
    with open(file) as puzzle_input:
        lines = puzzle_input.read().splitlines()
        instructions = list()
        for line in lines:
            direction, spaces = line.split()
            instructions.append((direction, int(spaces)))
        return instructions


helpers.print_timed_results(solution_func=count_tail_positions)
