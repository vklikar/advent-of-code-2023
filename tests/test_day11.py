from advent_of_code_2023.day11 import solve_part1, solve_part2

example1 = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def test_part1():
    assert solve_part1(example1) == 374


def test_part2():
    assert solve_part2(example1, multiplier=10) == 1030
    assert solve_part2(example1, multiplier=100) == 8410
