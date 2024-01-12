import time
from typing import Optional


def print_timed_results(
    solution_func: callable, test_path_extension: Optional[str] = "eg.txt"
):
    test_path = test_path_extension if test_path_extension is not None else None
    real_path = "input.txt"

    if test_path is not None:
        start = time.perf_counter()
        print(solution_func(test_path))
        print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
    start = time.perf_counter()
    print(solution_func(real_path))
    print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
