from collections import deque
input_file = f'input/01.txt'

def part_one():
    last_input = -1
    increase_jump = 0
    with open(input_file,'r') as input_doc:
        for line in input_doc.readlines():
            if last_input == -1:
                last_input = int(line)
            if int(line) > last_input:
                increase_jump += 1
            last_input = int(line)
    return increase_jump

print(f'Part one: {part_one()}')

def part_two():
    first_list = deque()
    second_list = deque()
    second_sum = -1
    total_increases = 0
    with open(input_file,'r') as input_doc:
        for line in input_doc.readlines():
            if second_sum != -1:
                second_list.appendleft(int(line))
            if len(first_list) == 3 and len(second_list) == 3:
                if sum(first_list) < sum(second_list):
                    total_increases += 1
                first_list.pop()
                second_list.pop()
            first_list.appendleft(int(line))
            second_sum = 0
    return total_increases

print(f'Part two: {part_two()}')