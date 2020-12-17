from typing import List

import numpy as np
from scipy.ndimage import convolve


def cycle(lines: List[str], times: int, dim: int):
    """Initialize a Conway cube and then cycle it."""
    plane = np.array([[c == "#" for c in line] for line in lines])
    cube = np.expand_dims(plane, axis=tuple(range(dim - 2)))
    n_mask = np.ones(shape=(3,) * dim)
    n_mask[(1,) * dim] = 0
    for _ in range(times):
        cube = np.pad(cube, 1).astype(int)
        n_count = convolve(cube, n_mask, mode="constant", cval=0)
        cube = (cube == 1) & ((n_count == 2) | (n_count == 3)) | (cube == 0) & (
            n_count == 3
        )
    return np.sum(cube)


def part1(lines: List[str]):
    return cycle(lines, 6, 3)


def part2(lines: List[str]):
    return cycle(lines, 6, 4)
