#!/usr/bin/python3
from math import gcd
holder = []
fileOpen = open('factors', 'r')
data = fileOpen.readlines()
temp = ([s.replace('\n', '') for s in data])
fileOpen.close
for place in data:
    holder.append(int(place))
# up till here i have moved the file content into an integer list.
holder.sort()
for place in holder:
    first = 1
    while first * second != place:
        temp = gcd(first, place)
        if temp == 1:
            first += 1
        second = int(place / temp)
    print("{}  {}".format(first, second))
