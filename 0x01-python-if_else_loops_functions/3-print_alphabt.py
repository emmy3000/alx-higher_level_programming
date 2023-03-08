#!/usr/bin/python3
number = 97
for number in range(97, 123):
    if number == 101:
        continue
    if number == 113:
        continue
    alphabet = chr(number)
    print("{}".format(alphabet), end="")
