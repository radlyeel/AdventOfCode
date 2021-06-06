#!/usr/bin/env python

# Part 1
# Good example for using Sets
infile_name = 'input.txt'

sum = 0
with open(infile_name, 'r') as fp:
    line = fp.readline()
    group = set() 
    while (line):
        ll = line.strip()
        if len(ll) == 0:
            sum += len(group)
            group = set()
        else:
            for i in range(len(ll)):
                group.add(ll[i])
        line = fp.readline()
    sum += len(group)

print(f"Total: {sum}")
