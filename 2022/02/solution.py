import os


def calculate_score(lines, score_map):
    score = 0
    for line in lines:
        line_score = score_map[line]
        score += line_score
    return score


def part_one(lines):
    win = 6
    lose = 0
    draw = 3
    score_map = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }
    return calculate_score(lines, score_map)


def part_two(lines):
    score_map = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }
    return calculate_score(lines, score_map)


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        lines = [x.replace("\n", "") for x in lines]
    print(f"Part One: {part_one(lines)}")
    print(f"Part Two: {part_two(lines)}")
