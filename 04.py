input_path = 'input/04.txt'
with open (input_path,'r') as input_file:
    input_data = input_file.readlines()
    bingo_numbers = ''
    new_card = False
    bingo_card_list = []
    bingo_card = []
    for index,line in enumerate(input_data):
        if not bingo_numbers:
            bingo_numbers = line.split(',')
            bingo_numbers = [int(x) for x in bingo_numbers]
        else:
            if line == '\n':
                new_card = True
                if index != 1:
                    #print(bingo_card)
                    bingo_card_list.append(bingo_card)
                bingo_card = []
                continue
            line = line.strip().split(' ')
            line = list(filter(lambda x: x != '', line))
            line = [int(x) for x in line]
            #print(line)
            bingo_card.append(line)

#Mark a number with -1 if it exists
def mark_a_number(board,number):
    for row in board:
        if number in row:
            pos = row.index(number)
            row[pos] = -1

#Checks to see if given board has a row or column of -1, if it is then return the board minus the winning column else return False
def is_a_winner(board):
    for row in board:
        if sum(row) == -5:
            return True
    cols = [list(x) for x in zip(*board)]
    for col in cols:
        if sum(col) == -5:
            return True
    return False


def calculate_remainder(board):
    overall = 0
    for row in board:
        row_sum = sum(x for x in row if x >= 0)
        overall += row_sum
    return overall


def part_one(bingo_numbers, bingo_card_list):
    tries = 0
    for number in bingo_numbers:
        #print(number)
        for index,board in enumerate(bingo_card_list):
            mark_a_number(board,number)
            if is_a_winner(board):
                #print(board, index)
                return calculate_remainder(board) * number
        #print(bingo_card_list[0])
print(part_one(bingo_numbers,bingo_card_list))