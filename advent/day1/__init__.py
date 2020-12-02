from itertools import combinations
from typing import List


def part1(lines: List[int]):
    for a, b in combinations(lines, 2):
        if a + b == 2020:
            print(a * b)
            break


def part2(lines: List[int]):
    for a, b, c in combinations(lines, 3):
        if a + b + c == 2020:
            print(a * b * c)
            break
