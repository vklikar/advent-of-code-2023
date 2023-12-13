from advent_of_code_2023.day13 import solve_part1, solve_part2

example1 = """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def test_part1():
    assert solve_part1(example1) == 405


def test_part2():
    assert solve_part2(example1) == 400
