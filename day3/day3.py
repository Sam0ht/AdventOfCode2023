import dataclasses
from typing import List


@dataclasses.dataclass
class Cell:
    value: str
    neighbours: List['Cell'] = dataclasses.field(default_factory=list)
    partners: List['Cell'] = dataclasses.field(default_factory=list)
    is_subsequent = False
    part_number: 'PartNumber' = None

    def __str__(self):
        return f"Cell[{self.value}] ({self.is_subsequent}) " \
               f"({','.join([c.value for c in self.neighbours])}) " \
               f"<{','.join([c.value for c in self.partners])}> "

    def add_neighbour(self, other: 'Cell', subsequent):
        if other.value == "." or self.value == ".":
            return

        self.neighbours.append(other)
        if subsequent and other.is_digit() and self.is_digit():
            self.partners.append(other)
            other.is_subsequent = True

    def is_digit(self):
        return self.value.isdigit()

    def is_symbol(self):
        return not self.is_digit() and not self.value == "."

    def neighbouring_symbol(self):
        return any(c.is_symbol() for c in self.neighbours)

    def is_star(self):
        return self.value == "*"

    def adjacent_digits(self):
        return [c for c in self.neighbours if c.is_digit()]

    def adjacent_part_numbers(self):
        part_nos = [cell.part_number for cell in self.adjacent_digits()]
        return {id(p): p for p in part_nos}

    def is_gear(self):
        return len(self.adjacent_part_numbers().values()) == 2

    def gear_ratio(self):
        assert self.is_gear()
        a, b = self.adjacent_part_numbers().values()
        return a.value() * b.value()

@dataclasses.dataclass
class PartNumber:
    digits: List[Cell] = dataclasses.field(default_factory=list)

    def __init__(self, digits):
        self.digits = digits
        for d in self.digits:
            d.part_number = self

    @staticmethod
    def starting_from(cell: Cell):
        current = cell
        digits = []
        while True:
            digits.append(current)
            if not len(current.partners):
                break
            current = current.partners[0]

        return PartNumber(digits=digits)

    def has_symbol(self):
        return any(cell.neighbouring_symbol() for cell in self.digits)

    def __str__(self):
        return "".join([c.value for c in self.digits])

    def value(self):
        return int(self.__str__())


grid: List[List[Cell]] = []

with open("input.txt") as infile:
    for line in infile.readlines():
        grid.append([])
        for c in line[:-1]:
            grid[-1].append(Cell(value=c))


for rn, row in enumerate(grid):
    for cn, cell in enumerate(row):
        for i in [rn-1, rn, rn+1]:
            if 0 <= i < len(grid):
                for j in [cn - 1, cn, cn +1]:
                    if 0 <= j < len(row):
                        if i != rn or j != cn:
                            cell.add_neighbour(grid[i][j], i == rn and j == cn+1)

part_numbers = []

for row in grid:
    for cell in row:
        if cell.is_digit() and not cell.is_subsequent:
            part_numbers.append(PartNumber.starting_from(cell))

valid_numbers = [n for n in part_numbers if n.has_symbol()]

print("The sum of all part numbers is", sum(n.value() for n in valid_numbers))

gear_ratios_total = 0

for row in grid:
    for cell in row:
        if cell.is_gear():
            gear_ratios_total += cell.gear_ratio()

print("The sum of all gear ratios is", gear_ratios_total)