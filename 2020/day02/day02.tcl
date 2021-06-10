# Problem:
# Reference: https://adventofcode.com/2020/day/2
# Part 1
# Examine a list of passwords to determine how may were valid when they were set.
# Datbase structure: each line is in the following format
# m-n c: pppp...
#   Where
#     m is the minimum number of occurrences of c in pppp...
#     n is the maximum number of occurrences of c in pppp...
#     c is a case-sensitive character in the range a..z
#     pppp... is a password of arbitrary length
# Usage: tclsh day02.tcl <filename>

# Function definitions
# Return the number of occurrences of character ch in string str
proc occurrences {ch str} {
    set n 0
    foreach test_ch [split $str ""] {
        if {$ch == $test_ch} {
            incr n
        }
    }
    return $n
}

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
set all_text [read $inf]
set lines [split $all_text "\n"]

# Part 1: scan the input file for valid passwords
set passed 0
foreach line $lines {
    if {$line != ""} {
        set parts [split $line " "]
        set limits [split [lindex $parts 0] "-"]
        set min [lindex $limits 0]
        set max [lindex $limits 1]
        set ch [string index [lindex $parts 1] 0]
        set pwd [lindex $parts 2]
        set occ [occurrences $ch $pwd]
        if {$occ >= $min && $occ <= $max} {
            incr passed
        }
    }
}
puts "Part 1: $passed passwords are okay"

# Part 1: scan the input file for valid passwords
set passed 0
foreach line $lines {
    if {$line != ""} {
        set parts [split $line " "]
        set limits [split [lindex $parts 0] "-"]
        set first [lindex $limits 0]
        set second [lindex $limits 1]
        set ch [string index [lindex $parts 1] 0]
        set pwd [lindex $parts 2]
        # Check to see if exactly one of the indexed characters is a match
        set first_match 0
        if {$ch == [string index $pwd [expr $first - 1]]} {
            set first_match 1
        }
        set second_match 0
        if {$ch == [string index $pwd [expr $second - 1]]} {
            set second_match 1
        }
        if {1 == [expr $first_match + $second_match]} {
            incr passed
        }
    }
}
puts "Part 2: $passed passwords are okay"
