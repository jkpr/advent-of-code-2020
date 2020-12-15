from typing import List


def elf_memory_game(nums, limit):
    last = {}
    pos = 1
    for num in nums:
        last[num] = pos
        pos += 1
    next_num = 0
    while pos <= limit:
        curr_num = next_num
        if curr_num in last:
            next_num = pos - last[curr_num]
        else:
            next_num = 0
        last[curr_num] = pos
        pos += 1
    return curr_num


def part1(lines: List[str]):
    nums = [int(i) for i in lines[0].split(",")]
    return elf_memory_game(nums, 2020)


def part2(lines: List[str]):
    nums = [int(i) for i in lines[0].split(",")]
    return elf_memory_game(nums, 30_000_000)
