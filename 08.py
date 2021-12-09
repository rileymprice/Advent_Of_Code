input_data = {}
input_path = "input/08.txt"
with open(input_path, "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        query, result = line.split(" | ")
        input_data[query] = result


def part_one(input_data):
    count = 0
    for result in input_data.values():
        digits = result.split(" ")
        for digit in digits:
            digit = digit.strip()
            # print(digit, len(digit))
            if len(digit) in [2, 3, 4, 7]:
                count += 1
    return count


print(f"Part One: {part_one(input_data)}")
