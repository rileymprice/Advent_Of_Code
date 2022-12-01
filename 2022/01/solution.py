import os

# def part_one():


def calculate_elves(lines):
    elves = []
    total = 0
    for line in lines:
        if line:
            total += int(line)
        else:
            elves.append(total)
            total = 0
    return elves


def part_one(lines):
    elves = calculate_elves(lines)
    return max(elves)


def part_two(lines):
    elves = calculate_elves(lines)
    top_three = []
    sorted = False
    for elf in elves:
        if len(top_three) < 3:
            top_three.append(elf)
        else:
            if not sorted:
                top_three.sort()
                sorted = True
            # print(top_three, elf)
            if elf > top_three[0]:
                top_three[0] = elf
                sorted = False
    return sum(top_three)

    # First try that worked

    # elves.sort()
    # top_elves = elves[-3:]
    # print(top_elves)
    # return sum(top_elves)


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        lines = [x.replace("\n", "") for x in lines]
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
