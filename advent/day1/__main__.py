from typing import List

from ..utils import cli, get_input_file, read_lines
from . import part1, part2


def main(lines: List, second_part: bool = False):
    if not second_part:
        part1(lines)
    else:
        part2(lines)


if __name__ == "__main__":
    args = cli()
    source = get_input_file(puzzle_data=args.puzzle_data, module_path=__file__)
    lines = read_lines(source, to_int=True)
    main(lines, second_part=args.second_part)
