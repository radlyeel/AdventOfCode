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
        break
    sample_index += 1

# We now have our target to match
# Starting from the beginning, we accumulate contiguous values until one of
# two conditions occurs:
#  1.  Their sum matches: success
#  2.  Their sum exceeds the sample, in which case advance to the next
#      value and repeat
start = 0
while start < len(numbers):
    acc = 0
    end = start   # Accommodate the possibility of a single value -- possible?
    while acc < sample:
        acc += numbers[end]
        end += 1
    if acc == sample:
        break
    start += 1

if start == len(numbers):
    print("Failed")
else:
    last = end - 1
    print(f"start = {start}; finish = {last}")
    n_min = numbers[start]
    n_max = numbers[start]
    for n in numbers[start:end]:
        if n < n_min:
            n_min = n
        if n > n_max:
            n_max = n
    print(f"{n_min} + {n_max} = {n_min + n_max}")


