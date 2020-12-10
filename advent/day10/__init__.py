from collections import Counter
from itertools import groupby
from typing import List


def part1(lines: List[int]):
    sorted_list = sorted(lines)
    sorted_list.insert(0, 0)
    sorted_list.append(sorted_list[-1] + 3)
    diffs = [b - a for a, b in zip(sorted_list, sorted_list[1:])]
    counter = Counter(diffs)
    return counter.get(3) * counter.get(1)


def part2(lines: List[int]):
    sorted_list = sorted(lines)
    sorted_list.insert(0, 0)
    sorted_list.append(sorted_list[-1] + 3)
    diffs = [b - a for a, b in zip(sorted_list, sorted_list[1:])]
    runs_of_one = [len(list(g)) for k, g in groupby(diffs) if k == 1]
    solutions = {
        1: 1,
        2: 2,
        3: 4,
        4: 7,
        5: 13,
        6: 24,
    }
    transforms = [solutions[k] for k in runs_of_one]
    product = 1
    for i in transforms:
        product *= i
    return product
