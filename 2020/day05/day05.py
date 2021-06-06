#!/usr/bin/env python

# Part 2
# Build a list of all seats.  Ignore missing seats at the low and high end of
# the range.  Find the missing seat

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
all_seats = []
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
        all_seats.append(seat_id)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
        seatpass = fp.readline().strip()

# Scan for missing seat
for this_seat in range(max_seat_id):
    if not this_seat in all_seats \
       and this_seat + 1 in all_seats \
       and this_seat - 1 in all_seats:
        print(f"Your seat is {this_seat}")
        break;
