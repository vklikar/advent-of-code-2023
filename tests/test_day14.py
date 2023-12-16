from advent_of_code_2023.day14 import solve_part1, solve_part2

example1 = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


def test_part1():
    assert solve_part1(example1) == 136


def test_part2():
    assert solve_part2(example1) == 64
