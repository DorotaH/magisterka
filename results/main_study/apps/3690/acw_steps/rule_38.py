used = [0] * 121
h, m, s, t1, t2 = map(int, input().split())
h %= 12
t1 %= 12
t2 %= 12
t1 *= 5
t2 *= 5
used[5 * h] = 1
used[5 * h + 60] = 1
used[m] = 1
used[m + 60] = 1
used[s] = 1
used[60 + s] = 1
if t2 < t1:
    t1, t2 = t2, t1
t3 = t1 + 60
if sum(used[t1:t2]) == 0 or sum(used[t2:t3]) == 0:
    print("YES")
else:
    print("NO")