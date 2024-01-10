import random

with open("input.txt") as infile:
    all_lines = infile.readlines()

instructions = all_lines[0].strip()

network_lines = all_lines[2:]

network = {}

starts = []

for network_line in network_lines:
    source = network_line[:3]
    left = network_line[7:10]
    right = network_line[12:15]

    network[source] = (left, right)
    if source.endswith("A"):
        starts.append(source)

print(network)

zs = {}
cycles = {}

for start in starts:
    print("Start", start)
    i = 0
    current = start
    visited = [start]
    while True:
        index = i % len(instructions)
        inst = instructions[index]

        left, right = network[current]
        # print(current, inst, left, right)

        current = left if inst == "L" else right

        current_id = str(index) + current
        # print(current, visited)
        if i < 6:
            print(current)

        if current.endswith("Z"):
            zs[start] = i + 1

        if current_id in visited:
            cycles[start] = 1 + i - visited.index(current_id)
            # visited.append(current_id)
            print("Ends with return to", current)
            break

        i += 1
        visited.append(current_id)

    # print(visited)

print("Zs")
print(zs)
print("Cycles")
print(cycles)

positions = zs

while len(set(positions.values())) > 1:
    lowest = min(positions.values())
    for start, position in positions.items():
        if position == lowest:
            positions[start] += cycles[start]
    if random.randint(0, 1000000) == 0:
        print(positions)

print(positions)
print("Success in", set(positions.values()), "steps")
