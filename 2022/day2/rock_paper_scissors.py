import os
import re

choice1 = {
    'A X': 'R R',
    'A Y': 'R P',
    'A Z': 'R S',
    'B X': 'P R',
    'B Y': 'P P',
    'B Z': 'P S',
    'C X': 'S R',
    'C Y': 'S P',
    'C Z': 'S S'
}
choice2 = {
    'A X': 'R S',
    'A Y': 'R R',
    'A Z': 'R P',
    'B X': 'P R',
    'B Y': 'P P',
    'B Z': 'P S',
    'C X': 'S P',
    'C Y': 'S S',
    'C Z': 'S R'
}
outcome = {
    'R P': 6+2,
    'P S': 6+3,
    'S R': 6+1,
    'R R': 3+1,
    'P P': 3+2,
    'S S': 3+3,
    'R S': 0+3,
    'P R': 0+1,
    'S P': 0+2
}
with open(f'{os.getcwd()}/2022/day2/input.txt', 'r') as f:
    score1 = sum([outcome[choice1[round]] for round in re.split('\n', f.read())])
with open(f'{os.getcwd()}/2022/day2/input.txt', 'r') as f:
    score2 = sum([outcome[choice2[round]] for round in re.split('\n', f.read())])
print(score1, score2)