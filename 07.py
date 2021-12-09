input_path = "input/07.txt"

with open(input_path, "r") as input_file:
    input_data = input_file.readline()
    input_data = [int(x) for x in input_data.split(",")]


def calculate_fuel(list_of_pos, target):
    fuel_used = 0
    for pos in list_of_pos:
        fuel_used += abs(pos - target)
    return fuel_used


def minimal_fuel(list_of_pos):
    lowest_fuel_used = -1
    for pos in list_of_pos:
        fuel = calculate_fuel(list_of_pos, pos)
        if lowest_fuel_used == -1:
            lowest_fuel_used = fuel
        elif fuel < lowest_fuel_used:
            lowest_fuel_used = fuel
    return lowest_fuel_used


def part_one(input_data):
    return minimal_fuel(input_data)


print(f"Part One: {part_one(input_data)}")


def calculate_fuel_2(list_of_pos, target):
    fuel_used = 0
    for pos in list_of_pos:
        move = abs(pos - target)
        fuel_used += move * ((1 + move) / 2)
    return fuel_used


def minimal_fuel_2(list_of_pos):
    lowest_fuel_used = -1
    for pos in list_of_pos:
        fuel = calculate_fuel_2(list_of_pos, pos)
        if lowest_fuel_used == -1:
            lowest_fuel_used = fuel
        elif fuel < lowest_fuel_used:
            lowest_fuel_used = fuel
    return lowest_fuel_used


def part_two(input_data):
    return minimal_fuel_2(input_data)


print(f"Part Two: {part_two(input_data)}")
