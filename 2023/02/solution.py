import os


def part_one(lines: list) -> int:
    bag_total = {'red': 12,'green':13, 'blue': 14}
    total = 0
    for line in lines:
        info,game = line.split(':')
        game_number = int(info.split(' ')[1])
        real_game = True
        draws = game.strip().split(';')
        for draw in draws:
            cubes = draw.split(',')
            for cube in cubes:
                cube = cube.strip()
                number,color = cube.split(' ')
                if int(number) > bag_total[color]:
                    real_game = False
        if real_game:
            total += game_number
    return total



def part_two(lines: list) -> int:
    total = 0
    for line in lines:
        red,green,blue = 0,0,0
        info,game = line.split(':')
        game_number = int(info.split(' ')[1])
        real_game = True
        draws = game.strip().split(';')
        for draw in draws:
            cubes = draw.split(',')
            for cube in cubes:
                cube = cube.strip()
                number,color = cube.split(' ')
                number = int(number)
                red = number if color == 'red' and number > red else red
                green = number if color =='green' and number > green else green
                blue = number if color == 'blue' and number > blue else blue
        total += red*blue*green
    return total

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        lines = [x.replace("\n", "") for x in lines]
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
