import sys
from typing import List


class Range:
    def __init__(self, data_string):
        dest, source, length = [int(s) for s in data_string.strip().split(" ")]
        self.delta = dest - source
        self.input_range = range(source, source + length)

    def convert(self, input_value: int):
        if input_value in self.input_range:
            return input_value + self.delta

    def contains(self, input_value: int):
        return input_value in self.input_range

    def __repr__(self):
        return f"Range({self.input_range} +{self.delta})"

    def convert_range(self, other_range: range):
        lower = range(other_range[0], self.input_range[0])
        higher = range(self.input_range[-1], other_range[-1])
        intersection = range(max(other_range[0], self.input_range[0]), min(other_range[-1], self.input_range[-1])+1)
        if len(intersection) == 0:
            return [other_range], []
        return [n for n in [lower, higher] if len(n) > 0], \
               [range(intersection.start + self.delta, intersection.stop + self.delta)]


class Map:
    def __init__(self, name: str, ranges: List[str]):
        desc, _ = name.split(" ")
        desc_tokens = desc.split("-")
        self.input = desc_tokens[0]
        self.output = desc_tokens[-1]

        self.ranges = [Range(r) for r in ranges]

    @staticmethod
    def from_chunk(chunk: str):
        lines = chunk.split("\n")
        return Map(lines[0], lines[1:])

    def convert(self, input_value: int):
        for range in self.ranges:
            if range.contains(input_value):
                return range.convert(input_value)
        return input_value

    def __repr__(self):
        return f"Map({self.input} to {self.output} - {self.ranges})"

    def convert_range(self, current_range: range):
        unprocessed_ranges = [current_range]
        processed_ranges = []
        for r in self.ranges:
            new_unprocessed = []
            for ur in unprocessed_ranges:
                unprocessed, processed = r.convert_range(ur)
                processed_ranges.extend(processed)
                new_unprocessed.extend(unprocessed)

            unprocessed_ranges = new_unprocessed

        return processed_ranges + unprocessed_ranges

def flatten(lol):
    return [item for sublist in lol for item in sublist]

with open("input.txt") as infile:
    indata = infile.read()
    chunks = indata.split("\n\n")
    seeds_line = chunks[0]
    maps_chunks = chunks[1:]

    seeds = [int(s) for s in seeds_line.split(" ")[1:]]

    maps = [Map.from_chunk(chunk.strip()) for chunk in maps_chunks]

    locations = []
    for seed in seeds:
        current = seed
        for map in maps:
            current = map.convert(current)
        assert map.output == "location"
        locations.append(current)

    print("The lowest single seed number is", min(locations))

    seed_ranges = [range(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

    current_ranges = [r for r in seed_ranges]
    for map in maps:
        current_ranges = flatten([map.convert_range(current_range) for current_range in current_ranges])

    print("The range lowest is", min(r.start for r in current_ranges))



