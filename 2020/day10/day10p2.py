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

# To complete part 2, we need a helper function that will take a starting
# index and compute a list of the possible tail chains.  Thus, in the
# short version, tails(dapters, 10) will return
#    [11 12, 15, 16, 19] and [12, 15, 16, 19]
def tails(ll, n):
    tail = []
    target = ll[-1]
    i = n
    while i < len(ll):
# Adjust for last adapter
possible.append(possible[-1] + max_difference)

dump_possible(possible)
