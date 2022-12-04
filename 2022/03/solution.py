import os
from itertools import zip_longest


def grouper(iterable_obj, count, fillvalue=None):
    args = [iter(iterable_obj)] * count
    return zip_longest(*args, fillvalue=fillvalue)


def num_convert(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


def part_one(lines):
    score = 0
    for ruck in lines:
        ruck_size = int(len(ruck) / 2)
        first = ruck[0:ruck_size]
        second = ruck[ruck_size:]
        for letter in first:
            if letter in second:
                score += num_convert(letter)
                break
    return score


def part_two(lines):
    groups = grouper(lines, 3)
    score = 0
    for group in groups:
        set_group = [set(x) for x in group]
        # print(set_group)
        intersection = set_group[0].intersection(set_group[1], set_group[2])
        letter = list(intersection)[0]
        score += num_convert(letter)
    return score


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        lines = [x.replace("\n", "") for x in lines]
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
