from typing import List


def part1(lines: List[int]):
    preamble = 25
    # preamble = 5  # for testing
    for i in range(preamble, len(lines)):
        target = lines[i]
        previous_list = lines[slice(i - preamble, i)]
        previous_set = set(previous_list)
        for num in previous_list:
            diff = target - num
            if diff in previous_set:
                break
        else:
            return target


def part2(lines: List[int]):
    target = part1(lines)
    for i in range(len(lines) - 2):
        for j in range(i + 2, len(lines)):
            window = lines[slice(i, j)]
            this_sum = sum(window)
            if this_sum == target:
                result = min(window) + max(window)
                return result
            elif this_sum > target:
                break
