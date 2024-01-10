with open("input.txt") as infile:
    all_lines = infile.readlines()

instructions = all_lines[0].strip()

network_lines = all_lines[2:]

network = {}

for network_line in network_lines:
    source = network_line[:3]
    left = network_line[7:10]
    right = network_line[12:15]

    network[source] = (left, right)


print(network)

i = 0
current = "AAA"
while current != "ZZZ":
    inst = instructions[i % len(instructions)]
    i += 1

    left, right = network[current]
    # print(current, inst, left, right)

    current = left if inst == "L" else right

print("Reached", current, "in", i, "steps")