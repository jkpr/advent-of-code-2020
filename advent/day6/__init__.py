from typing import List


def part1(lines: List[str]):
    count = 0
    parties = "\n".join(lines).split("\n\n")
    for party in parties:
        answers = party.split()
        party_sets = [set(answer) for answer in answers]
        count += len(set.union(*party_sets))
    print(count)


def part2(lines: List[str]):
    count = 0
    parties = "\n".join(lines).split("\n\n")
    for party in parties:
        answers = party.split()
        party_sets = [set(answer) for answer in answers]
        count += len(set.intersection(*party_sets))
    print(count)
