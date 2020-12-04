from pkg_resources import require

from aoc2020.util import get_input_day04


def valid_byr(byr):
    if byr == None:
        return False
    return 1920 <= int(byr) <= 2002


def valid_iyr(iyr):
    if iyr == None:
        return False
    return 2010 <= int(iyr) <= 2020


def valid_eyr(eyr):
    if eyr == None:
        return False
    return 2020 <= int(eyr) <= 2030


def valid_hgt(hgt):
    if hgt == None:
        return False
    unit = hgt[-2:]
    height = hgt[:-2]
    if unit == "cm":
        return 150 <= int(height) <= 193
    elif unit == "in":
        return 59 <= int(height) <= 76
    return False


def valid_hcl(hcl):
    if hcl == None:
        return False
    if hcl[0] != "#":
        return False
    if len(hcl[1:]) != 6:
        return False
    try:
        int(hcl[1:], base=16)
    except ValueError:
        return False
    return True


def valid_ecl(ecl):
    if ecl == None:
        return False
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    return True


def valid_pid(pid):
    if pid == None:
        return False
    return len(pid) == 9


def valid_cid(cid):
    return True


REQUIRED = {
    "byr": valid_byr,
    "iyr": valid_iyr,
    "eyr": valid_eyr,
    "hgt": valid_hgt,
    "hcl": valid_hcl,
    "ecl": valid_ecl,
    "pid": valid_pid,
    #    "cid": valid_cid,
}


def solve_part1(entries):
    required_keys = list(REQUIRED.keys())
    required_keys.sort()
    # we don't care about cid and since we sort the
    # required keys down below to compare it needs
    # to be removed
    # required_keys.remove("cid")
    valid = 0
    for passport in entries:
        passport = passport.split(" ")
        keys = []
        for field in passport:
            k, v = field.split(":")
            if k != "cid":
                keys.append(k)
        keys.sort()
        if keys == required_keys:
            valid += 1
    return valid


def solve_part2(entries):
    required_keys = list(REQUIRED.keys())
    required_keys.sort()
    valid = 0
    for passport in entries:
        is_valid = True
        passport = passport.split(" ")
        fields = dict(field.split(":") for field in passport)
        # remove cid if it exists
        fields.pop("cid", None)
        if len(fields.keys()) != 7:
            is_valid = False
        if is_valid:
            for k, v in fields.items():
                # call the validator function for the field
                if k != "cid" and not REQUIRED[k](v):
                    is_valid = False
                    break
        if is_valid:
            valid += 1
    return valid


if __name__ == "__main__":  # pragma: no cover
    entries = get_input_day04("aoc2020/day04/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
