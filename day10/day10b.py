grid = []
with open("input.txt") as infile:
    for inline in infile.readlines():
        grid.append(list(inline.strip()))

start = (0, 0)

for rownum, row in enumerate(grid):
    # print(row)
    print("".join(row))
    if "S" in row:
        start = (row.index("S"), rownum)

print("Start at", start)

def value(x: int, y: int) -> str:
    return grid[y][x]

visited = {start}

current = start

connections = {
    "-": ((-1, 0), (1, 0)),
    "|": ((0, 1), (0, -1)),
    "F": ((0, 1), (1, 0)),
    "J": ((0, -1), (-1, 0)),
    "7": ((0, 1), (-1, 0)),
    "L": ((1, 0), (0, -1)),
    ".": ()
}


nextp = None

for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
    cx, cy = current
    ox = cx - dx
    oy = cy - dy
    connects = connections[value(ox, oy)]
    if (dx, dy) in connects:
        nextp = (ox, oy)

print(nextp, grid[oy][ox], "is a connection")



visited.add(nextp)

prev = start
current = nextp

print(visited)


while True:
    cx, cy = current
    character = value(cx, cy)
    connects = connections[character]

    adjoining = {(cx + conx, cy + cony) for conx, cony in connects}

    adjoining.remove(prev)
    nextp = adjoining.pop()
    assert len(adjoining) == 0

    print("Next pos is", nextp, value(*nextp))

    if nextp in visited:
        break

    visited.add(nextp)

    prev = current
    current = nextp



print("visited", visited)
print("Furthest steps", int(len(visited) / 2))

loop = visited

corners = {"F": True, "7": True, "L": False, "J": False}

enclosed = []

for rownum, row in enumerate(grid):
    print("".join(row))
    inside = False
    corners_seen = []
    for cellnum, cell in enumerate(row):
        if (cellnum, rownum) in loop:
            if cell == "|":
                inside = not inside
            if cell in corners:
                corners_seen.append(cell)
                if len(corners_seen) == 2:
                    values = [corners[cs] for cs in corners_seen]
                    if True in values and False in values:
                        inside = not inside
                    corners_seen = []
        else:
            if inside:
                enclosed.append((cellnum, rownum))
            corners_seen = []

print(enclosed)
print("The loop encloses", len(enclosed), "squares")
