import sys

s = input().strip()

if not len(s) == 1:
    print(s[0].upper() + "C")
else:
    print(s.upper())
