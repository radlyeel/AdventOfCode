# Problem:
# Reference: https://adventofcode.com/2020/day/1
# Part 1
# Given a sequence of numbers as a text file (input.txt or example.txt), find
# the pair that sums to 2020 and multiply them together to find the answer
# For the example.txt file, the answer is 514579.
# Part 2
# Like Part 1, but with three numbers

# Usage: tclsh day01.tcl <filename>


# Check command line
set fname ""
if { $argc != 1 } {
    puts "Usage:  tclsh day01.tcl <filename>"
    exit
} else {
    set fname [lindex $argv 0]
}

# Open input file if possible
if [catch {set inf [open $fname r] } errmsg] {
    error "Can't open $fname: $errmsg"
    exit
}

# Now, with the preliminaries done, we can finally do the work
set values [read $inf]

# Part 1: find two 
set done 0
set len [llength $values]
for {set i 0} {$i < $len} {incr i} {
    set first [lindex $values $i]
    for {set j [expr {$i + 1}]} {$j < $len} {incr j} {
        set second [lindex $values $j]
        if {2020 == [expr {$first + $second}]} {
            puts "Part 1 Answer; $first * $second = [expr {$first * $second}]"
            set done 1
        }
        if {$done} {break}
    }
    if {$done} {break}
}

# Part 2: find three
set done 0
for {set i 0} {$i < $len} {incr i} {
    set first [lindex $values $i]
    for {set j 0} {$j < $len} {incr j} {
        set second [lindex $values $j]
        for {set k 0} {$k < $len} {incr k} {
            set third [lindex $values $k]
            if {2020 == [expr {$first + $second + $third}]} {
                # Exclude re-using  the same number
                if { $i != $j && $i != $k && $j != $k} {
                    puts "Part 2 Answer; $first * $second * $third = [expr {$first * $second *$third}]"
                    set done 1
                }
            }
            if {$done} {break}
        }
        if {$done} {break}
    }
    if {$done} {break}
}

