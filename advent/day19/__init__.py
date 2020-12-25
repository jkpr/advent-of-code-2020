from typing import List


def is_match(all_rules, message, pattern):
    if not message and not pattern:
        return True
    if message and not pattern:
        return False
    if pattern and not message:
        return False
    next_letter = message[0]
    next_sub_pattern = all_rules[pattern[0]].strip()
    if next_sub_pattern.startswith('"'):
        if next_letter != next_sub_pattern[1]:
            return False
        return is_match(all_rules, message[1:], pattern[1:])
    paths = []
    for item in next_sub_pattern.split("|"):
        result = is_match(all_rules, message, item.split() + pattern[1:])
        paths.append(result)
    return any(paths)


def parse_rule_zero(lines: List[str], for_part2: bool):
    chunks = "\n".join(lines).split("\n\n")
    all_rules = dict(line.split(":") for line in chunks[0].split("\n"))
    if for_part2:
        all_rules["8"] = "42 | 42 8"
        all_rules["11"] = "42 31 | 42 11 31"
    messages = chunks[1].split("\n")
    return sum(is_match(all_rules, message, ["0"]) for message in messages)


def part1(lines: List[str]):
    return parse_rule_zero(lines, for_part2=False)


def part2(lines: List[str]):
    return parse_rule_zero(lines, for_part2=True)
