import sys as sys

f = sys.stdin
for line in f:
    numbers = line.rstrip().split(" ")
    print(abs(int(numbers[0]) - int(numbers[1])))
