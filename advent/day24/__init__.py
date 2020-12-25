from typing import List, Tuple


OFFSETS = {
    "e": (1, -1, 0),
    "w": (-1, 1, 0),
    "nw": (0, 1, -1),
    "ne": (1, 0, -1),
    "se": (0, -1, 1),
    "sw": (-1, 0, 1),
}


def apply_sequence(line: str) -> Tuple[int, int, int]:
    xyz = 0, 0, 0
    i = 0
    while i < len(line):
        if line[i] in ("e", "w"):
            direction = OFFSETS[line[i]]
            i += 1
        else:
            direction = OFFSETS[line[i : i + 2]]
            i += 2
        xyz = tuple(a + b for a, b in zip(xyz, direction))
    return xyz


def initialize(lines: List[str]) -> set:
    black = set()
    for line in lines:
        xyz = apply_sequence(line)
        if xyz in black:
            black.discard(xyz)
        else:
            black.add(xyz)
    return black


def part1(lines: List[str]):
    black = initialize(lines)
    return len(black)


def get_neighbors(point) -> set:
    neighbors = set()
    for offset in OFFSETS.values():
        neighbors.add(tuple(a + b for a, b in zip(point, offset)))
    return neighbors


def get_all_neighbors(black) -> set:
    return set.union(*[get_neighbors(b) for b in black])


def part2(lines: List[str]):
    black = initialize(lines)
    for _ in range(100):
        black_to_white = set()
        for b in black:
            neighbors = get_neighbors(b)
            black_neighbors = len(black & neighbors)
            if black_neighbors == 0 or black_neighbors > 2:
                black_to_white.add(b)
        white_to_black = set()
        for white_neighbor in get_all_neighbors(black) - black:
            neighbors = get_neighbors(white_neighbor)
            black_neighbors = len(black & neighbors)
            if black_neighbors == 2:
                white_to_black.add(white_neighbor)
        black -= black_to_white
        black |= white_to_black
    return len(black)
