import os
from typing import List

def get_priority(item: str) -> int:
    return ord(item)-96 if item.islower() else ord(item)-38

def get_doublets(rucksack: str) -> List[str]:
    return list(set([item for item in rucksack[:len(rucksack)//2] if item in rucksack[len(rucksack)//2:]]))

def get_badge(rucksacks: List[str]):
    return list(set([item for item in rucksacks[0] if item in rucksacks[1] and item in rucksacks[2]]))

compartment = []
with open(f'{os.getcwd()}/2022/day3/input.txt', 'r') as f:
    for rucksack in f.readlines():
        compartment.extend([get_priority(item) for item in get_doublets(rucksack.replace('\n', ''))])
print(sum(compartment))

compartment = []
with open(f'{os.getcwd()}/2022/day3/input.txt', 'r') as f:
    rucksacks = []
    for rucksack in f.readlines():
        rucksacks.append(rucksack.replace('\n', ''))
        if len(rucksacks) == 3:
            compartment.extend([get_priority(item) for item in get_badge(rucksacks)])
            rucksacks = []
print(sum(compartment))