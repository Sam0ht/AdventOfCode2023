total = 0
with open("input.txt") as infile:
    for inline in infile.readlines():
        _, numbers = inline.strip().split(":")
        winning, present = numbers.split("|")
        winning_numbers = set(int(n) for n in winning.strip().split(" ") if n != "")
        present_numbers = set(int(n) for n in present.strip().split(" ") if n != "")
        your_wins = len(winning_numbers.intersection(present_numbers))

        if your_wins > 0:
            total += 2 ** (your_wins - 1)

print("Your total score is", total)