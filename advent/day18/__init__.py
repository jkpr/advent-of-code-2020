from typing import List


def evaluate(line, precedence):
    output = []
    operators = []
    for ch in line:
        if ch == "(":
            operators.append(ch)
        elif ch in ("*", "+"):
            while (
                operators
                and operators[-1] != "("
                and precedence[operators[-1]] >= precedence[ch]
            ):
                output.append(operators.pop())
            operators.append(ch)
        elif ch == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())
            operators.pop()
        elif ch in "0123456789":
            output.append(ch)
    while operators:
        output.append(operators.pop())
    result = []
    for item in output:
        if item in "0123456789":
            result.append(int(item))
        elif item == "*":
            a = result.pop()
            b = result.pop()
            result.append(a * b)
        elif item == "+":
            a = result.pop()
            b = result.pop()
            result.append(a + b)
    return result[0]


def part1(lines: List[str]):
    precedence = {
        "*": 1,
        "+": 1,
    }
    return sum(evaluate(line, precedence) for line in lines)


def part2(lines: List[str]):
    precedence = {
        "*": 1,
        "+": 2,
    }
    return sum(evaluate(line, precedence) for line in lines)
