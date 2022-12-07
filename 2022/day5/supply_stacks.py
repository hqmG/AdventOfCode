# Modules
import os
import re

def get_stacks(supplies: str) -> dict:
    stacks = {int(stack): [] for stack in re.findall('\d+', supplies.rsplit('\n', 1)[-1])}
    for level in reversed(supplies.rsplit('\n', 1)[0].split('\n')):
        for index, crate in enumerate(level.replace('    ', ' ').split(' ')):
            if crate != '':
                stacks[index+1].append(crate[1])
    return stacks

def get_receipt(instructions: str) -> list:
    return [int(instruction) for instruction in re.findall('\d+', instructions)]

def move1(stacks: dict, amount: int, from_stack: int, to_stack: int) -> dict:
    for _ in range(amount):
        crate = stacks[from_stack].pop()
        stacks[to_stack].append(crate)
    return stacks

def move2(stacks: dict, amount: int, from_stack: int, to_stack: int) -> dict:
    crates = stacks[from_stack][-amount:]
    stacks[from_stack] = stacks[from_stack][:-amount]
    stacks[to_stack].extend(crates)
    return stacks
    
with open(f'{os.getcwd()}/2022/day5/input.txt', 'r') as f:
    stacks = get_stacks(re.split('\n\n', f.read())[0])
with open(f'{os.getcwd()}/2022/day5/input.txt', 'r') as f:
    for instructions in re.split('\n\n', f.read())[1].split('\n'):
        crates, from_stack, to_stack = get_receipt(instructions)
        stacks = move1(stacks, crates, from_stack, to_stack)
    print(''.join([crates[-1] for crates in stacks.values()]))

with open(f'{os.getcwd()}/2022/day5/input.txt', 'r') as f:
    stacks = get_stacks(re.split('\n\n', f.read())[0])
with open(f'{os.getcwd()}/2022/day5/input.txt', 'r') as f:
    for instructions in re.split('\n\n', f.read())[1].split('\n'):
        crates, from_stack, to_stack = get_receipt(instructions)
        stacks = move2(stacks, crates, from_stack, to_stack)
    print(''.join([crates[-1] for crates in stacks.values()]))