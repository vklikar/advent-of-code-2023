def parse_data(data):
    parsed_data = []
    for line in data.splitlines():
        card, numbers = line.split(":")
        card_number = int(card.removeprefix("Card "))
        winning_numbers, my_numbers = numbers.split("|")
        winning_numbers = {int(x) for x in winning_numbers.split()}
        my_numbers = [int(x) for x in my_numbers.split()]
        parsed_data.append((card_number, winning_numbers, my_numbers))
    return parsed_data


def solve_part1(data):
    parsed_data = parse_data(data)

    ans = 0
    for card_number, winning_numbers, my_numbers in parsed_data:
        matches = sum(1 for x in my_numbers if x in winning_numbers)
        if matches:
            ans += 2 ** (matches - 1)

    return ans


def solve_part2(data):
    parsed_data = parse_data(data)

    dp = [1] * len(parsed_data)

    for card_number, winning_numbers, my_numbers in parsed_data:
        matches = sum(1 for x in my_numbers if x in winning_numbers)
        if matches:
            for i in range(card_number, min(len(dp), card_number + matches)):
                dp[i] += dp[card_number - 1]

    return sum(dp)
