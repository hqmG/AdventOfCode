import os
import re

with open(f'{os.getcwd()}/2022/day1/input.txt', 'r') as f:
    elves = re.split('\n\n', f.read())
    for index, elf in enumerate(elves):
        elves[index] = sum([int(calories) for calories in re.split('\n', elf)])
    print(max(elves))