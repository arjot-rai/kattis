enter = input()

i = 1
result = ""
result += enter[0]

while i<len(enter):
    if enter[i] != enter[i-1]:
        result += enter[i]
    i += 1

print(result)