import argparse
from pathlib import Path
from typing import List, Union


def read_lines(input_file: Path, to_int: bool = False) -> Union[List[str], List[int]]:
    with open(input_file) as f:
        if to_int:
            return [int(line) for line in f]
        return f.read().splitlines()


def get_input_file(puzzle_data: str = None, module_path: str = None) -> Path:
    if puzzle_data:
        return Path(puzzle_data)
    source = puzzle_data if puzzle_data else "input.txt"
    if module_path:
        return Path(module_path).parent.joinpath(source)
    return Path(source)


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Advent of Code parser")
    parser.add_argument("-i", "--puzzle_data", help="Puzzle input file.")
    parser.add_argument(
        "-2", "--second_part", help="Run the second part.", action="store_true"
    )
    args = parser.parse_args()
    return args
