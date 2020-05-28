import sys as sys
# import time

# def check(s):
#
#     s = sorted(s, key=len, reverse=True)
#
#     while len(s) > 0:
#         l = s.pop()
#         for i in s:
#             if len(l) <= len(i):
#                 if l in i:
#                     return True
#
#     return False

# seconds = time.time()
f = sys.stdin
# numbers = ['2\n', '3\n', '911\n', '97625999\n', '91125426\n', '5\n', '113\n', '12340\n', '123440\n', '12345\n', '98346\n']

numbers = []

for line in f:
    numbers.append(line.strip("\n"))
# numbers = set(numbers)

length = len(numbers)
t = int(numbers[0])

i = 1
while t != 0:

    n = int(numbers[i])
    i += 1
    found = False
    sub = sorted(numbers[i: i+n], key=len, reverse=True)
    s = set()
    for num in sub:
        if num in s:
            found = True
            break
        for j in range(1, len(num) + 1):
            s.add(num[:j])


    # sub.clear()

    if found:
        print("NO")
    else:
        print("YES")

    i += n
    t -= 1

# print(time.time() - seconds)