from pathlib import Path

from advent_of_code_2023 import (
    day01,
    day02,
    day03,
    day04,
    day05,
    day06,
    day07,
    day08,
    day09,
    day10,
    day11,
    day12,
    day13,
    day14,
    day15,
    day16,
    day17,
    day18,
    day19,
)


def read_input(filename):
    path = Path("inputs") / Path(filename)
    return path.read_text()


def main():
    print("01A:", day01.solve_part1(read_input("day01.txt")))
    print("01B:", day01.solve_part2(read_input("day01.txt")))
    print("02A:", day02.solve_part1(read_input("day02.txt")))
    print("02B:", day02.solve_part2(read_input("day02.txt")))
    print("03A:", day03.solve_part1(read_input("day03.txt")))
    print("03B:", day03.solve_part2(read_input("day03.txt")))
    print("04A:", day04.solve_part1(read_input("day04.txt")))
    print("04B:", day04.solve_part2(read_input("day04.txt")))
    print("05A:", day05.solve_part1(read_input("day05.txt")))
    print("05B:", day05.solve_part2(read_input("day05.txt")))
    print("06A:", day06.solve_part1(read_input("day06.txt")))
    print("06B:", day06.solve_part2(read_input("day06.txt")))
    print("07A:", day07.solve_part1(read_input("day07.txt")))
    print("07B:", day07.solve_part2(read_input("day07.txt")))
    print("08A:", day08.solve_part1(read_input("day08.txt")))
    print("08B:", day08.solve_part2(read_input("day08.txt")))
    print("09A:", day09.solve_part1(read_input("day09.txt")))
    print("09B:", day09.solve_part2(read_input("day09.txt")))
    print("10A:", day10.solve_part1(read_input("day10.txt")))
    print("10B:", day10.solve_part2(read_input("day10.txt")))
    print("11A:", day11.solve_part1(read_input("day11.txt")))
    print("11B:", day11.solve_part2(read_input("day11.txt")))
    print("12A:", day12.solve_part1(read_input("day12.txt")))
    print("12B:", day12.solve_part2(read_input("day12.txt")))
    print("13A:", day13.solve_part1(read_input("day13.txt")))
    print("13B:", day13.solve_part2(read_input("day13.txt")))
    print("14A:", day14.solve_part1(read_input("day14.txt")))
    print("14B:", day14.solve_part2(read_input("day14.txt")))
    print("15A:", day15.solve_part1(read_input("day15.txt")))
    print("15B:", day15.solve_part2(read_input("day15.txt")))
    print("16A:", day16.solve_part1(read_input("day16.txt")))
    print("16B:", day16.solve_part2(read_input("day16.txt")))
    print("17A:", day17.solve_part1(read_input("day17.txt")))
    print("17B:", day17.solve_part2(read_input("day17.txt")))
    print("18A:", day18.solve_part1(read_input("day18.txt")))
    print("18B:", day18.solve_part2(read_input("day18.txt")))
    print("19A:", day19.solve_part1(read_input("day19.txt")))
    print("19B:", day19.solve_part2(read_input("day19.txt")))


if __name__ == "__main__":
    main()
