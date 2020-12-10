from collections import Counter
from typing import List


def part1(lines: List[str]):
    count = 0
    max_y = len(lines)
    max_x = len(lines[0])
    cur_y = 0
    cur_x = 0
    while cur_y < max_y:
        char = lines[cur_y][cur_x]
        if char == "#":
            count += 1
        cur_x += 3
        cur_x %= max_x
        cur_y += 1
    print(count)


def ski(lines, delta_x, delta_y):
    count = 0
    max_y = len(lines)
    max_x = len(lines[0])
    cur_y = 0
    cur_x = 0
    while cur_y < max_y:
        char = lines[cur_y][cur_x]
        if char == "#":
            count += 1
        cur_x += delta_x
        cur_x %= max_x
        cur_y += delta_y
    return count


def part2(lines: List[str]):
    result = [ski(lines, x, y) for x, y in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))]
    prod = 1
    for i in result:
        prod *= i
    print(prod)
