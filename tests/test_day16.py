from advent_of_code_2023.day16 import solve_part1, solve_part2

example1 = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""


def test_part1():
    assert solve_part1(example1) == 46


def test_part2():
    assert solve_part2(example1) == 51
