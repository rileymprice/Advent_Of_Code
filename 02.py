

input_path = 'input/02.txt'
def part_one():
    horizontal_pos = 0
    depth_pos = 0
    with open(input_path, 'r') as input_file:
        for line in input_file.readlines():
            position,change = line.split(' ')
            change = int(change)
            if position == 'forward':
                horizontal_pos += change
            elif position == 'up':
                depth_pos -= change
            else:
                depth_pos += change
    return horizontal_pos * depth_pos

print(part_one())

def part_two():
    horizontal_pos = 0
    depth_pos = 0
    aim = 0
    with open(input_path, 'r') as input_file:
        for line in input_file.readlines():
            position,change = line.split(' ')
            change = int(change)
            if position == 'forward':
                horizontal_pos += change
                depth_change = change * aim
                depth_pos += depth_change
            elif position == 'up':
                aim -= change
            else:
                aim += change
    return horizontal_pos * depth_pos

print(part_two())