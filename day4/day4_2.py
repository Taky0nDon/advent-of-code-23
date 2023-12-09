
with open("input.txt") as file:
    cards = file.readlines()


def get_card_ID(card):
    return card.split(":")[0].split(" ")[1]

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
    for number in yours:
        for wnumber in winning_numbers:
            if number == wnumber:
                matches += 1
    return matches


def get_points(matches):
    return 0 if not matches else 2 ** (matches - 1)


def play_game(stack):
    for card in stack:
        times = stack[card][0]
        for time in range(times):
            id = card
            current_card = stack[id][1]
            print(id)
            numbers = get_card_numbers(current_card)
            winning = get_winning_numbers(numbers)
            yours = get_your_numbers(numbers)
            matches = get_matches(winning, yours)
            won_copies = [n for n in range(id + 1, id + matches + 1)]
            for copy in won_copies:
                stack[copy] = stack[copy][0] + 1, stack[copy][1]
    return stack

stack_o_cards = {
        card:(count,orig_card) for card, count, orig_card in\
                zip([n for n in range(1, len(cards) + 1)],
                [1 for n in range(189)],
                    [card for card in cards])}
if __name__ == "__main__":
    result = 0
    final_stack = play_game(stack_o_cards)
    for value in final_stack.values():
        count = value[0]
        result += count
    print(result)
