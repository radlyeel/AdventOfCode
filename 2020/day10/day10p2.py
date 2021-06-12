#!/usr/bin/env python

infile_name = "short.txt"

# We will allow redefining the problem from a "max difference" of 3
max_difference = 3

def dump_possible(p):
    adapter_count = len(p)
    for i in range(adapter_count):
        if i == 0 or i == adapter_count - 1:
            print(f"({p[i]})", end="")
        else:
            print(f"{p[i]}", end="")
        if i != adapter_count - 1:
            print(", ", end="")
    print()

# Initialize the arry of joltage differences to all zeros
differences = []
for i in range(max_difference):
    differences.append(0)

adapters = []
with open(infile_name, 'r') as fp:
    line = fp.readline()
    while (line):
        if len(line) > 1:
            adapters.append(int(line))
        line = fp.readline()

adapters.sort()
target_rating = adapters[-1]
final_rating = target_rating + max_difference

possible = [0]
for current_adapter in range(len(adapters)):
    if current_adapter != 6:
        possible.append(adapters[current_adapter])

# Adjust for last adapter
possible.append(possible[-1] + max_difference)

dump_possible(possible)
