
universe = []
with open("input.txt") as infile:
    for inline in infile.readlines():
        universe.append([c == "#" for c in inline.strip()])

universe_width = len(universe[0])
universe_height = len(universe)

def draw():
    print("|" * universe_width)
    for row in universe:
        print("".join("#" if cell else "." for cell in row))

blank_rows = []
for rownum, row in enumerate(universe):
    if all(not c for c in row):
        blank_rows.append(rownum)


blank_cols = []

universe_width = len(universe[0])
universe_height = len(universe)

for col_num in range(universe_width):
    if all(not row[col_num] for row in universe):
        blank_cols.append(col_num)


universe_width = len(universe[0])
universe_height = len(universe)

galaxies = []

for row_num, row in enumerate(universe):
    for col_num, cell in enumerate(row):
        if cell:
            galaxies.append((col_num, row_num))

print(galaxies)


expansion_factor = 1000000

total_dist = 0

def dist(galaxy1, galaxy2):
    gx, gy = galaxy1
    ox, oy = galaxy2
    expanded = len([ex for ex in blank_cols if gx < ex < ox or ox < ex < gx]) +\
               len([ey for ey in blank_rows if gy < ey < oy or oy < ey < gy])

    return abs(ox - gx) + abs(oy - gy) + (expanded * (expansion_factor - 1))


for galaxy in galaxies:
    for other in galaxies:
        total_dist += dist(galaxy, other)

print("The total path distance is", total_dist // 2)
