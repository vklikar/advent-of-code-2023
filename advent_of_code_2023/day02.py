import re
from math import prod


def parse(data):
    parsed_data = {}
    for line in data.splitlines():
        game, *sets = re.split(r"[:;]", line)
        game_number = int(game.lstrip("Game "))
        parsed_sets = []
        for revealed_set in sets:
            parsed_set = {}
            for draw in revealed_set.split(","):
                number, color = draw.strip().split()
                number = int(number)
                parsed_set[color] = number
            parsed_sets.append(parsed_set)
        parsed_data[game_number] = parsed_sets
    return parsed_data


def solve_part1(data):
    LIMITS = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    parsed_data = parse(data)

    ans = 0
    for game_number, parsed_sets in parsed_data.items():
        if all(number <= LIMITS[color] for parsed_set in parsed_sets for color, number in parsed_set.items()):
            ans += game_number

    return ans


def solve_part2(data):
    parsed_data = parse(data)

    ans = 0
    for game_number, parsed_sets in parsed_data.items():
        min_values = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for parsed_set in parsed_sets:
            for color, number in parsed_set.items():
                min_values[color] = max(min_values[color], number)
        ans += prod(min_values.values())

    return ans
