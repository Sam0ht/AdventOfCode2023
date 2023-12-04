from collections import defaultdict

cards = defaultdict(lambda: 1)
with open("input.txt") as infile:
    for inline in infile.readlines():
        card_and_id, numbers = inline.strip().split(":")
        card_id = int(card_and_id.split(" ")[-1])
        winning, present = numbers.split("|")
        winning_numbers = set(int(n) for n in winning.strip().split(" ") if n != "")
        present_numbers = set(int(n) for n in present.strip().split(" ") if n != "")
        your_wins = len(winning_numbers.intersection(present_numbers))

        my_copies = cards[card_id]
        for copy_id in range(card_id + 1, card_id + 1 + your_wins):
            cards[copy_id] += my_copies

print(cards)
print("The total number of scratchcards is", sum(cards.values()))