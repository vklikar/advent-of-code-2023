import re
from functools import cache


def parse_data(data):
    parsed_data = []
    for line in data.splitlines():
        springs, groups_part = line.split()
        group_sizes = [int(x) for x in groups_part.split(",")]
        parsed_data.append((springs, group_sizes))
    return parsed_data


@cache
def brute_force(springs, i):
    # TODO: needs to be replaced as it is very slow
    if i == len(springs):
        return [""]

    j = springs[i:].find("?")
    if j == -1:
        return [springs[i:]]

    head = springs[i : i + j]
    tail = brute_force(springs, i + j + 1)
    return [head + "." + s for s in tail] + [head + "#" + s for s in tail]


def make_groups(springs):
    return re.split(r"\.+", springs.strip("."))


def solve_part1(data):
    parsed_data = parse_data(data)
    ans = 0
    for springs, group_sizes in parsed_data:
        arrangements = brute_force(springs, 0)
        ans += sum(
            1 for arrangement in arrangements if [len(group) for group in make_groups(arrangement)] == group_sizes
        )
    return ans


def solve_part2(data):
    pass
