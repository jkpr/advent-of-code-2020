import itertools
import re
from typing import List


def apply_mask(mask, value):
    bin_val = bin(value)[2:]
    full_val = bin_val.zfill(36)
    result = []
    for m, v in zip(mask, full_val):
        if m == "1" or m == "0":
            result.append(m)
        else:
            result.append(v)
    combined = "".join(result)
    return int(combined, base=2)


def part1(lines: List[str]):
    answers = {}
    for line in lines:
        cur_mask = ""
        if line.startswith("mask = "):
            mask = line[7:]
        else:
            groups = re.match(r"mem\[(\d+)\] = (\d+)", line).groups()
            address = int(groups[0])
            value = int(groups[1])
            new_value = apply_mask(mask, value)
            answers[address] = new_value
    return sum(answers.values())


def apply_mask_v2(mask, address):
    bin_val = bin(address)[2:]
    full_val = bin_val.zfill(36)
    partial_mask = []
    for m, v in zip(mask, full_val):
        if m == "0":
            partial_mask.append(v)
        else:
            partial_mask.append(m)
    x_count = partial_mask.count("X")
    product = itertools.product(["0", "1"], repeat=x_count)
    result = []
    for i in product:
        temp = []
        x_fill = list(i)
        for j in partial_mask:
            if j == "X":
                temp.append(x_fill.pop(0))
            else:
                temp.append(j)
        combined = "".join(temp)
        result.append(int(combined, base=2))
    return result


def part2(lines: List[str]):
    answers = {}
    for line in lines:
        cur_mask = ""
        if line.startswith("mask = "):
            mask = line[7:]
        else:
            groups = re.match(r"mem\[(\d+)\] = (\d+)", line).groups()
            address = int(groups[0])
            value = int(groups[1])
            new_addresses = apply_mask_v2(mask, address)
            for new_address in new_addresses:
                answers[new_address] = value
    return sum(answers.values())
