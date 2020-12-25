from collections import defaultdict
from itertools import chain
import math
import re
from typing import List


def parse_input(lines: List[str]):
    rules = defaultdict(set)
    mine = []
    nearby = []
    chunks = "\n".join(lines).split("\n\n")
    for i, chunk in enumerate(chunks):
        if i == 0:  # rules
            for line in chunk.split("\n"):
                number_type = re.match(r"([\w ]+): ", line).group(1)
                ranges = re.findall(r"(\d+)-(\d+)", line)
                for lower, upper in ranges:
                    this_range = range(int(lower), int(upper) + 1)
                    rules[number_type].update(this_range)
        if i == 1:  # my ticket
            mine = [int(j) for j in chunk.split("\n")[1].split(",")]
        if i == 2:  # nearby tickets
            for line in chunk.split("\n")[1:]:
                nearby.append([int(j) for j in line.split(",")])
    return rules, mine, nearby


def part1(lines: List[str]):
    rules, _, nearby = parse_input(lines)
    valid = set.union(*rules.values())
    return sum(i for i in chain(*nearby) if i not in valid)


def part2(lines: List[str]):
    rules, mine, nearby = parse_input(lines)
    valid = set.union(*rules.values())
    # Keep all "good" entries from "Nearby tickets"
    good = filter(lambda line: all(x in valid for x in line), nearby)
    # Now, build up a list of "possible" solutions.
    # Keys are the field, e.g. "seat",
    # and values are the set of column indices with
    # entries that all fall into the field's range
    # of valid numbers.
    possible = defaultdict(set)
    for i, col in enumerate(zip(*good)):
        for key, val in rules.items():
            if all(j in val for j in col):
                possible[key].add(i)
    # Build up a solution dictionary.
    # Keys are the field, e.g. "seat",
    # and values are the column index
    # that must match the field.
    solution = {}
    while possible:
        solved_field = set()
        for field, cols in possible.items():
            if len(cols) == 1:
                solved_field.add(field)
        solved_col = set()
        for field in solved_field:
            col = possible.pop(field).pop()
            solution[field] = col
            solved_col.add(col)
        for col in solved_col:
            for cols in possible.values():
                cols.discard(col)
    return math.prod(mine[v] for k, v in solution.items() if k.startswith("departure"))
