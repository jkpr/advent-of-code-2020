import copy
from typing import List


class Boot:
    def __init__(self, data: List[str]):
        self._data = data
        self.initialize()

    def initialize(self):
        self.data = copy.copy(self._data)
        self.accumulator = 0
        self.instruction = 0
        self.exit_code = None
        self.safety = 1_000_000_000

    def step(self):
        """Run the next instuction."""
        self.safety -= 1
        if self.instruction >= len(self.data):
            self.exit_code = 1
        if self.instruction == len(self.data) - 1:
            self.exit_code = 0
        full_instruction = self.data[self.instruction]
        op_code, value = full_instruction.split()
        if op_code == "nop":
            self.instruction += 1
        elif op_code == "acc":
            self.accumulator += int(value)
            self.instruction += 1
        elif op_code == "jmp":
            self.instruction += int(value)

    def copy(self):
        return copy.copy(self)
