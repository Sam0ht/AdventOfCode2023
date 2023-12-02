numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def find(line, direction=1):
    for index in range(len(line))[::direction]:
        target = line[index:]
        for n in range(1, 10):
            if target.startswith(str(n)) or target.startswith(numbers[n-1]):
                return n

with open("input.txt") as infile:
    answer = sum((10 * find(line)) + find(line, -1) for line in infile.readlines())
    print("The total is", answer)