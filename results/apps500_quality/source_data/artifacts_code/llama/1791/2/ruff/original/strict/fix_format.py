s = input().strip()
n = len(s)

max_pile = 0

i = 0
while i < n:
    j = i + 1
    while j < n and s[i] == s[j]:
        j += 1
    if j - i > max_pile:
        max_pile = j - i
    i = j

print(max_pile)
