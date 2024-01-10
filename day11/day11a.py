
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

for blank in blank_rows[::-1]:
    universe.insert(blank, [False] * universe_width)

blank_cols = []

universe_width = len(universe[0])
universe_height = len(universe)

for col_num in range(universe_width):
    if all(not row[col_num] for row in universe):
        blank_cols.append(col_num)


for blank in blank_cols[::-1]:
    for row in universe:
        row.insert(blank, False)

# draw()


universe_width = len(universe[0])
universe_height = len(universe)

galaxies = []

for row_num, row in enumerate(universe):
    for col_num, cell in enumerate(row):
        if cell:
            galaxies.append((col_num, row_num))

print(galaxies)


total_dist = 0

for gx, gy in galaxies:
    for ox, oy in galaxies:
        total_dist += (abs(ox - gx) + abs(oy - gy))

print("The total path distance is", total_dist // 2)
