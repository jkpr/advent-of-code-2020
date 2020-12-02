from collections import Counter
import re
from typing import List


def part1(lines: List[str]):
    count = 0
    for line in lines:
        found = re.search(r"(\d+)-(\d+) (\w): (\w+)", line)
        if found:
            start, stop, letter, password = found.groups()
            counter = Counter(password)
            hits = counter.get(letter, 0)
            if int(start) <= hits <= int(stop):
                count += 1
    print(count)


def part2(lines: List[int]):
    count = 0
    for line in lines:
        found = re.search(r"(\d+)-(\d+) (\w): (\w+)", line)
        if found:
            start, stop, letter, password = found.groups()
            password += " " * int(stop)
            start_match = password[int(start) - 1] == letter
            stop_match = password[int(stop) - 1] == letter
            if sum((start_match, stop_match)) == 1:
                count += 1
    print(count)
