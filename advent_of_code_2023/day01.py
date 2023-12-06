DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

REVERSED_DIGITS = {k[::-1]: v for k, v in DIGITS.items()}

WINDOW_SIZE = max(len(k) for k in DIGITS)


def parse_data(data):
    return data.splitlines()


def find_digit(s) -> str:
    return next(c for c in s if c.isdigit())


def find_digit_or_word(s, is_reversed=False):
    digits = REVERSED_DIGITS if is_reversed else DIGITS
    for i in range(len(s)):
        window = s[i : i + WINDOW_SIZE]
        if window[0].isdigit():
            return window[0]
        for digit in digits:
            if window.startswith(digit):
                return digits[digit]


def solve_part1(data):
    parsed_data = parse_data(data)
    return sum(int(find_digit(x) + find_digit(x[::-1])) for x in parsed_data)


def solve_part2(data):
    parsed_data = parse_data(data)
    return sum(int(find_digit_or_word(x) + find_digit_or_word(x[::-1], is_reversed=True)) for x in parsed_data)
