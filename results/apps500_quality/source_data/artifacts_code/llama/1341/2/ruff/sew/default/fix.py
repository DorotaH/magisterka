s = input()
t = input()
n = len(s)
curr_pos = 1

for i in range(n):
    if  t[i] == s[i]:
        curr_pos = curr_pos + 1

print(curr_pos)