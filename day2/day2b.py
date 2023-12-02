from typing import List

def count_maxima(shows: List[str]):
    counts = {
        "red": [],
        "green": [],
        "blue": []
    }
    for show in shows:
        colours = show.split(",")
        for colour in colours:
            count, colour_name = colour.strip().split(" ")
            counts[colour_name].append(int(count))

    total = 1
    for colour_counts in counts.values():
        total *= max(colour_counts)

    return total

with open("input.txt") as infile:
    total = 0
    for inline in infile.readlines():
        _, data = inline.split(":")
        shows = data.split(";")
        total += count_maxima(shows)
    print("The sum of game powers is", total)