import re
from typing import List


def part1(lines: List[str]):
    heading = 0
    x, y = 0, 0
    for line in lines:
        command = line[0]
        value = int(line[1:])
        if command == "N":
            y += value
        elif command == "S":
            y -= value
        elif command == "E":
            x += value
        elif command == "W":
            x -= value
        elif command == "L":
            heading += value
            heading %= 360
        elif command == "R":
            heading -= value
            heading %= 360
        elif command == "F":
            if heading == 0:
                x += value
            elif heading == 90:
                y += value
            elif heading == 180:
                x -= value
            elif heading == 270:
                y -= value
            else:
                raise ValueError(line)
        else:
            raise ValueError(line)
    return abs(x) + abs(y)


def part2(lines: List[str]):
    x, y = 0, 0
    wx, wy = 10, 1
    for line in lines:
        command = line[0]
        value = int(line[1:])
        if command == "N":
            wy += value
        elif command == "S":
            wy -= value
        elif command == "E":
            wx += value
        elif command == "W":
            wx -= value
        elif command == "L":
            if value == 90:
                wx, wy = -wy, wx
            elif value == 180:
                wx, wy = -wx, -wy
            elif value == 270:
                wx, wy = wy, -wx
            else:
                raise ValueError(line)
        elif command == "R":
            if value == 90:
                wx, wy = wy, -wx
            elif value == 180:
                wx, wy = -wx, -wy
            elif value == 270:
                wx, wy = -wy, wx
            else:
                raise ValueError(line)
        elif command == "F":
            x += wx * value
            y += wy * value
        else:
            raise ValueError(line)
    return abs(x) + abs(y)
