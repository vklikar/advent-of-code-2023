from advent_of_code_2023.day01 import solve_part1, solve_part2

example1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


example2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def test_part1():
    assert solve_part1(example1) == 142


def test_part2():
    assert solve_part2(example2) == 281
