import os

import helpers


def get_total_game_strategy_points(file_path: os.path) -> int:
    strategy_guides = _get_strategy_guides(file=file_path)
    points = 0
    for game in strategy_guides:
        elf_choice = game[0]
        my_strategy = game[1]
        if my_strategy == "Y":
            points += 3
            my_choice = elf_choice
        elif my_strategy == "X":
            my_choice = _make_correct_decision(opponent_choice=elf_choice, win=False)
        elif my_strategy == "Z":
            points += 6
            my_choice = _make_correct_decision(opponent_choice=elf_choice, win=True)
        else:
            raise ValueError("my strategy is impossible who wrote this damn guide?")
        points += _points_per_choice(choice=my_choice)
    return points


def _make_correct_decision(opponent_choice: str, win: bool) -> str:
    if win:
        if opponent_choice == "A":
            return "B"
        elif opponent_choice == "B":
            return "C"
        elif opponent_choice == "C":
            return "A"
    else:
        if opponent_choice == "A":
            return "C"
        elif opponent_choice == "B":
            return "A"
        elif opponent_choice == "C":
            return "B"


def _points_per_choice(choice: str) -> int:
    if choice == "A":
        return 1
    elif choice == "B":
        return 2
    elif choice == "C":
        return 3
    else:
        raise ValueError("choice must be A B or C")


def _get_strategy_guides(file: os.path) -> list[tuple[str, str]]:
    with open(file) as puzzle_input:
        games = puzzle_input.read().splitlines()
        strategy_guides = list()
        for game in games:
            strategy_guides.append((game.split()[0], game.split()[1]))
    return strategy_guides


helpers.print_timed_results(solution_func=get_total_game_strategy_points)
