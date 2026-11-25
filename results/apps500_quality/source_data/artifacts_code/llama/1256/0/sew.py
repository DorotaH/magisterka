s = input()

s = list(s)

i = 0
while i<len(s)-1:
    if s[i] == '+':
        continue
    elif s[i] < s[i + 1]:
        s[i], s[i + 1] = s[i + 1], s[i]
        while  i < len(s) - 1 and  s[i] == s[i + 1]:
            i = i + 1
            s[i], s[1 + i] = s[1 + i], s[i]
    i = i + 1

print(''.join(s))