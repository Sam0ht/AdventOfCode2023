def parse(char: str):
    if char == "?":
        return None
    return char == "#"


def calc_runs(broken_springs):
    read_runs = []
    current = 0
    for c in broken_springs:
        if c:
            current += 1
        elif current > 0:
            read_runs.append(current)
            current = 0
    if current > 0:
        read_runs.append(current)
    return read_runs

def find_all(sought, inlist):
    locations = []
    for i, v in enumerate(inlist):
        if v == sought:
            locations.append(i)
    return locations

total = 0

with open("input.txt") as infile:
    for inline in infile.readlines():
        springs_string, runs_string = inline.split(" ")
        broken_springs = [parse(c) for c in springs_string]
        runs = [int(c) for c in runs_string.split(",")]

        unknown_locations = find_all(None, broken_springs)
        print(unknown_locations)

        num_combo = 2 ** len(unknown_locations)
        print(num_combo, "combinations")

        combos = []
        for i in range(num_combo):
            bit_value = list("000000000000000000" + str(bin(i))[2:])
            # print("bit_value",bit_value)
            new_combo = []
            for v in broken_springs[::-1]:
                if v is None:
                    new_combo.append(bit_value.pop() == "1")
                else:
                    new_combo.append(v)
            combos.append(list(reversed(new_combo)))


        # read_runs = calc_runs(broken_springs)

        # for run in combos:
        #     print(list(run), calc_runs(run))

        valid_runs = [run for run in combos if calc_runs(run) == runs]


        print("Springs:", broken_springs, "Valid Runs:", len(valid_runs), "namely", valid_runs)

        total += len(valid_runs)
        # break

print("The total of all valid combos is", total)