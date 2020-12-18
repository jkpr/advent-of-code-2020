import ast
from typing import List


class SubToMult(ast.NodeTransformer):
    def visit_Sub(self, node):
        return ast.Mult()


class MultToAdd(ast.NodeTransformer):
    def visit_Mult(self, node):
        return ast.Add()


def part1(lines: List[str]):
    result = []
    for line in lines:
        tree = ast.parse(f"this_result = {line.replace('*', '-')}")
        SubToMult().visit(tree)
        code = compile(tree, filename="<ast>", mode="exec")
        exec(code, globals())
        result.append(this_result)
    return sum(result)


def part2(lines: List[str]):
    result = []
    for line in lines:
        tree = ast.parse(f"this_result = {line.replace('*', '-').replace('+', '*')}")
        MultToAdd().visit(tree)
        SubToMult().visit(tree)
        code = compile(tree, filename="<ast>", mode="exec")
        exec(code, globals())
        result.append(this_result)
    return sum(result)
