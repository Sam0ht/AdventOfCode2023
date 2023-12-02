with open("input.txt") as infile:
    line_values = []
    for inline in infile.readlines():
        data = inline.strip()
        digits = [n for n in data if n.isdigit()]
        line_value = int(digits[0] + digits[-1])
        line_values.append(line_value)
    print("The total is", sum(line_values))