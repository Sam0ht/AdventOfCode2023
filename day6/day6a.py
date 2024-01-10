import numpy as numpy

with open("example.txt") as infile:
    times_str, distances_str = infile.readlines()
    times = [t for t in times_str.split(" ") if t]
    times = [int(t) for t in times[1:]]
    print("times:", times)

    distances = [d for d in distances_str.split(" ") if d]
    distances = [int(d) for d in distances[1:]]
    print("distances:", distances)

    races = [(times[i], distances[i]) for i in range(len(times))]

    print("races", races)

    race_options = []
    for time, record_distance in races:

        best_hold_time = int(time / 2)
        best_run_time = time - best_hold_time

        best_distance = best_hold_time * best_run_time

        print("best distance", best_distance)

        options_half = best_distance - record_distance

        print("there are approx", 2 * options_half, "ways to win")

        options = []
        for hold_time in range(time):
            distance = hold_time * (time - hold_time)  # symmetrical
            options.append((hold_time, distance))
        print("RACE:", time, "s", record_distance, "mm")
        # print(options)
        winning_options = [(h, d) for h, d in options if d > record_distance]
        print(winning_options)
        race_options.append(len(winning_options))

    print("The multiplication of all winning options in all races is", numpy.prod(race_options))