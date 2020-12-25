from itertools import accumulate, islice, repeat
from typing import List


def part1(lines: List[str]):
    init = [int(i) - 1 for i in lines[0]]
    init_offset = init[1:] + init[:1]
    cups = dict(zip(init, init_offset))
    N = len(init)
    curr = init[0]
    for _ in range(100):
        rem1 = cups[curr]
        rem2 = cups[rem1]
        rem3 = cups[rem2]
        all_rem = {rem1, rem2, rem3}
        cups[curr] = cups[rem3]
        dest = next(
            (curr - i) % N for i in range(1, 5) if (curr - i) % N not in all_rem
        )
        temp = cups[dest]
        cups[dest] = rem1
        cups[rem3] = temp
        curr = cups[curr]
    result = "".join(
        str(i + 1)
        for i in islice(
            accumulate(repeat(None), lambda x, _: cups[x], initial=cups[0]), N - 1
        )
    )
    return result


def part2(lines: List[str]):
    init = [int(i) - 1 for i in lines[0]]
    init.extend(range(len(init), 1_000_000))
    init_offset = init[1:] + init[:1]
    cups = dict(zip(init, init_offset))
    N = len(init)
    curr = init[0]
    for _ in range(10_000_000):
        rem1 = cups[curr]
        rem2 = cups[rem1]
        rem3 = cups[rem2]
        all_rem = {rem1, rem2, rem3}
        cups[curr] = cups[rem3]
        dest = next(
            (curr - i) % N for i in range(1, 5) if (curr - i) % N not in all_rem
        )
        temp = cups[dest]
        cups[dest] = rem1
        cups[rem3] = temp
        curr = cups[curr]
    next1 = cups[0]
    next2 = cups[next1]
    return (next1 + 1) * (next2 + 1)
