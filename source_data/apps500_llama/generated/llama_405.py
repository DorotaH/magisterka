s, t = input(), input()
n, curr_pos = len(s), 1

for i in range(n):
    if s[i] == t[i]:
        curr_pos += 1

print(curr_pos)
