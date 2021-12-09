input_path = "input/06.txt"
input_data = []

NEW_FISH_LIFE = 8
FISH_MOM = 6
DAYS_TO_SIMULATE = 80
DAYS_TO_SIMULATE_PART_TWO = 256
with open(input_path, "r") as input_file:
    line = input_file.readline()
    fishes = line.split(",")
    fish_ages = [0] * 9
    for fish in fishes:
        fish = int(fish)
        fish_ages[fish] += 1


def pass_day(list_of_ages):
    list_of_ages.append(list_of_ages.pop(0))
    list_of_ages[6] += list_of_ages[8]
    return list_of_ages


def part_one(days, fish_list):

    # given_list = [0, 1, 1, 2, 1, 0, 0, 0, 0]
    for _ in range(days):
        fish_list = pass_day(fish_list)
        # print(len(list_of_fish))
    return sum(fish_list)


print(f"Part One: {part_one(80, fish_ages)}")
print(f"Part Two: {part_one(256, fish_ages)}")
