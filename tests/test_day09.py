from advent_of_code_2023.day09 import solve_part1, solve_part2

example1 = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def test_part1():
    assert solve_part1(example1) == 114


def test_part2():
    assert solve_part2(example1) == 2
