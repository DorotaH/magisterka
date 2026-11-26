import sys

s = input().strip()
n = len(s)

max_pile = 0

i = 0
while n > i:
    j = i + 1
    while n > j and s[i] == s[j]:
        j = j + 1
    if j - i > max_pile:
        max_pile = j - i
    i = j

print(max_pile)
