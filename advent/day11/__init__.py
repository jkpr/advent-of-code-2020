from collections import Counter, defaultdict
from typing import List


def get_neighbors1(max_x, max_y):
    result = defaultdict(list)
    directions = (
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (-1, -1),
    )
    for i in range(max_x * max_y):
        x, y = idx_to_xy(i, max_x, max_y)
        for d_x, d_y in directions:
            new_x = x + d_x
            new_y = y + d_y
            if 0 <= new_x < max_x and 0 <= new_y < max_y:
                result[i].append(xy_to_idx(new_x, new_y, max_x, max_y))
    return result


def part1(lines: List[str]):
    max_x = len(lines)
    max_y = len(lines[0])
    seats = []
    for line in lines:
        seats.extend(line)
    neighbors_idx = get_neighbors1(max_x, max_y)
    next_gen = []
    while True:
        print_seats(seats, max_x, max_y)
        for i, item in enumerate(seats):
            if item == ".":
                next_gen.append(".")
            else:
                neighbors = [seats[j] for j in neighbors_idx[i]]
                counter = Counter(neighbors)
                if item == "L" and counter["#"] == 0:
                    next_gen.append("#")
                elif item == "#" and counter["#"] >= 4:
                    next_gen.append("L")
                else:
                    next_gen.append(item)
        if seats == next_gen:
            break
        seats = next_gen
        next_gen = []
    return Counter(next_gen)["#"]


# --- # --- # --- # --- # --- # --- # --- # ---
# COMMON CODE BETWEEN THE PARTS
# --- # --- # --- # --- # --- # --- # --- # ---


def idx_to_xy(idx, max_x, max_y):
    return divmod(idx, max_y)


def xy_to_idx(x, y, max_x, max_y):
    return x * max_y + y


def print_seats(seats, max_x, max_y):
    for i, item in enumerate(seats):
        print(item, end="")
        if (i + 1) % max_y == 0 and i != 0:
            print()
    print("===")


# --- # --- # --- # --- # --- # --- # --- # ---
# PART 2 BELOW
# --- # --- # --- # --- # --- # --- # --- # ---


def get_views(max_x, max_y):
    result = defaultdict(list)
    directions = (
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (-1, -1),
    )
    for i in range(max_x * max_y):
        x, y = idx_to_xy(i, max_x, max_y)
        for d_x, d_y in directions:
            this_direction = []
            next_xy = x + d_x, y + d_y
            while 0 <= next_xy[0] < max_x and 0 <= next_xy[1] < max_y:
                this_direction.append(xy_to_idx(next_xy[0], next_xy[1], max_x, max_y))
                next_xy = next_xy[0] + d_x, next_xy[1] + d_y
            if this_direction:
                result[i].append(this_direction)
    return result


def get_neighbors2(seats, max_x, max_y):
    result = defaultdict(list)
    views = get_views(max_x, max_y)
    for i, item in enumerate(seats):
        if item in ("#", "L"):
            lines_of_sight = views[i]
            for line in lines_of_sight:
                for idx in line:
                    if seats[idx] in ("#", "L"):
                        result[i].append(idx)
                        break
    return result


def part2(lines: List[str]):
    max_x = len(lines)
    max_y = len(lines[0])
    seats = []
    for line in lines:
        seats.extend(line)
    neighbors_idx = get_neighbors2(seats, max_x, max_y)
    next_gen = []
    while True:
        print_seats(seats, max_x, max_y)
        for i, item in enumerate(seats):
            if item == ".":
                next_gen.append(".")
            else:
                neighbors = [seats[j] for j in neighbors_idx[i]]
                counter = Counter(neighbors)
                if item == "L" and counter["#"] == 0:
                    next_gen.append("#")
                elif item == "#" and counter["#"] >= 5:
                    next_gen.append("L")
                else:
                    next_gen.append(item)
        if seats == next_gen:
            break
        seats = next_gen
        next_gen = []
    return Counter(next_gen)["#"]
