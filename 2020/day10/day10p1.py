#!/usr/bin/env python

infile_name = "long.txt"

# We will allow redefining the problem from a "max difference" of 3
max_difference = 3

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

current_joltage = 0
for current_adapter in range(len(adapters)):
    difference = adapters[current_adapter] - current_joltage
    differences[difference - 1] += 1
    current_joltage += difference
    #print(f"{current_adapter}: {current_joltage} ({difference})")

# Adjust for last adapter
differences[max_difference - 1] += 1
for i in range(len(differences)):
    val = differences[i]
    print(f"differences[{i}]: {val}")

print(f"Product of 1-jolt and 3-jolt differences = {differences[0] * differences[2]}")

