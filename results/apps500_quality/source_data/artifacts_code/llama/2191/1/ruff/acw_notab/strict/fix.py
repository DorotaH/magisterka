n = int(input())
s = input()

sets = []
count = 0
win_streak = 0
for i in range(n):
    if s[i] == '?':
        sets.append(count)
        count = 0
        win_streak = 0
    elif s[i] == '0':
        win_streak = 0
        count += 1
        sets.append(count)
        count = 1 if count > win_streak else 0
    elif s[i] == '1':
        win_streak = 0
        count = 0
        sets.append(count)

if count > win_streak:
    sets.append(count)

result = [0] * n
for i in range(1, 1 + n):
    result[n - i] = max(sets) - (n - i - 1) // i

print(*result)
