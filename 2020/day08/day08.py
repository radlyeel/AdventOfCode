#!/usr/bin/env python

# Part 1

infile_name = "input.txt"

program = []

with open(infile_name, 'r') as fp:
    line = fp.readline()

    while (line):
        ll = line.strip()
        if len(ll) > 0:
            parts = line.split()
            program.append([parts, 0])
        line = fp.readline()


change_point = 1
completed = False

while not completed and change_point < len(program):
    opc = program[change_point][0][0]
    if opc == 'nop' or opc == 'jmp':
        # Found something to change
        if opc == 'nop':
            program[change_point][0][0] = 'jmp'
        else:
            program[change_point][0][0] = 'nop'

        # Now run the program and see if it completes
        pc = 0
        acc = 0
        for step in program:
            step[1] = 0

        while True:
            step = program[pc]
            if step[1] == 1:
                # We've been here before
                break
            program[pc][1] += 1
            op = step[0]
            if op[0] == "acc":
                acc += int(op[1])
                pc += 1
            elif op[0] == "jmp":
                pc += int(op[1])
            elif op[0] == "nop":
                pc += 1
            else:
                print("Error: invalid op code")
                break

            if pc == len(program):
                print(f"After changing opcode at {change_point}")
                print(f"  program terminated correctly with acc = {acc}.")
                completed = True
                break

            if pc > len(program):
                print(f"Illegal PC; acc = {acc}.")
                break

        if completed:
            # We found our fix
            break

        # We changed something, we'd better change it back
        program[change_point][0][0] = opc
        change_point += 1

    else:
        # Keep looking
        change_point += 1

    
