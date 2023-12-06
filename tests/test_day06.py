from advent_of_code_2023.day06 import solve_part1, solve_part2

example1 = """Time:      7  15   30
Distance:  9  40  200"""


def test_part1():
    assert solve_part1(example1) == 288


def test_part2():
    assert solve_part2(example1) == 71503
