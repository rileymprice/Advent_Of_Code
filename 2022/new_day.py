import os

day_number = input("What is the day number you are working on?")

# Create folder
os.mkdir(day_number)
os.chdir(day_number)

# Create input file
with open("input.txt", "w") as input_file:
    pass

# Create solution file
with open("solution.py", "w") as solution_file:
    solution_mock = """import os

def part_one(lines):
    pass


def part_two(lines):
    pass


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        lines = [x.replace('\\n', "") for x in lines]
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
"""
    solution_file.write(solution_mock)
