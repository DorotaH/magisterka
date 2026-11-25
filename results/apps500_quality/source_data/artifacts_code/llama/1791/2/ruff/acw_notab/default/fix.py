
s = input().strip()
n = len(s)

max_pile = 0

i = 0
while i < n:
    j = i + 1
    while n > j and s[i] == s[j]:
        j += 1
    max_pile = max(max_pile, j - i)
    i = j

print(max_pile)
