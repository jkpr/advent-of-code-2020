from collections import Counter
import re
from typing import List


def parse_input(lines: List[str]):
    lookup = {}
    all_ingredients = Counter()
    for line in lines:
        ingredients_string, allergens_string = line.split("(contains")
        ingredients = set(re.findall(r"\w+", ingredients_string))
        allergens = re.findall(r"\w+", allergens_string)
        for allergen in allergens:
            if allergen in lookup:
                lookup[allergen] = lookup[allergen] & ingredients
            else:
                lookup[allergen] = ingredients
        all_ingredients += Counter(ingredients)
    return lookup, all_ingredients


def part1(lines: List[str]):
    lookup, all_ingredients = parse_input(lines)
    possible_ingredients = set.union(*lookup.values())
    return sum(v for k, v in all_ingredients.items() if k not in possible_ingredients)


def part2(lines: List[str]):
    lookup, _ = parse_input(lines)
    solved = {}
    while lookup:
        to_delete = set()
        for allergen, ingredients in lookup.items():
            if len(ingredients) == 1:
                ingredient = ingredients.pop()
                to_delete.add(ingredient)
                solved[allergen] = ingredient
        for ingredient in to_delete:
            for ingredients in lookup.values():
                ingredients.discard(ingredient)
        lookup = {k: v for k, v in lookup.items() if len(v) > 0}
    result = sorted(solved.items())
    return ",".join(v for k, v in result)
