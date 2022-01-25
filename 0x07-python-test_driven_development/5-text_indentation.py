#!/usr/bin/python3
"""
Fuction that prints new line after some chars
Chars: '.', '?' and ':'
text: has to be an string
"""


from hashlib import new


def text_indentation(text):
    """Function that insert new lines"""
    if type(text) != str:
        raise TypeError("text must be a string")
    temp = ""
    new = []
    new2 = []
    i = 0
    a = 0
    j = 0
    temp = str(text.splitlines())
    for i in range(len(temp)):
        if temp[i] == ":" or temp[i] == "?" or temp[i] == ".":
            new.append(text[a:i - 1])
            a = i
            i = i + 1
        else:
            i = i + 1
    if a < len(temp):
        new.append(text[a: i - 1])
    while j < len(new):
        new2.append(new[j].strip())
        j = j + 1
    for n in new2:
        print("{:s}".format(n))
        print()
