# Advent of Code 2020

These are my solutions to Advent of Code 2020.

Try the problems yourself at [https://adventofcode.com/2020/](https://adventofcode.com/2020/).

Feel free to create a Github issue if you want to discuss anything!

# Day 1

This is a warm up challenge. Python's standard library comes to the rescue with the [`itertools` library and `combinations` function][1a].

[1a]: https://docs.python.org/3/library/itertools.html#itertools.combinations

# Day 2

Since the lines were all in the same format, a regular expression came to mind. In terms of counting the number of occurrences of a letter, the [`collections.Counter` class][2a] has that functionality built in.

At this point, Python's `itertools` and `collections` modules have been useful, as they often are in programming challenges.

[2a]: https://docs.python.org/3/library/collections.html#collections.Counter

# Day 3

The main thing to realize is that since the forest is repeating along the x-axis, we can use module arithmetic on the position of the x-axis index.

# Day 4

Some useful things to note.

1. I went with the [`re` module][4a] because the text followed patterns seemingly perfectly.
2. There is a difference in Python between `re.search` (find regex anywhere in the string), `re.match` (find regex starting at the beginning of the string) and `re.fullmatch` (the regex must match the full string). I first did this with `re.match` and a regex like `\d{4}` could match something like `20202`. Of course, there are also the meta characters `^` and `$` to denote the start and end of a line.
3.  The `re` match object has a `.groups()` method which returns just the pieces that match the regex in parentheses `()`. There is also a `.group(n)` method that is similar. `.group(0)` returns the full match, then `1` up to `n` match the pieces matched in parentheses.

[4a]: https://docs.python.org/3/library/re.html
