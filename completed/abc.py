import sys as sys

f = sys.stdin
c = []
for line in f:
    c.append(line)

b = c[1].strip('\n')
a = c[0].strip('\n').split()
a = [int(i) for i in a]
a.sort()

result = []
j = 0
for i in b:
    if i == "A":
        result.append(str(a[0]))
    elif i == "B":
        result.append(str(a[1]))
    else:
        result.append(str(a[2]))

result = ' '.join(result)
print(result)