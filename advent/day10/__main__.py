from ..utils import common_main

# from . import part1, part2
from .alternate import part1, part2


common_main(module_path=__file__, input_to_int=True, part1=part1, part2=part2)
