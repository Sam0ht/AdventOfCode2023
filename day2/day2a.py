# only 12 red cubes, 13 green cubes, and 14 blue cubes
maxima = {
    "red": 12,
    "green": 13,
    "blue": 14
}
from typing import List


def check_shows(shows: List[str]):
    for show in shows:
        colours = show.split(",")
        for colour in colours:
            count, colour_name = colour.strip().split(" ")
            if int(count) > maxima[colour_name]:
                return False
    return True


with open("input.txt") as infile:
    total = 0
    for inline in infile.readlines():
        game, data = inline.split(":")
        _, game_id = game.split(" ")
        shows = data.split(";")
        if check_shows(shows):
            total += int(game_id)
    print("The sum of valid ids is", total)