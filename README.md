# Advent of Code 2020

These are my solutions to Advent of Code 2020.

Try the problems yourself at [https://adventofcode.com/2020/](https://adventofcode.com/2020/).

# Day 1

This is a warm up challenge. Python's standard library comes to the rescue with the [`itertools` library and `combinations` function][1a].

[1a]: https://docs.python.org/3/library/itertools.html#itertools.combinations

# Day 2

Since the lines were all in the same format, a regular expression came to mind. In terms of counting the number of occurrences of a letter, the [`collections.Counter` class][2a] has that functionality built in.

At this point, Python's `itertools` and `collections` modules have been useful, as they often are in programming challenges.

[2a]: https://docs.python.org/3/library/collections.html#collections.Counter

# Day 3

The main thing to realize is that since the forest is repeating along the x-axis, we can use module arithmetic on the position of the x-axis index.
