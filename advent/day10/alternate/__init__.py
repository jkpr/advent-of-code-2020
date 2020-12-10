from collections import defaultdict
from typing import List


def part1(lines: List[int]):
    voltages = sorted(lines)
    voltages.insert(0, 0)
    voltages.append(voltages[-1] + 3)
    diffs = defaultdict(int)
    for a, b in zip(voltages, voltages[1:]):
        diffs[b - a] += 1
    return diffs[1] * diffs[3]


def part2(lines: List[int]):
    voltages = sorted(lines)
    voltages.insert(0, 0)
    voltages.append(voltages[-1] + 3)

    voltages_set = set(voltages)
    network = {}
    for i in voltages:
        possible_connections = set(range(i + 1, i + 4))
        connections = voltages_set & possible_connections
        network[i] = sorted(list(connections))
    paths = {voltages[-1]: 1}
    for j in reversed(voltages[:-1]):
        from_this_node = sum(paths[conn] for conn in network[j])
        paths[j] = from_this_node
    return paths[0]
