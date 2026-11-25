import sys

s = input().strip()

if not (s[0] == 'B' and s[-1] == 'B'):
    print(1)
else:
    print(0)