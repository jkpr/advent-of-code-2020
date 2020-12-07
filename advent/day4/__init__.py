from collections import Counter
import re
from typing import List


def part1(lines: List[str]):
    count = 0
    joined = "\n".join(lines)
    split = joined.split("\n\n")
    for passport in split:
        passport_split = passport.split()
        pp_dict = dict(
            re.fullmatch(r"(\w{3}):(\S+)", item).groups() for item in passport_split
        )
        size_valid = len(pp_dict) == 8
        optional_cid = len(pp_dict) == 7 and "cid" not in pp_dict
        if size_valid or optional_cid:
            count += 1
    print(count)


# --- --- # --- --- # --- --- # --- --- # --- ---
# The following is for part 2. It has some duplicate code from part 1
# --- --- # --- --- # --- --- # --- --- # --- ---


def get_passports(lines: List[str]):
    result = []
    joined = "\n".join(lines)
    split = joined.split("\n\n")
    for passport in split:
        passport_split = passport.split()
        pp_dict = dict(
            re.fullmatch(r"(\w{3}):(\S+)", item).groups() for item in passport_split
        )
        result.append(pp_dict)
    return result


def is_valid_pp(pp: dict):
    if len(pp) <= 6:
        return False
    if len(pp) == 7 and "cid" in pp:
        return False
    try:
        byr = int(re.fullmatch(r"\d{4}", pp["byr"]).group(0))
        if not 1920 <= byr <= 2002:
            return False
        iyr = int(re.fullmatch(r"\d{4}", pp["iyr"]).group(0))
        if not 2010 <= iyr <= 2020:
            return False
        eyr = int(re.fullmatch(r"\d{4}", pp["eyr"]).group(0))
        if not 2020 <= eyr <= 2030:
            return False
        hgt = re.fullmatch(r"(\d+)(cm|in)", pp["hgt"])
        if hgt.group(2) == "in" and not 59 <= int(hgt.group(1)) <= 76:
            return False
        if hgt.group(2) == "cm" and not 150 <= int(hgt.group(1)) <= 193:
            return False
    except AttributeError:
        return False
    hcl = re.fullmatch(r"#[0-9a-f]{6}", pp["hcl"])
    if not hcl:
        return False
    ecl = re.fullmatch(r"(amb|blu|brn|gry|grn|hzl|oth)", pp["ecl"])
    if not ecl:
        return False
    pid = re.fullmatch(r"\d{9}", pp["pid"])
    if not pid:
        return False
    return True


def part2(lines: List[int]):
    count = 0
    pp_list = get_passports(lines)
    for pp in pp_list:
        if is_valid_pp(pp):
            count += 1
    print(count)
