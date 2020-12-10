import re
from typing import List


def part1(lines: List[str]):
    # `data` is a list of tuples:
    # index-0 for the parent bag color
    # index-1 for the set of children bag colors
    # I am not paying attention to the numbers in this part
    data = []
    for line in lines:
        # All bags are described by two words, such as "shiny gold"
        found = re.findall(r"(\w+ \w+) bag", line)
        if found[1] == "no other":
            # This is for terminating lines such as "dark violet bags contain no other bags."
            data.append((found[0], set()))
        else:
            data.append((found[0], set(found[1:])))
    bags = set()
    current_set = {"shiny gold"}
    while current_set:
        this_set = set()
        for item in data:
            # If a rule has a current bag as a child bag...
            if current_set & item[1]:
                # ... add the parent to search later
                this_set.add(item[0])
        # Search the new bags that are not already found
        current_set = this_set - bags
        bags |= this_set
    print(len(bags))


def part2(lines: List[str]):
    # `data` is a list of tuples:
    # index-0 for the parent bag color
    # index-1 for a list of tuples: the number and the bag color of children
    data = []
    for line in lines:
        found = re.findall(r"(\d+ )?(\w+ \w+) bag", line)
        color = found[0][1]
        if found[1][1] != "no other":
            sub_colors = []
            for i in found[1:]:
                sub_colors.append([int(i[0]), i[1]])
            data.append((color, sub_colors))
        else:
            data.append((color, []))
    data_dict = dict(data)
    print(get_size(data_dict, "shiny gold") - 1)


def get_size(data_dict: dict, color: str):
    """Get the size of a bag of a specific color.

    A recursive function. The size of "this bag" is the
    size of all its sub-bags + 1 (the +1 is to account
    for "this bag").
    """
    counts = []
    for count, sub_color in data_dict[color]:
        this_color_size = count * get_size(data_dict, sub_color)
        counts.append(this_color_size)
    size = 1 if not counts else sum(counts) + 1
    return size
