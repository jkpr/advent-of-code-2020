from typing import List


LARGE_PRIME = 20201227
PART_ONE_SUBJECT_NUMBER = 7


def determine_loops(key: int) -> int:
    value = 1
    loop_size = 0
    while True:
        loop_size += 1
        value = (value * PART_ONE_SUBJECT_NUMBER) % LARGE_PRIME
        if value == key:
            break
    return loop_size


def find_private_key(subject_number: int, loops: int) -> int:
    value = 1
    for _ in range(loops):
        value = (value * subject_number) % LARGE_PRIME
    return value


def part1(lines: List[str]):
    card_key = int(lines[0])
    door_key = int(lines[1])
    loops = determine_loops(door_key)
    result = find_private_key(card_key, loops)
    return result


def part2(lines: List[str]):
    pass
