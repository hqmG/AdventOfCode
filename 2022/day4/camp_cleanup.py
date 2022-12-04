import os
from typing import List

def get_sections(sections: str) -> List[int]:
    return [section for section in range(int(sections.split('-')[0]), int(sections.split('-')[1])+1)]

def reconsider(pair: List[int]) -> bool:
    return all(section in pair[0] for section in pair[1]) or all(section in pair[1] for section in pair[0])

def overlap(pair: List[int]) -> bool:
    return any([section for section in pair[0] if section in pair[1]])

with open(f'{os.getcwd()}/2022/day4/input.txt', 'r') as f:
    print(len([pair for pair in f.readlines() if reconsider([get_sections(section) for section in pair.replace('\n', '').split(',')])]))

with open(f'{os.getcwd()}/2022/day4/input.txt', 'r') as f:
    print(len([pair for pair in f.readlines() if overlap([get_sections(section) for section in pair.replace('\n', '').split(',')])]))