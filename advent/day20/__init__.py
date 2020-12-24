import itertools
import math
import re
from typing import List


class Tile:
    """A puzzle Tile.

    Class properties:
        ORIENTATIONS: The exhaustive list of possible operations
            of flipping and rotating. In the form of (flip_int, rotate_int).

    Instance properties:
        key: This tile's key
        lines: The tile contents. In other words, the initial list
            of rows of the tile from the puzzle input.
        flipped: 0 for not flipped. 1 for flipped.
        rotated: The number of 90-degree clockwise rotations, between 0 and 3.
        possible_sides: All possible sides (for finding matching tiles)

    The lines of the tile are not modified after initialization. To get
    current state, flips and rotations are applied to the initial lines.
    """

    ORIENTATIONS = tuple(itertools.product(range(2), range(4)))

    def __init__(self, key: int, lines: List[str], flipped: int = 0, rotated: int = 0):
        self.key = key
        self.lines = list(lines)
        self.flipped = flipped
        self.rotated = rotated

        self.possible_sides = self.get_possible_sides()

    def orient_to_match(self, edge: str, which_side: int):
        """Orient this tile to match a neighbor's edge, if possible.

        We need to flip and rotate tiles to match neighbors.
        This method finds the right orientation so that the
        specified side of the tile matches the specified neighbor's
        edge.

        Sides are numbered 0-3,

        - 0 for top
        - 1 for right
        - 2 for bottom
        - 3 for left

        Params:
            edge: A string representing a neighbor's edge
            which_side: The side of this tile that should match that edge

        Returns:
            A copy of this tile, oriented such that the correct side
            matches the neighbor's edge.

        Raises:
            TypeError: If this tile does not match the supplied
                edge at all.
            ValueError: If this tile matches in more than one
                orientation to the supplied edge.
        """
        if edge not in self.possible_sides:
            raise TypeError()
        matches = []
        for orientation in self.ORIENTATIONS:
            orientated = self.apply_orientation(*orientation)
            possible = orientated.side(which_side)
            if edge == possible:
                matches.append(orientated)
        if not matches:
            # Should not happen
            raise TypeError()
        if len(matches) > 1:
            raise ValueError()
        return matches[0]

    def apply_orientation(self, flipped: int, rotated: int):
        """Apply the orientation on a copy of this tile.

        Returns:
            A new tile with supplied orientation."""
        return Tile(self.key, self.lines, flipped, rotated)

    @staticmethod
    def get_orientated_lines(lines: List[str], flipped: int, rotated: int) -> List[str]:
        """Apply an orientation to supplied content.

        This static method can be used for things other than
        tile contents.

        Returns:
            A new list of rows (strings).
        """
        new_lines = list(lines)
        if flipped:
            new_lines = [row[::-1] for row in new_lines]
        rotated = rotated % 4
        for _ in range(rotated):
            new_lines = ["".join(reversed(col)) for col in zip(*new_lines)]
        return new_lines

    @property
    def orientated_lines(self) -> List[str]:
        """Get this tile's rows with the orientation applied.

        Returns:
            A new list of tile rows (strings).
        """
        return self.get_orientated_lines(self.lines, self.flipped, self.rotated)

    def side(self, which: int) -> str:
        """Get the specified side from this Tile.

        Sides are numbered 0-3,

        - 0 for top
        - 1 for right
        - 2 for bottom
        - 3 for left

        Returns:
            A string representing for the edge.
        """
        which = which % 4
        if which == 0:
            return self.top
        elif which == 1:
            return self.right
        elif which == 2:
            return self.bottom
        else:
            return self.left

    def get_possible_sides(self) -> set:
        """Get all possible sides after flipping and rotating."""
        sides = set()
        for i in range(4):
            sides.add(self.side(i))
            sides.add(self.side(i)[::-1])
        return sides

    def edges_removed(self) -> List[str]:
        """Get these Tile contents with the outside edges removed."""
        lines = self.orientated_lines
        lines.pop(0)
        lines.pop(-1)
        lines = [line[1:-1] for line in lines]
        return lines

    @property
    def top(self) -> str:
        """Return the top edge of the tile."""
        lines = self.orientated_lines
        return lines[0]

    @property
    def bottom(self) -> str:
        """Return the bottom edge of the tile."""
        lines = self.orientated_lines
        return lines[-1]

    @property
    def left(self) -> str:
        """Return the left edge of the tile."""
        lines = self.orientated_lines
        return "".join((line[0] for line in lines))

    @property
    def right(self) -> str:
        """Return the right edge of the tile."""
        lines = self.orientated_lines
        return "".join((line[-1] for line in lines))

    def __str__(self):
        """Return the tile contents as a string."""
        lines = self.orientated_lines
        return "\n".join(lines)

    def __repr__(self):
        return f"<Tile {self.key} ({self.flipped}, {self.rotated})>"


def parse_to_tiles(lines: List[str]):
    """Parse the puzzle input to a dictionary of tiles."""
    chunks = "\n".join(lines).split("\n\n")
    tiles = {}
    for chunk in chunks:
        chunk_lines = chunk.split("\n")
        this_key = int(re.search(r"\d+", chunk_lines[0]).group(0))
        this_tile = chunk_lines[1:]
        tiles[this_key] = Tile(this_key, this_tile)
    return tiles


def get_corners(tiles):
    """Find the corner tiles."""
    for key, tile in tiles.items():
        edge_matches = []
        for other_key, other_tile in tiles.items():
            if key == other_key:
                continue
            if tile.get_possible_sides() & other_tile.get_possible_sides():
                edge_matches.append(other_tile)
        if len(edge_matches) == 2:
            yield tile


def part1(lines: List[str]):
    tiles = parse_to_tiles(lines)
    corners = get_corners(tiles)
    return math.prod(c.key for c in corners)


def get_top_left_corner(tiles):
    """Get the top-left corner."""
    corner = next(get_corners(tiles))
    matching_sides = []
    for tile in (t for t in tiles.values() if t.key != corner.key):
        for i in range(4):
            if corner.side(i) in tile.possible_sides:
                matching_sides.append(i)
    matching_sides.sort()
    for i in range(4):
        rotated = sorted([(x + i) % 4 for x in matching_sides])
        if rotated == [1, 2]:
            break
    top_left = corner.apply_orientation(0, i)
    return top_left


def orient_all_tiles(tiles):
    """Place all tiles on a canvas, oriented properly."""
    top_left = get_top_left_corner(tiles)
    remaining_tiles = set(tiles.keys())
    remaining_tiles.remove(top_left.key)
    top_row = [top_left]
    side_len = int(math.sqrt(len(tiles)))
    for _ in range(1, side_len):
        for key in remaining_tiles:
            try:
                left_neighbor = top_row[-1]
                orientated = tiles[key].orient_to_match(left_neighbor.right, 3)
                top_row.append(orientated)
                remaining_tiles.remove(key)
                break
            except TypeError:
                pass
    canvas = [top_row]
    for i in range(1, side_len):
        prev_row = canvas[i - 1]
        this_row = []
        for j in range(side_len):
            for key in remaining_tiles:
                try:
                    top_neighbor = prev_row[j]
                    orientated = tiles[key].orient_to_match(top_neighbor.bottom, 0)
                    this_row.append(orientated)
                    remaining_tiles.remove(key)
                    break
                except:
                    pass
        canvas.append(this_row)
    return canvas


def get_canvas_lines(canvas_tiles):
    """Convert a canvas of tiles to a list of lines."""
    canvas_lines = []
    for canvas_row in canvas_tiles:
        tiles = (tile.edges_removed() for tile in canvas_row)
        canvas_lines.extend(["".join(row) for row in zip(*tiles)])
    return canvas_lines


SEA_MONSTER = """\
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """


def get_monster_offsets(monster):
    """Get the (i, j) coords of the monster."""
    offsets = []
    for i, line in enumerate(monster.split("\n")):
        for j, ch in enumerate(line):
            if ch == "#":
                offsets.append((i, j))
    return tuple(offsets)


MONSTER_OFFSETS = get_monster_offsets(SEA_MONSTER)


def find_sea_monsters(canvas_lines):
    """Find the sea monster in the supplied canvas."""
    monsters = []
    height = len(canvas_lines)
    width = len(canvas_lines[0])
    for i in range(height):
        for j in range(width):
            points = tuple(((point[0] + i, point[1] + j) for point in MONSTER_OFFSETS))
            if all(
                0 <= k < height and 0 <= l < width and canvas_lines[k][l] == "#"
                for k, l in points
            ):
                monsters.append(points)
    return monsters


def part2(lines: List[str]):
    tiles = parse_to_tiles(lines)
    canvas_tiles = orient_all_tiles(tiles)
    canvas_lines = get_canvas_lines(canvas_tiles)
    for orientation in Tile.ORIENTATIONS:
        these_lines = Tile.get_orientated_lines(canvas_lines, *orientation)
        sea_monsters = find_sea_monsters(these_lines)
        if sea_monsters:
            break
    all_monster_points = set(itertools.chain(*sea_monsters))
    for i, line in enumerate(these_lines):
        for j, ch in enumerate(line):
            if (i, j) in all_monster_points:
                print("O", end="")
            else:
                print(ch, end="")
        print()
    all_hashes = sum(ch == "#" for ch in itertools.chain(*these_lines))
    return all_hashes - len(all_monster_points)
