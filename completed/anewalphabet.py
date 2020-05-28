import sys as sys

dict = {
    'a': '@',
    'b': '8',
    'c': '(',
    'd': '|)',
    'e': '3',
    'f': '#',
    'g': '6',
    'h': '[-]',
    'i': '|',
    'j': '_|',
    'k': '|<',
    'l': '1',
    'm': '[]\\/[]',
    'n': '[]\\[]',
    'o': '0',
    'p': '|D',
    'q': '(,)',
    'r': '|Z',
    's': '$',
    't': "']['",
    'u': '|_|',
    'v': '\\/',
    'w': '\\/\\/',
    'x': '}{',
    'y': '`/',
    'z': '2'
}

string = input()
output = ""

i = 0
while i < len(string):

    if string[i].isalpha():
        output += dict[string[i].lower()]
    else:
        output += string[i]

    i += 1
print(output)