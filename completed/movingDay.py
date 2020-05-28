import sys as sys

f = sys.stdin

lines = []
for line in f:
    lines.append([int(i) for i in line.split()])


n = lines[0][0]
V = lines[0][1]

i = 2
d = lines[1][0]*lines[1][1]*lines[1][2]

while i <= n:
    v = lines[i][0]*lines[i][1]*lines[i][2]
    if v > d:
        d = v
    i += 1

print(d - V)
