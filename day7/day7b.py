from functools import cmp_to_key


ranks = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

hands = []
with open("input.txt") as infile:
    for inline in infile.readlines():
        cards, bid = inline.split(" ")
        hands.append((cards, int(bid)))


def occurrences(hand: str):
    uniques = set(hand)
    counts = {u: hand.count(u) for u in uniques}
    if "J" not in counts or len(counts) == 1:
        return counts
    jokers = counts["J"]
    del counts["J"]
    max_value = max(counts.values())
    for char, count in counts.items():
        if count == max_value:
            counts[char] += jokers
            return counts


for hand in hands:
    print(hand, occurrences(hand[0]))

print("===")

def compare(hand_and_bid_1, hand_and_bid_2):
    hand1, _ = hand_and_bid_1
    hand2, _ = hand_and_bid_2
    o1 = occurrences(hand1)
    o2 = occurrences(hand2)
    if max(o1.values()) != max(o2.values()):
        return max(o2.values()) - max(o1.values())
    if len(o1) != len(o2):
        return len(o1) - len(o2)
    for i in range(5):
        if hand1[i] != hand2[i]:
            return ranks.index(hand1[i]) - ranks.index(hand2[i])
    return 0

sorted = sorted(hands, key=cmp_to_key(compare))

total = 0
for r, s in enumerate(sorted):
    cards, bid = s
    rank = len(sorted) - r
    print(rank, cards, bid)
    total += (rank * bid)

print("The total is", total)