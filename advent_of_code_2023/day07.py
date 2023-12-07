from collections import Counter
from enum import IntEnum, auto


def parse_data(data):
    lines = [line.split() for line in data.splitlines()]
    return [(hand, int(bid)) for hand, bid in lines]


class HandType(IntEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    FIVE_OF_A_KIND = auto()


def get_hand_type(hand):
    counter = Counter(hand)
    if len(counter) == 1:
        return HandType.FIVE_OF_A_KIND
    if counter.most_common()[0][1] == 4:
        return HandType.FOUR_OF_A_KIND
    if len(counter) == 2:
        return HandType.FULL_HOUSE
    if counter.most_common()[0][1] == 3:
        return HandType.THREE_OF_A_KIND
    if len(counter) == 3:
        return HandType.TWO_PAIR
    if counter.most_common()[0][1] == 2:
        return HandType.ONE_PAIR

    return HandType.HIGH_CARD


def get_joker_hand_type(hand):
    hand_type = get_hand_type(hand)
    jokers_count = hand.count("J")
    joker_hand_type = {
        1: {
            HandType.FOUR_OF_A_KIND: HandType.FIVE_OF_A_KIND,
            HandType.THREE_OF_A_KIND: HandType.FOUR_OF_A_KIND,
            HandType.TWO_PAIR: HandType.FULL_HOUSE,
            HandType.ONE_PAIR: HandType.THREE_OF_A_KIND,
            HandType.HIGH_CARD: HandType.ONE_PAIR,
        },
        2: {
            HandType.FULL_HOUSE: HandType.FIVE_OF_A_KIND,
            HandType.TWO_PAIR: HandType.FOUR_OF_A_KIND,
            HandType.ONE_PAIR: HandType.THREE_OF_A_KIND,
        },
        3: {
            HandType.FULL_HOUSE: HandType.FIVE_OF_A_KIND,
            HandType.THREE_OF_A_KIND: HandType.FOUR_OF_A_KIND,
        },
        4: {
            HandType.FOUR_OF_A_KIND: HandType.FIVE_OF_A_KIND,
        },
    }

    return joker_hand_type[jokers_count][hand_type] if 0 < jokers_count < 5 else hand_type


def get_cards_strength(hand):
    return tuple("23456789TJQKA".index(card) for card in hand)


def get_joker_cards_strength(hand):
    return tuple("J23456789TQKA".index(card) for card in hand)


def solve_part1(data):
    parsed_data = parse_data(data)
    sorted_hands = sorted(parsed_data, key=lambda x: (get_hand_type(x[0]), get_cards_strength(x[0])))
    return sum(rank * bid for rank, (_, bid) in enumerate(sorted_hands, 1))


def solve_part2(data):
    parsed_data = parse_data(data)
    sorted_hands = sorted(parsed_data, key=lambda x: (get_joker_hand_type(x[0]), get_joker_cards_strength(x[0])))
    return sum(rank * bid for rank, (_, bid) in enumerate(sorted_hands, 1))
