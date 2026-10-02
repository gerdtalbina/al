#!/usr/bin/python3

import random
def generate_dna(length=20):
    nucl = ['A', 'G', 'C', 'T']
    return ''.join(random.choice(nucl) for _ in range(lenght))
lenght = int(input('L:'))
dna = generate_dna(lenght)
print(f'DNA:{dna}')
