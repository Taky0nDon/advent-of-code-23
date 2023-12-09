with open("test.txt") as file:
    cards = file.readlines()


def get_card_numbers(card):
    return card.split(":")[1]


def get_winning_numbers(card_numbers):
    return card_numbers.split("|")[0].strip().replace("  ", " ")


def get_your_numbers(card_numbers):
    return card_numbers.split("|")[1].strip().replace("  ", " ")


def get_matches(winning_numbers, numbers_you_have):
    matches = 0
    winning_numbers = [int(n) for n in winning_numbers.split(" ")]
    yours = [int(n) for n in numbers_you_have.split(" ")]
    print(sorted(winning_numbers))
    print(sorted(yours))
    for number in yours:
        for wnumber in winning_numbers:
            if number == wnumber:
                matches += 1

    print(f"{matches=}")
    return matches


def get_points(matches):
    return 0 if not matches else 2 ** (matches - 1)


def main():
    points_lst = []
    result = 0
    i = 0
    for card in cards:
        print(f"{i=}")
        numbers = get_card_numbers(card)
        print(numbers)
        winning = get_winning_numbers(numbers)

        yours = get_your_numbers(numbers)
        matches = get_matches(winning, yours)
        card_points = get_points(matches)
        result += card_points
        points_lst.append(card_points)
        print(card_points)
        i += 1
    return sum(points_lst)


if __name__ == "__main__":
    print(main())
