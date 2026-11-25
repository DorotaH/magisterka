
s = input().strip()

max_pile_size = 0

for  i in  range(0, len(s)):
    for j in range(2 + i, len(s), 2):
        if s[j] != s[i]:
            break
        pile_size = j - i
        k = i + 2 * pile_size
        while  k<len(s) and  s[j] == s[k]:
            pile_size = pile_size + 1
            k = k + 1
        max_pile_size = max(max_pile_size, pile_size)

print(max_pile_size)
