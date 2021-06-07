#!/usr/bin/env python

infile_name = "input.txt"
preamble_length = 25

numbers = []
with open(infile_name, 'r') as fp:
    line = fp.readline()
    while (line):
        if len(line) > 1:
            n = int(line.strip())
            numbers.append(n)
        line = fp.readline()

sample_index = preamble_length
while sample_index != len(numbers):
    sample = numbers[sample_index]
    # print(f"Testing sample {sample_index} = {numbers[sample_index]}")
    found_match = False
    for i in range(preamble_length):
        # This loops i from 0 to preamble_length - 1
        for j in range(preamble_length - i - 1):
            # This loops j from 0 to preamble length - 1 - i
            ii = sample_index - preamble_length + i
            jj = sample_index - preamble_length + i + j + 1
            first = numbers[ii]
            second = numbers[jj]
            # print(f"n[{ii}] = {numbers[ii]}; n[{jj}] = {numbers[jj]};", end="")
            # print(f" sum = {first + second}")
            if sample == first + second:
                found_match = True
                #print(f"{sample} = {first} + {second}")
                break
        if found_match:
            break
    if not found_match:
        print(f"{sample}: No match found")
        break
    sample_index += 1

