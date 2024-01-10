with open("input.txt") as infile:
    all_lines = infile.readlines()

instructions = all_lines[0].strip()

network_lines = all_lines[2:]

network = {}

starts = []
ends = []

for network_line in network_lines:
    source = network_line[:3]
    left = network_line[7:10]
    right = network_line[12:15]

    network[source] = (left, right)
    if source.endswith("A"):
        starts.append(source)
    # elif source.endswith("Z"):
    #     ends.append(source)

print(network)

print(starts)

i = 0
current = starts
while not all(c.endswith("Z") for c in current):
    inst = instructions[i % len(instructions)]
    i += 1

    next = []
    for c in current:
        left, right = network[c]
        next.append(left if inst == "L" else right)

    current = next
    if (i % 100000) == 0:
        print(i, inst, next)


print("Reached", current, "in", i, "steps")