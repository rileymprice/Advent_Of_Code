

def binary_to_decimal(binary):
    return int(str(binary),2)

def decimal_to_binary(decimal):
    return format(decimal,'b')

input_path = f'input/03.txt'
input_data = []
line_max_size = 0
with open(input_path,'r') as input_file:
    for line in input_file.readlines():
        input_data.append(line.strip())
        if len(line.strip()) > line_max_size:
            line_max_size = len(line.strip())


def part_one(input_data, max_size):
    gamma = [0]*max_size
    epsilon = [0]*max_size
    location_list = []
    for _ in range(max_size):
        location_list.append([0,0])
    for line in input_data:
        for index,digit in enumerate(str(line)):
            location_list[index][int(digit)] += 1
    for index,location in enumerate(location_list):
        max_value = max(location)
        binary = location.index(max_value)
        if binary == 0:
            gamma[index] = '0'
            epsilon[index] = '1'
        else:
            gamma[index] = '1'
            epsilon[index] = '0'
    #print(gamma,type(gamma))
    gamma = ''.join(gamma)
    epsilon = ''.join(epsilon)
    return int(gamma), int(epsilon)
most,least = part_one(input_data,line_max_size)
#print(most)
print(f'Part One: {binary_to_decimal(most)*binary_to_decimal(least)}')

def part_two(input_data,max_size):
    #print('i')
    most,least = part_one(input_data,max_size)
    most = part_two_helper(str(most),input_data)
    least = part_two_helper(str(least),input_data)
    most = binary_to_decimal(most)
    least = binary_to_decimal(least)
    return most,least


def part_two_helper(compare_list,input_data):
    #print('hi')
    index = 0
    result = input_data.copy()
    while len(result) > 1:
        result = [number for number in result if number[index] == compare_list[index]]
        index += 1
    return result[0]


oxygen,co2 = part_two(input_data,line_max_size)
print(f'Part Two: {oxygen*co2}')
        
    

        