#!/usr/bin/env python
import re   # Added for checking hair color

# Compile once, match often
rgb = re.compile('\#[0-9a-f]{6}')
pid = re.compile('[0-9]{9}')

# Part 1

# Edit this line to change source of data
infile_name = 'input.txt'

# A utility function for displaying a passport
def process_passport(pp):
    # Make a dictionary out of the passport, and store the keys in has
    pp_dict = {}
    for p in pp:
        parts = p.split(':')
        pp_dict[parts[0]] = parts[1]
    keys = ['cid', 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    need = len(keys)
    have = 0
    valid = True

    # First, make sure the keys are all valid
    for key in pp_dict:
        if key not in keys:
            valid = False

    # Now validate each key
    for key in keys:
        if key in pp_dict or key == 'cid':
            have += 1
        if key in pp_dict:
            value = pp_dict[key]
            if key == 'byr':
                if int(value) < 1920 or int(value) > 2002:
                    valid = False
            elif key == 'iyr':
                if int(value) < 2010 or int(value) > 2020:
                    valid = False
            elif key == 'eyr':
                if int(value) < 2020 or int(value) > 2030:
                    valid = False
            elif key == 'hgt':
                # separate value from units
                unit = value[-2:]
                h = value[:-2]
                if unit == 'cm':
                    if int(h) < 150 or int(h) > 193:
                        valid = False
                elif unit == 'in':
                    if int(h) < 59 or int(h) > 76:
                        valid = False
                else:
                    # Invalid unit
                    valid = False
            elif key == 'hcl':
                if len(value) != 7 or not rgb.match(value):
                    valid = False
            elif key == 'ecl':
                if not value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    valid = False
            elif key == 'pid':
                if len(value) != 9 or not pid.match(value):
                    valid = False
            else: # cid is ignored
                pass

    if valid and have >= need:
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
