from typing import List


def part1(lines: List[str]):
    result = []
    for line in lines:
        front = line[:7]
        front_bin = ''.join('0' if a == 'F' else '1' for a in front)
        front_int = int(front_bin, base=2)
        side = line[7:]
        side_bin = ''.join('0' if a == 'L' else '1' for a in side)
        side_int = int(side_bin, base=2)
        seat_id = front_int * 8 + side_int
        result.append(seat_id)
    print(max(result))


def part2(lines: List[int]):
    result = []
    for line in lines:
        front = line[:7]
        front_bin = ''.join('0' if a == 'F' else '1' for a in front)
        front_int = int(front_bin, base=2)
        side = line[7:]
        side_bin = ''.join('0' if a == 'L' else '1' for a in side)
        side_int = int(side_bin, base=2)
        seat_id = front_int * 8 + side_int
        result.append(seat_id)
    result_set = set(result)
    comp = set(range(max(result))) - result_set
    print(sorted(list(comp)))