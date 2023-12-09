import os

# def part_one():



def part_one(lines: list) -> int:
    total = 0
    for line in lines:
        numbers = [int(i) for i in line if i.isdigit()]
        total += int(f'{numbers[0]}{numbers[len(numbers)-1]}')
    return total



def part_two(lines: list) -> int:
    total = 0
    for line in lines:
        first_digit = -1
        last_digit = -1
        for index, char in enumerate(line):
            if first_digit*last_digit > 1:
                #Found both digits
                break
            if first_digit < 0:
                if char.isdigit():
                    first_digit = int(char)
                digit_from_text = get_number_from_text(line[index:])
                if digit_from_text:
                    first_digit = digit_from_text
            if last_digit < 0:
                if line[(index+1) * -1].isdigit():
                    last_digit = int(line[(index+1) * -1])
                digit_from_text = get_number_from_text(line[len(line) -1 -index:])
                if digit_from_text:
                    last_digit = digit_from_text
        #print(line,first_digit,last_digit)
        total += int(f'{first_digit}{last_digit}')
    return total



def get_number_from_text(text: str) -> int:
    if text.startswith("zero"):
        return 0
    if text.startswith("one"):
        return 1
    if text.startswith("two"):
        return 2
    if text.startswith("three"):
        return 3
    if text.startswith("four"):
        return 4
    if text.startswith("five"):
        return 5
    if text.startswith("six"):
        return 6
    if text.startswith("seven"):
        return 7
    if text.startswith("eight"):
        return 8
    if text.startswith("nine"):
        return 9
    return None

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        lines = [x.replace("\n", "") for x in lines]
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
