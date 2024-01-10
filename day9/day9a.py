from typing import List


def diffs(num_list: List[int]) -> List[int]:
    return [b - a for a, b in zip(num_list[:-1], num_list[1:])]

total_end = 0
total_start = 0

with open("example.txt") as infile:
    for inline in infile.readlines():
        values = [int(s) for s in inline.strip().split(" ")]
        sequences = [values]
        while not all([v == 0 for v in sequences[-1]]):
            sequences.append(diffs(sequences[-1]))


        sequences[-1].append(0)

        for s1, s2 in zip(sequences[::-1][:-1], sequences[::-1][1:]):
            s2.append(s1[-1] + s2[-1])

        for s in sequences:
            print(s)

        total_end += sequences[0][-1]

print("The total is", total_end)
