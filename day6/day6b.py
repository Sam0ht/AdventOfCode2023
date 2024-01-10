import numpy as numpy

with open("input.txt") as infile:
    times_str, distances_str = infile.readlines()

    time = int(times_str.split(":")[1].replace(" ", ""))
    print("time", time)

    record_distance = int(distances_str.split(":")[1].replace(" ", ""))
    print("distance", record_distance)

    best_hold_time = int(time / 2)
    best_run_time = time - best_hold_time

    best_distance = best_hold_time * best_run_time

    print("best distance", best_distance)

    options_half = best_distance - record_distance

    print("RACE:", time, "s", record_distance, "mm")

    winning_options = 0
    for hold_time in range(time):
        distance = hold_time * (time - hold_time)  # symmetrical
        if distance > record_distance:
            winning_options += 1 # .append((hold_time, distance))
            if winning_options % 100000 == 0:
                print("Found", winning_options, "options")
    # print(options)
    # winning_options = [(h, d) for h, d in options if d > record_distance]
    # print(winning_options)
    print("There are", winning_options, "ways to win")
