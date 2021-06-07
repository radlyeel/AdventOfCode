#!/usr/bin/env python

# Part 1
# There are two interesting challenges in this problem:
#   - What is the best data structure for holding the rules?
#   - How to parse the English text into that data structure?

# Data structure:
#  The rules will be captured in a dictionary whose key is the type
#  of bag: "light red", "dark orange", etc.  Its value will be a 
#  possibly empty list of tuples (n, b}, where n is an integer and
#  b is a bag type (which can be used as a key)
#  Thus, the first and last rulesin the sample set will be
#  {"light red" : [(1, "bright white"), (2, "muted yellow")]}
#  {"dotted black" : []}

# Step 1: Parse the input and verify the data structure
# Step 1: Work out the processing,

infile_name = "input.txt"

rules = {}

with open(infile_name, 'r') as fp:
    line = fp.readline()

    while (line):
        ll = line.strip()
        if len(ll) > 0:

            # Ugly but effective
            bags = ll.find('bags', 0)
            bag_type = ll[0: bags - 1]
            contains = []

            # Find the beginning of the word "contain" and skip 8
            cnt = ll.find('contain', bags) + 8
            rest = ll[cnt:]
            if rest != 'no other bags.':
                # This bag contains other bags
                while rest:
                    parts = rest.split()
                    n = int(parts[0])

                    # To get the next bag type we have to find the first
                    # space in rest, then "bag"--note that finding "bags"
                    # is not reliable
                    inner_type_start = rest.find(' ', 0) + 1
                    inner_type_end = rest.find('bag', 0) - 1
                    inner_type = rest[inner_type_start : inner_type_end]
                    
                    # We have the count and type. store it and keep going
                    contains.append((n, inner_type))

                    rest_start = rest.find(',', 0)
                    if rest_start == -1:
                        break
                    rest = rest[rest_start + 2:]

            rules[bag_type] = contains

        line = fp.readline()


# Now that we have our rules, we need to scan all the bag types EXCEPT our
# own type, to see if it can contain directly or indirectly our type.  We
# could use a helper function "can_contain" to facilitate this.
def can_contain(container_bag, my_bag, nesting):
    contents = rules[container_bag]
    if not contents:
        return False
    found = False
    for packet in contents:
        if found or packet[1] == my_bag:
            return True
        else:
            found = can_contain(packet[1], my_bag, nesting + 1)
    return found

my_type = "shiny gold"
choices = 0
for bag_type in rules.keys():
    if (bag_type != my_type):
        can = can_contain(bag_type, my_type, 0)
        if can:
            choices += 1

print(f"You have {choices} choices.")


