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

rows = len(forest)
print(f'Forest is {rows} deep and {width} wide')

# Stepping distances
right = 3
down = 1

# Here we traverse the forest by stepping over and down, checking to see
# if a tree is present ('#'), and if it is, we simply count it.  The
# forest repeats to the right ad infinitum
x = 0
y = 0
hits = 0
while y < rows:
    print(f'x:y = {x},{y} spot[{y}][{x % width}] = {forest[y][x % width]}  Row = {forest[y]}')
    if forest[y][x % width] == '#':
        hits += 1
    x += right
    y += down

print(f'You hit {hits} trees on the way down.')
