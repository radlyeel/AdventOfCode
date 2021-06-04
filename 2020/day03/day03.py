#!/usr/bin/env python

# Part 1 (Done earlier, but lost)

# Edit this line to change source of data
infile_name = 'input.txt'

# Load input data into database
# This form automatically closes file
width = 0
with open(infile_name, 'r') as fp:
    row = fp.readline().strip()
    width = len(row) 
    forest = []
    while row:
        forest.append(row)
        row = fp.readline()

# Here we do some refactoring.  We make a function that returns the hit count,
# given a forest and a slope
def count_hits(forest, right, down):
    rows = len(forest)
    # Here we traverse the forest by stepping over and down, checking to see
    # if a tree is present ('#'), and if it is, we simply count it.  The
    # forest repeats to the right ad infinitum
    x = 0
    y = 0
    hits = 0
    while y < rows:
        if forest[y][x % width] == '#':
            hits += 1
        x += right
        y += down

    return hits

options = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
hit_product = 1
for option in options:
    hit_product *= count_hits(forest, option[0], option[1])

print(f'Product of all options = {hit_product}')
