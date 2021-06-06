#!/usr/bin/env python

# Part 1

# Edit this line to change source of data
infile_name = 'input.txt'

# Calculate the firstrow and length 
def region(reg, ch):
    half = int(reg[1]/2)
    if ch == 'F' or ch == 'L':
        return (reg[0], half)
    else:
        return (reg[0] + half, half)

def disp(block, spec):
    for i in range(len(spec)):
        ch = spec[i];
        block = region(block, ch)
    return block[0]

# Now process the data
with open(infile_name, 'r') as fp:
    seatpass = fp.readline().strip()
    max_seat_id = 0
    while seatpass:
        blk = (0, 128)
        sp = seatpass[:7]
        row = disp(blk, sp)
        blk = (0, 8)
        sp = seatpass[7:]
        col = disp(blk, sp)
        seat_id = row * 8 + col
        if seat_id > max_seat_id:
            max_seat_id = seat_id
        seatpass = fp.readline().strip()

print(f"Max seat id: {max_seat_id}")
