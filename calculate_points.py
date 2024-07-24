import fileinput
import re

total_points = 0
for line in fileinput.input():
    sections = line.split(":")[1].split("|")
    winning_numbers: set[int] = set(map(int, re.findall(r"(\d+)", sections[0])))
    player_numbers: set[int] = set(map(int, re.findall(r"(\d+)", sections[1])))

    matched_numbers = player_numbers.intersection(winning_numbers)
    if matched_numbers:
        total_points += 2 ** (len(matched_numbers) - 1)

print(total_points)
