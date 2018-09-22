# Written by Daniel Hocking for COMP4418

'''
Assignment 1
CNF file generator
Expects a file prefix
Expects three integer inputs: n-sat, number of variables,
    number of clauses
'''

import sys
from random import sample, choice, seed
import csv

files_to_gen = list()
if len(sys.argv) == 2:
    try:
        with open(sys.argv[1], 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            files_to_gen = [l for l in csv_reader]
    except FileNotFoundError:
        print('Input file not found, giving up.')
        sys.exit()

if len(files_to_gen) == 0:    
    try:
        file_prefix = input('Which file prefix do you want to use? ')
    except ValueError:
        print('Incorrect input, giving up.')
        sys.exit()

    try:
        seed_num = int(input('Enter the seed number to use '))
        if seed_num < 0:
            raise ValueError
        n_sat = int(input('Enter the n-sat number to use '))
        if n_sat < 1:
            raise ValueError
        num_vars = int(input('Enter the number of variables to use '))
        if num_vars < 1:
            raise ValueError
        num_clauses = int(input('Enter the number of clauses to use '))
        if num_clauses < 1:
            raise ValueError
    except ValueError:
        print('Incorrect input, giving up.')
        sys.exit()
    files_to_gen.append([file_prefix, seed_num, n_sat, num_vars, num_clauses])


for file in files_to_gen:
    try:
        file_prefix, seed_num, n_sat, num_vars, num_clauses = file
        seed_num, n_sat, num_vars, num_clauses = int(seed_num), int(n_sat), int(num_vars), int(num_clauses)
        input_file = f'{file_prefix}_{n_sat}_{num_vars}_{num_clauses}.cnf'
        not_neg = [True, False]
        variables = ['-'+str(i + 1) for i in range(num_vars)]
        seed(seed_num)

        with open(input_file, 'w') as inf:
            inf.write(f'p cnf {num_vars} {num_clauses}\n')
            for i in range(num_clauses):
                clause_vars = sample(variables, n_sat)
                for i in range(n_sat):
                    if choice(not_neg):
                        clause_vars[i] = clause_vars[i].strip('-')
                    
                for var in clause_vars:
                    inf.write(var+' ')
                inf.write('0\n')         

    except FileNotFoundError:
        print('Input file not found, giving up.')
        sys.exit()
