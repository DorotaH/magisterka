import sys

s = input().strip()

if len(s) == 1:
    print(s.upper())
else:
    print("C" + s[0].upper())
