#!/usr/bin/env python

# Part 1

# Edit this line to change source of data
infile_name = 'input.txt'

# A utility function for displaying a passport
def process_passport(pp):
    has = []
    for p in pp:
        parts = p.split(':')
        has.append(parts[0])
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    need = len(required)
    have = 0
    for key in required:
        if key in has:
            have += 1
    if have == need:
        return 1
    else:
        return 0

# Load input data into database
# This form automatically closes file
in_passport = True
passport = []
valid_count = 0
with open(infile_name, 'r') as fp:
    line = fp.readline()
    while line: 
        if len(line) == 1:
            if in_passport:
                valid_count += process_passport(passport)
            in_passport = False
            passport = []
        else:
            in_passport = True
            for kv in line.strip().split(' '):
                passport.append(kv)
        line = fp.readline()
    if in_passport:
        valid_count += process_passport(passport)

print (f'{valid_count} valid passports')
