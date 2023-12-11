from advent_of_code_2023.day10 import solve_part1, solve_part2

example1 = """\
.....
.S-7.
.|.|.
.L-J.
....."""

example2 = """\
..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

example3 = """\
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

example4 = """\
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

example5 = """\
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

no_edge_dots1 = """\
S-7
|.|
L-J"""

no_edge_dots2 = """\
F--------7
|.S----7.|
|.|....|.|
|.L-7F-J.|
|...||...|
L---JL---J"""

edge_dots = """\
............
.F--------7.
.|.S----7.|.
.|.|....|.|.
.|.L-7F-J.|.
.|...||...|.
.L---JL---J.
............"""

vertical_pipe_start = """\
.....
.F-7.
.S.|.
.L-J.
....."""

horizontal_pipe_start = """\
.....
.F-7.
.|.|.
.LSJ.
....."""


def test_part1_ex1():
    assert solve_part1(example1) == 4


def test_part1_ex2():
    assert solve_part1(example2) == 8


def test_part2_ex3():
    assert solve_part2(example3) == 4


def test_part2_ex4():
    assert solve_part2(example4) == 8


def test_part2_ex5():
    assert solve_part2(example5) == 10


def test_part2_no_edge_dots1():
    assert solve_part2(no_edge_dots1) == 1


def test_part2_no_edge_dots2():
    assert solve_part2(no_edge_dots2) == 12


def test_part2_edge_dots():
    assert solve_part2(edge_dots) == 12


def test_part2_vertical_pipe_start():
    assert solve_part2(vertical_pipe_start) == 1


def test_part2_horizontal_pipe_start():
    assert solve_part2(horizontal_pipe_start) == 1
