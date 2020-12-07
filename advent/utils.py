import argparse
from pathlib import Path
from typing import Callable, List, Union


def read_lines(input_file: Path, input_to_int: bool = False) -> Union[List[str], List[int]]:
    with open(input_file) as f:
        if input_to_int:
            return [int(line) for line in f]
        return f.read().splitlines()


def get_input_file(puzzle_data: str = None, module_path: str = None, test_input: bool = False) -> Path:
    if puzzle_data:
        return Path(puzzle_data)
    source = "test_input.txt" if test_input else "input.txt"
    if module_path:
        return Path(module_path).parent.joinpath(source)
    return Path(source)


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Advent of Code parser")
    parser.add_argument("-i", "--puzzle_data", help="Puzzle input file.")
    parser.add_argument(
        "-2", "--second_part", help="Run the second part.", action="store_true"
    )
    parser.add_argument("-t", "--test_input", help="Search for 'test_input.txt' for puzzle input file", action="store_true")
    args = parser.parse_args()
    return args


def common_main(module_path: str, input_to_int: bool, part1: Callable[[list], None], part2: Callable[[list], None]):
    """Run a common main method.

    Args:
        module_path: __file__ from the calling module. This helps find the input text file.
        input_to_int: Should the input be converted to integer?
        part1: A callable taking a list (lines of the input file) and printing the result
        part2: A callable taking a list (lines of the input file) and printing the result
    """
    args = cli()
    source = get_input_file(puzzle_data=args.puzzle_data, module_path=module_path, test_input=args.test_input)
    lines = read_lines(source, input_to_int=input_to_int)
    if not args.second_part:
        part1(lines)
    else:
        part2(lines)
