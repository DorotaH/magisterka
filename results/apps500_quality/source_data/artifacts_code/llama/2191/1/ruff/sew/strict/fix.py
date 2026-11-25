n = int(input())
s = input()

sets = list()
count = win_streak = 0
for i in range(0, n):
    if  s[i]=='?':
        sets.append(count)
        count = win_streak = 0
    elif  s[i] == '0':
        win_streak = 0
        count += 1
        if not count > win_streak:
            sets.append(count)
            count = 0
        else:
            sets.append(count)
            count = 1
    elif  s[i] == '1':
        win_streak = count = 0
        sets.append(count)

if win_streak < count:
    sets.append(count)

result = [0] * n
for i in range(1, 1 + n):
    result[n-i]=max(sets)-(n - i - 1) // i

print(*result)
