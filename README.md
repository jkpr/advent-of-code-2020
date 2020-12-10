# Advent of Code 2020

These are my solutions to Advent of Code 2020.

Try the problems yourself at [https://adventofcode.com/2020/](https://adventofcode.com/2020/).

Feel free to create a Github issue if you want to discuss anything!

# Usage

1. Clone this repo: `git clone https://github.com/jkpr/advent-of-code-2020`
2. Change into the new directory: `cd advent-of-code-2020`
3. Run `make env` to build the environment.
4. Activate the environment with `source env/bin/activate`
5. Run a CLI for day `N`'s code with `python3 -m advent.dayN`, e.g. `python3 -m advent.day1`.

The CLI is common for each day. The main patterns for options are:

- `-t` to run the code with `test_input.txt`
- `-2` to run part 2
- `-t -2` to run part 2 with `test_input.txt`

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

# Day 5

The trick is to realize this is really just binary! I created a string representing a binary number, e.g. 

1. `"BFFFBBFRRR"`
2. `"BFFFBBF"` and `"RRR"`
3. `"1000110"` and `"111"`

Then I used `int(binary_string, base=2)` to convert to integer. The result is 70 and 7. By the way, the reverse operation is 

```python
>>> bin(70)
'0b1000110'
```

I do not have the most elegant solution for part 2, I'm sure. In order to see the gaps, I started with a set of all numbers from 0 to the maximum, then subtracted the set of all seat IDs. Then I printed out what remained as a sorted list and visually (manually) scanned for the correct answer.

# Day 6

Python has some built-in methods that make this one very easy! First of all, it becomes clear that we only need a set of letters per line to test for membership. Python treats a string as an iterable of the individual letters. For example:

```python
>>> set("asdf")
{'a', 's', 'd', 'f'}
```

For part 1, we just need the union of all sets in a group then to count the size. For part 2, we take the intersection, then count the size.

I googled how to take the interection of a collection of sets, and I [found this on StackOverflow][6a]. Basically it is:

```python
set.intersection(*list_of_sets)
```

I am astonished 😲 that this works! The StackOverflow response says:

> Note that `set.intersection` is not a static method, but this uses the functional notation to apply intersection of the first set with the rest of the list. So if the argument list is empty this will fail.

So apparently, that is equivalent to

```python
list_of_sets[0].intersection(*list_of_sets[1:])
```

Same works with `union`. Amazing.

I will need to research this one a little bit more.

[6a]: https://stackoverflow.com/a/2541814/6438168

# Day 7

First recursive algorithm. In trees, we often perform the same function on a node as on its descendents. That is what we did with `get_size` here.

# Day 8

Could this be the first steps to building a compiler? I made some premature optimizations to plan for more op-codes.

# Day 9

A few items of interest:

```python
for STATEMENT:
    ...
else:
    STATEMENT
```

If a `for` loop is not exited via a `break` key word, then an `else` block can be run after the `for` block completes.

Also, [`slice`][9a] objects are useful for getting windows into an array.

[9a]: https://docs.python.org/3/library/functions.html#slice
