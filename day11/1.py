import time
import pathlib
import re


def calculate_monkey_business_over_20_rounds(file: str) -> int:
    attributes_per_monkey = _get_attributes_per_monkey(file=file)
    print(attributes_per_monkey)


def _get_attributes_per_monkey(
    file: str,
) -> dict[int, list[list, str, int, tuple[int, int]]]:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        blocks = puzzle_input.read().split("\n\n")
        attributes_per_monkey = list()
        for i, block in enumerate(blocks):
            attributes = dict()
            monkey = block.split("\n")
            items = list(map(int, re.findall(r"\d+", monkey[1])))
            operation = monkey[2].split("=")[-1].strip()
            divisible = int(monkey[3].split()[-1])
            throw_to_options = int(monkey[4].split()[-1]), int(monkey[5].split()[-1])
            attributes[i] = [items, operation, divisible, throw_to_options]
            attributes_per_monkey.append(attributes)
        return attributes_per_monkey


start = time.perf_counter()
calculate_monkey_business_over_20_rounds("eg.txt")
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
start = time.perf_counter()
calculate_monkey_business_over_20_rounds("input.txt")
print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
