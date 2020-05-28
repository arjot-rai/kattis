import sys as sys

f = sys.stdin

strings = []

for l in f:
    strings.append(l)

str1 = strings[0].rstrip('\n')
str2 = strings[1].rstrip('\n')


result = "No"

if str1 == str2:
    result = "Yes"
elif str2 == str1[0:len(str1)-1] and str1[len(str1)-1].isdigit():
    result = "Yes"
elif str2 == str1[1:len(str1)] and str1[0].isdigit():
    result = "Yes"
else:
    str3 = str2.swapcase()

    if str1 == str3:
        result = "Yes"


print(result)
