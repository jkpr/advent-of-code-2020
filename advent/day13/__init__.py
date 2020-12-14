import math
from typing import List


def part1(lines: List[str]):
    time = int(lines[0])
    split = filter(lambda x: x != "x", lines[1].split(","))
    times = [int(x) for x in split]
    diff = 1_000_000
    for i in range(time, time + diff):
        for j in times:
            if i % j == 0:
                return (i - time) * j


def chinese_remainder(A: List[int], N: List[int]):
    """
    Given

    x === A1 (mod N1)
    x === A2 (mod N2)
    ...
    x === An (mod Nn)

    Args:
        n: List of moduluses
        a: List of residues / remainders

    https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
    """
    result = 0
    prod = math.prod(N)
    for a_i, n_i in zip(A, N):
        N_i = prod // n_i
        result += a_i * mul_inv(N_i, n_i) * N_i
    return result % prod


def mul_inv(a: int, n: int):
    """Find multiplicative inverse of a under n.

    Solve: ax === 1 (mod n)

    This assumes that gcd(a, n) == 1, i.e.
    that a and n are coprime.

    http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html
    """
    n0 = n
    x0, x1 = 0, 1
    if n == 1:
        return 1
    while a > 1:
        q = a // n
        a, n = n, a % n
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += n0
    return x1


def part2(lines: List[str]):
    split = lines[1].split(",")
    idx = []
    for i, num in enumerate(split):
        if num != "x":
            new_index = (-i) % int(num)
            idx.append([new_index, int(num)])
    A = [x[0] for x in idx]
    N = [x[1] for x in idx]
    return chinese_remainder(A, N)
