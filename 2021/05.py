input_path = 'input/05.txt'
input_data = []
max_x = 0
max_y = 0
with open(input_path,'r') as input_file:
    lines = input_file.readlines()
    for line in lines:
        input_line = set()
        dots = line.split(' -> ')
        for index,dot in enumerate(dots):
            x,y = dot.split(',')
            x,y = int(x),int(y)
            max_x = x if x > max_x else max_x
            max_y = y if y > max_y else max_y
            if index == 0:
                start = [x,y]
            else:
                end = [x,y]
        input_line = start+end
        input_data.append(input_line)


def build_line_map(row_count,col_count):
    row = [0]*max_x
    line_map = [row]*max_y
    return line_map

def part_one(input_data):
    crosses = 0
    line_map = build_line_map(max_x,max_y)
    for line in input_data:
        #print(line)

        start_dot = line[0:2]
        end_dot = line[2:4]
        #check for straight line
        if start_dot[0] == end_dot[0]:
            #print(f'x is the same')
            x_coordinate = start_dot[0]
            if start_dot[1] > end_dot[1]: start_dot[1],end_dot[1] = end_dot[1],start_dot[1]
            for column in range(start_dot[1], end_dot[1]):
                line_map[x_coordinate][column] += 1
                if line_map[x_coordinate][column] > 1:
                    crosses += 1
                    #print(crosses)
        elif start_dot[1] == end_dot[1]:
            #print('y is the same')
            y_coordinate = start_dot[1]
            if start_dot[0] > end_dot[0]: start_dot[0],end_dot[0] = end_dot[0],start_dot[0]
            for row in range(start_dot[0], end_dot[0]):
                line_map[row][y_coordinate] += 1
                if line_map[row][y_coordinate] > 1:
                    crosses += 1
        #print(line_map)
    return crosses
print(input_data[:50])
print(f'Part One: {part_one(input_data)}')