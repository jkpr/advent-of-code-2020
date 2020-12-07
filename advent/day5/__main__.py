from ..utils import common_main
from . import part1, part2


if __name__ == "__main__":
    common_main(module_path=__file__, input_to_int=False, part1=part1, part2=part2)
