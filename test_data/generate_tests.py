import sys
from random import sample, choice, seed

names = list()
with open('names.txt, 'r') as names_files:
    names = [l for l in names_files]

print(names)
