from collections import deque
from typing import List


def initialize(lines):
    chunks = "\n".join(lines).split("\n\n")
    deck1 = deque(int(i) for i in chunks[0].split("\n")[1:])
    deck2 = deque(int(i) for i in chunks[1].split("\n")[1:])
    return deck1, deck2


def play_to_end(deck1, deck2):
    while deck1 and deck2:
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
    return deck1, deck2


def recursive_play_to_end(deck1, deck2):
    seen = set()
    while deck1 and deck2:
        if (state := (tuple(deck1), tuple(deck2))) in seen:
            deck2.clear()
            return deck1, deck2
        seen.add(state)
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if len(deck1) >= card1 and len(deck2) >= card2:
            new_deck1 = deque(deck1)
            while len(new_deck1) > card1:
                new_deck1.pop()
            new_deck2 = deque(deck2)
            while len(new_deck2) > card2:
                new_deck2.pop()
            recursive_play_to_end(new_deck1, new_deck2)
            if new_deck1:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
        else:
            if card1 > card2:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
    return deck1, deck2


def part1(lines: List[str]):
    deck1, deck2 = play_to_end(*initialize(lines))
    winner = deck1 if deck1 else deck2
    return sum(i * card for i, card in enumerate(reversed(winner), start=1))


def part2(lines: List[str]):
    deck1, deck2 = recursive_play_to_end(*initialize(lines))
    winner = deck1 if deck1 else deck2
    return sum(i * card for i, card in enumerate(reversed(winner), start=1))
