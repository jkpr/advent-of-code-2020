from collections import defaultdict
from itertools import product
from typing import List


def get_neighbors(loc):
    """Return all neighbors of loc, not loc."""
    dim = len(loc)
    offsets = product((-1, 0, 1), repeat=dim)
    neighbors = set()
    for offset in offsets:
        if offset == (0,) * dim:
            continue
        neighbors.add(tuple(a + b for a, b in zip(loc, offset)))
    return neighbors


def get_all_neighbors(locs):
    """Return all neighbors of all locs."""
    neighbors = (get_neighbors(loc) for loc in locs)
    return set.union(*neighbors)


def initialize(lines, dim):
    """Set up first generation based on input."""
    start_gen = defaultdict(int)
    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            if letter == "#":
                start_gen[(i, j) + (0,) * (dim - 2)] = 1
    return start_gen


def cycle(start, times):
    """Advance game from start a number of times."""
    current_gen = start
    for _ in range(times):
        next_gen = defaultdict(int)
        all_locs = get_all_neighbors(current_gen.keys())
        all_locs.update(current_gen.keys())
        for loc in all_locs:
            neighbors = get_neighbors(loc)
            count = sum(current_gen[n] for n in neighbors)
            if count in (2, 3) and current_gen[loc] == 1:
                next_gen[loc] = 1
            elif count == 3 and current_gen[loc] == 0:
                next_gen[loc] = 1
        current_gen = next_gen
    return current_gen


def part1(lines: List[str]):
    start_gen = initialize(lines, 3)
    end_gen = cycle(start_gen, 6)
    return sum(end_gen.values())


def part2(lines: List[str]):
    start_gen = initialize(lines, 4)
    end_gen = cycle(start_gen, 6)
    return sum(end_gen.values())
