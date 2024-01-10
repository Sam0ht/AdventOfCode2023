import re

with open('example.txt', 'r') as game_data_file:

    game_data = [x.rstrip('\n') for x in game_data_file]
    print("cube_data = " + str(game_data))

    game_one = []
    game_two = []
    game_three = []
    string_list = [str(element) for element in game_data]
    print('game data = ', game_data)


    #game = game_data.pop()
    #game_string = str(game)
    #print(game_string)
    #print(game)

    games = [i.split(':', 1)[0] for i in game_data]
    print('Games = ', games)

    retrieved = [i.split(' ', 1)[1] for i in game_data]
    print('Retrieved = ', retrieved)

    sorted = [i.split(':', 1)[1] for i in retrieved]
    print('Sorted =', sorted)

    counter = 0
    iteration = 0
    holding_list = []
    index_position = []
    game_outcomes = []

    for i in sorted:
        print('iteration = ', iteration)
        iteration += 1
        myString = str(sorted[counter])
        myList = re.split('\s', myString)
        print('my list =', myList)

        for item, index in enumerate(myList):
            if index == 'blue,'or index == 'blue;':
                print(item, index)
                index_position.append(item)
                print(index_position)
        index_position.clear()
        counter += 1

        print("The original list : " + str(myList))

        particular_value_blue = 'blue;'
        particular_value_green = 'green;'
        particular_value_red = 'red;'
        result = []
        result_ints = []
        temp_list = []
        for i in myList:
            if i == particular_value_blue or i == particular_value_green or i == particular_value_red:
                temp_list.append(i)
                result.append(temp_list)
                temp_list = []
            else:
                temp_list.append(i)
        result.append(temp_list)
        print("The list after splitting by a value : " + str(result))

        for item in result:
            for thing, index in enumerate(item):
                print(thing, index)

        add_red = []
        add_green = []
        add_blue = []
        blue_yes = []
        red_yes = []
        green_yes = []

        for item in result:

            for thing, index in enumerate(item):
                if index == 'red,' or index == 'red;' or index == 'red':
                    position = thing
                    number = position -1
                    add_red.append(item[number])
                    print('red list = ', add_red)
                    for value in (add_red):
                        int_add_red = list(map(int, add_red))
                        for item in int_add_red:
                            if item >= 12:
                                red_yes.append(iteration)
                                print('red excess detected = ', red_yes)
                                for item in red_yes:
                                    games.append(red_yes[0])
                                    print('games = ', games)

        for item in result:
            for thing, index in enumerate(item):
                if index == 'green,' or index == 'green;' or index == 'green':
                    position = thing
                    number = position -1
                    add_green.append(item[number])
                    print('green list = ', add_green)
                    for value in (add_green[1:]):
                        int_add_green = list(map(int, add_green))
                        for item in int_add_green:
                            if item >= 13:
                                green_yes.append(iteration)
                                print('green excess detected= ', green_yes)
                                for item in green_yes:
                                    games.append(green_yes[0])
                                print('games = ', games)
        for item in result:
            for thing, index in enumerate(item):
                if index == 'blue,' or index == 'blue;' or index == 'blue':
                    position = thing
                    number = position -1
                    add_blue.append(item[number])
                    print('blue list = ', add_blue)
                    int_add_blue = list(map(int, add_blue))
                    for item in int_add_blue:
                        if item >= 14:
                            blue_yes.append(iteration)
                            print('blue excess detected = ', blue_yes)
                            for item in blue_yes:
                                games.append(blue_yes[0])
                            print('games = ', games)

            #12 red cubes, 13 green cubes, and 14 blue cubes.