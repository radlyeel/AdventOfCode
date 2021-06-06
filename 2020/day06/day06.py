#!/usr/bin/env python

# Part 1
# Good example for using Sets

# Part 2
# Replace Part 1 code with "anyone" function and add "everyone" function.

infile_name = 'input.txt'

def anyone():
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

# Here we use the question as a key into a dict whose value we increment
# When we finish with a group, we drop all elements whose value does not
# equal the number of people in the group.  We want a helper function for
# that.
def purge_group(gp, n):
    keys = []
    # Because the keys() method is a *view* of the dictionary
    for key in gp.keys():
        keys.append(key)
    for key in keys:
        if gp[key] != n:
            gp.pop(key)
    return gp

def everyone():
    sum = 0
    with open(infile_name, 'r') as fp:
        line = fp.readline()
        group = {}
        people_in_group = 0
        while (line):
            ll = line.strip()
            if len(ll) == 0:
                group = purge_group(group, people_in_group)
                sum += len(group)
                group = {}
                people_in_group = 0
            else:
                people_in_group += 1
                for i in range(len(ll)):
                    key = ll[i]
                    if not key in group.keys():
                        group[key] = 1
                    else:
                        group[key] += 1
            line = fp.readline()
        group = purge_group(group, people_in_group)
        sum += len(group)

    print(f"Total: {sum}")

#anyone()
everyone()
