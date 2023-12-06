from advent_of_code_2023.day03 import solve_part1, solve_part2

example1 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_part1():
    assert solve_part1(example1) == 4361


def test_part2():
    assert solve_part2(example1) == 467835
