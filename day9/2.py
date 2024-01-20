import math
import os
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

    def follow_tail(self, head: Head):
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
    tail_1 = Tail(x=0, y=0)
    tail_2 = Tail(x=0, y=0)
    tail_3 = Tail(x=0, y=0)
    tail_4 = Tail(x=0, y=0)
    tail_5 = Tail(x=0, y=0)
    tail_6 = Tail(x=0, y=0)
    tail_7 = Tail(x=0, y=0)
    tail_8 = Tail(x=0, y=0)
    tail_9 = Tail(x=0, y=0)
    positions: set[tuple[int, int]] = {(0, 0)}
    for instruction in instructions:
        spaces = 0
        direction = instruction[0]
        while spaces < instruction[1]:
            head.move(direction=direction)
            if tail_1.has_to_move(head):
                tail_1.follow_head(head)
            if tail_2.has_to_move(tail_1):
                tail_2.follow_head(tail_1)
            if tail_3.has_to_move(tail_2):
                tail_3.follow_head(tail_2)
            if tail_4.has_to_move(tail_3):
                tail_4.follow_head(tail_3)
            if tail_5.has_to_move(tail_4):
                tail_5.follow_head(tail_4)
            if tail_6.has_to_move(tail_5):
                tail_6.follow_head(tail_5)
            if tail_7.has_to_move(tail_6):
                tail_7.follow_head(tail_6)
            if tail_8.has_to_move(tail_7):
                tail_8.follow_head(tail_7)
            if tail_9.has_to_move(tail_8):
                tail_9.follow_head(tail_8)
                positions.add((tail_9.x, tail_9.y))
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
helpers.print_timed_results(
    solution_func=count_tail_positions, test_path_extension="eg1.txt"
)
