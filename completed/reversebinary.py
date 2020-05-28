import sys as sys

f = sys.stdin
for line in f:
    n = int(line)

bin_n = bin(n)
n_reverse = 0

for i in range(2, len(bin_n)):
    #print(n_reverse)
    n_reverse += int(bin_n[i])*pow(2,int(i-2))

print(n_reverse)