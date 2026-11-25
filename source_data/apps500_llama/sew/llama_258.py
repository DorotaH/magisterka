import sys

s = sys.stdin.readline().strip()
print(f"{s[0]}{''.join('18' if 17 == i else '' for i in range(1, len(s) - 2))}{s[-1]}")