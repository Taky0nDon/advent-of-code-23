### THIS IS FOR TESTING ###
from importlib import reload
### THIS IS FOR TESTING ###
with open("input.txt") as file:
    puzzle_input = file.readlines()[1:]

class Bag:
    red = 12
    green = 13
    blue = 14
    total_cubes = red + green + blue

class Game():
    def __init__(self, game_id, red=0, green=0, blue=0):
        self.ID = game_id
        self.red = red
        self.green = green
        self.blue = blue
        self.total_cubes = self.red + self.green + self.blue

def get_game_id(strInput) -> int:
    return int(strInput.strip().split(":")[0].split(" ")[1])

def get_games(strInput: str) -> list[str]:
    data = strInput.split(":")[1]
    reveals = []
    for reveal in data.split(";"):
        reveals.append(reveal.strip())
    return reveals

def get_revealed_cubes(games: list[dict[str, int]]):
    result = []
    for game in games:
        reveal_data = {}
        dig_color_pairs = game.strip().split(",")
        for pair in dig_color_pairs:
            pair = pair.strip().split(" ")
            digit = int(pair[0])
            color = pair[1]
            reveal_data[color] = digit
        result.append(reveal_data)
    return result

def set_game_data(game: Game, revealed_cubes: list[dict[str, int]]) -> list[Game]:
    ID = game.ID
    result = []
    for game_dict in revealed_cubes:
        inner_game = Game(ID)
        revealed_colors = [key for key in game_dict.keys()]
        for color in revealed_colors:
            setattr(inner_game, color, game_dict[color])
        inner_game.total_cubes = sum([inner_game.red, inner_game.blue, inner_game.green])
        result.append(inner_game)
    return result

    
    
def game_is_possible(list_of_games: list[Game]) -> bool:
    for game in list_of_games:
        conditions = [
                game.red <= Bag.red,
                game.green <= Bag.green,
                game.blue <= Bag.blue,
                game.total_cubes <= Bag.total_cubes
                ]
        if all(conditions):
            continue
        else:
            return False
    return True

class Testing:
    first_input = puzzle_input[0]
    game_ID = get_game_id(first_input)
    inner_games = get_games(first_input)
    revelations = get_revealed_cubes(inner_games)
    list_of_games = set_game_data(Game(game_ID), revelations)
    
def get_sum_of_possible_game_IDs(puzzle_input: str):
    IDs_to_sum = []
    for line in puzzle_input:
        ID = get_game_id(line)
        temp_game = Game(ID)
        inner_games = get_games(line)
        revelations = get_revealed_cubes(inner_games)
        list_of_game_objects = set_game_data(temp_game, revelations)
        if game_is_possible(list_of_game_objects):
            IDs_to_sum.append(ID)
    return sum(IDs_to_sum)

def get_game_power(game_objects: list[Game]) -> list[int]:
    red = []
    green = []
    blue = []

    for game in game_objects:
        red.append(getattr(game, "red"))
        green.append(getattr(game, "green"))
        blue.append(getattr(game, "blue"))
    power = max(red)*max(green)*max(blue)
    return power


# print(get_sum_of_possible_game_IDs(puzzle_input))
powers = []
for line in puzzle_input:
    temp_game = Game(0)
    inner_games = get_games(line)
    revelations = get_revealed_cubes(inner_games)
    list_of_game_objs = set_game_data(temp_game, revelations)
    powers.append(get_game_power(list_of_game_objs))
print(sum(powers))
