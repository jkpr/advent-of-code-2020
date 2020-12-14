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

- `-t` to run part 1 with `test_input.txt`
- `-2` to run part 2
- `-t -2` to run part 2 with `test_input.txt`
- `-t 1` to run part 1 with `test_input1.txt`
- `-t 1 -2` to run part 2  with `test_input1.txt`

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

# Day 10

Part 1 is fairly easy. I made use of `zip` with offset (by 1) lists to get the differences. 

Part 2 was more complicated. In the supplied list of transformers, my breakthrough came when I noticed there were jumps of 1 and 3 only. There are no jumps of 2.

Transformers on both sides of a jump of three have to stay because that is the largest jump allowed, so really I was looking at how to remove transformers that have jumps of 1 from one to the next.

I also noticed that the largest run of jumps of size 1 that I had was 4.

After Googling, I learned
- The number of ways to use 1 and 2 to add up to a number N is the (N+1)-th Fibonacci number
- The number of ways to use 1, 2 and 3 to add up to a number N is the (N+1)-th Tribonacci number.

The [Tribonacci sequence][10a] is 1, 1, 2, 4, 7, 13, 24, 44, 81, ...

So my solution is to identify the number of runs of steps of 1, how long they were, then find the corresponding "Tribonacci number" (I did by hand without knowing the name of the sequence).
Then multiply all those numbers together.

Also: [`itertools.groupby`][10b] came in handy for identifying runs of numbers.
It automatically creates new groups when the value changes, going one item to the next.

[10a]: https://mathworld.wolfram.com/Fibonaccin-StepNumber.html
[10b]: https://docs.python.org/3/library/itertools.html#itertools.groupby

# Day 11

With maze searching, it is easier to list out all the directions as offsets to search rather than name the directions, i.e.

```python
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
```

is better than 

```python
def move_up(...):
    ...

def move_up_right(...):
    ...

... # etc.
```

Also for mazes, I find that working with a single array and doing calculations between index and `(x, y)` is better than maintaining a 2-D array.
These companion functions are helpful. Of course, results can be cached to get even faster, too!

```python
def idx_to_xy(idx, max_x, max_y):
    return divmod(idx, max_y)

def xy_to_idx(x, y, max_x, max_y):
    return x * max_y + y
```

It is easier for me to think in terms of `(x, y)` rather than `row, col`.
In my manner of speaking, I say `row, col` which corresponds to `(y, x)`, so it is opposite to `(x, y)`.
But I almost always think in terms of `(x, y)` and `(x, y)` usually makes more sense for 2-D arrays.

Final thing to say: the neighbors to check in each part do not change from generation to generation.
I decided to cache the neighbors lookup ahead of time with `get_neighbors1` and `get_neighbors2`.
It is much better than calculating them on each pass through.

# Day 12

Fairly straightforward problem. Not too many tricks to share today.
One thing to share is that with Python we can update two values at once.
For example:

```python
# Set x and y at the same time:
x, y = 0, 0

# Perform 180 degree rotation for the problem:
wx, wy = -wx, -wy
```

This makes use of iterable unpacking from tuples.

# Day 13

Part 1 was accomplished by checking and seeing case by case. 

With such a small input file, I could see I had a bus number of 13 (my smallest). So, I would not need to look more than 13 above the start time.

Part 2 was harder. My original solution did not use the Chinese Remainder Theorem. First thing I noticed was that my bus numbers were all prime. I also noticed that a lot of buses would be arriving at the same time. So for that to happen, it had to be a multiple of the product of all of those buses. I did a "brute force" search on that multiple. 

But the Chinese Remainder Theorem was definitely the way to go to immediately calculate an answer.

Calculate the product of an iterable of numbers with [math.prod][13a]:

```python
import math

nums = [3, 5, 6]
result = math.prod(nums)  # 90
```

Also there is a difference between `/` and `//`:

```python
>>> 10 / 2
5.0
>>> 10 // 2
5
```

The first (`/`) is float division and the second (`//`) is integer division.

[13a]: https://docs.python.org/3/library/math.html#math.prod

# Day 14

My previous notes on converting between base 10 and base 2 were helpful here!

A number saved as a string, e.g. `"42"`, can be padded with zeros using `.zfill(width)`. See [`zfill` documentation][14a].

```python
>>> "42".zfill(5)
"00042"
```

The cartesian product also came in handy for the second part to fill in the `X` values in the memory mask. See documentation for [`itertools.product`][14b].

```python
>>> list(itertools.product([0, 1], repeat=3))
(0, 0, 0)
(0, 0, 1)
(0, 1, 0)
...
(1, 1, 1)
```

[14a]: https://docs.python.org/3/library/stdtypes.html#str.zfill
[14b]: https://docs.python.org/3/library/itertools.html#itertools.product
