import copy
from typing import List

from ..boot import Boot


def part1(lines: List[str]):
    boot = Boot(lines)
    seen = set()
    while boot.safety > 0 and boot.instruction not in seen:
        seen.add(boot.instruction)
        boot.step()
    print(boot.accumulator)


def run_experiment(i, lines):
    boot = Boot(lines)
    if boot.data[i].startswith("nop "):
        boot.data[i] = boot.data[i].replace("nop ", "jmp ")
    elif boot.data[i].startswith("jmp "):
        boot.data[i] = boot.data[i].replace("jmp ", "nop ")
    seen = set()
    while boot.safety > 0 and boot.instruction not in seen and boot.exit_code is None:
        seen.add(boot.instruction)
        boot.step()
    if boot.exit_code == 0:
        print(boot.accumulator)


def part2(lines: List[str]):
    for i in range(len(lines)):
        run_experiment(i, lines)
