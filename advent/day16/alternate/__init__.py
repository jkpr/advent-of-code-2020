from collections import defaultdict
import re
from typing import List

import numpy as np


def parse_input(lines: List[str]):
    chunks = "\n".join(lines).split("\n\n")
    for i, chunk in enumerate(chunks):
        if i == 0:  # rules
            rules = defaultdict(set)
            for line in chunk.split("\n"):
                number_type = re.match(r"([\w ]+): ", line).group(1)
                ranges = re.findall(r"(\d+)-(\d+)", line)
                for lower, upper in ranges:
                    this_range = range(int(lower), int(upper) + 1)
                    rules[number_type].update(this_range)
        if i == 1:  # my ticket
            mine = np.fromstring(chunk.split("\n")[1], dtype=int, sep=",")
        if i == 2:  # nearby tickets
            nearby = np.stack(
                [
                    np.fromstring(line, dtype=int, sep=",")
                    for line in chunk.split("\n")[1:]
                ]
            )
    return rules, mine, nearby


def part1(lines: List[str]):
    rules, mine, nearby = parse_input(lines)
    axis0 = sorted(rules)
    the_cube = np.stack([np.isin(nearby, list(rules[item])) for item in axis0])
    mask = ~np.any(the_cube, axis=0)
    return np.sum(nearby[mask])


def part2(lines: List[str]):
    rules, mine, nearby = parse_input(lines)
    axis0 = np.array(sorted(rules))
    the_cube = np.stack([np.isin(nearby, list(rules[item])) for item in axis0])
    row_mask = np.all(np.any(the_cube, axis=0), axis=1)
    good_cube = the_cube[:, row_mask, :]
    field_by_col = np.all(good_cube, axis=1)
    solution = np.zeros(field_by_col.shape, dtype=bool)
    while np.sum(field_by_col) > 0:
        fields_solved = np.sum(field_by_col, axis=1) == 1
        columns_solved = np.sum(field_by_col[fields_solved, :], axis=0) == 1
        solution[fields_solved, columns_solved] = field_by_col[
            fields_solved, columns_solved
        ]
        field_by_col[:, columns_solved] = False
    idx = np.any(solution[np.char.startswith(axis0, "departure")], axis=0)
    return np.prod(mine[idx])
