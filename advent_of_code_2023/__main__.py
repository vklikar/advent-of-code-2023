from pathlib import Path

from advent_of_code_2023 import day01, day02, day03, day04, day05, day06


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


if __name__ == "__main__":
    main()
