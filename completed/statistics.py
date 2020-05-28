import sys as sys

f = sys.stdin

case = 0
for line in f:
    line = line.split(' ')
    lines = [int(i) for i in line]
    n = lines[0]
    i = 2
    min = max = lines[1]

    while i < len(lines):
        if lines[i] < min:
            min = lines[i]
        elif lines[i] > max:
            max = lines[i]
        i += 1

    print("Case ", case + 1, ": ", min, ' ', max, ' ', max-min, sep="", end="\n")
    case += 1
