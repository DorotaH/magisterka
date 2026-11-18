used = 121 * [0]
h, m, s, t1, t2 = map(int, input().split())
h %= 12
t1 %= 12
t2 %= 12
t1 *= 5
t2 *= 5
used[5 * h] = 1
used[60 + h * 5] = 1
used[m] = 1
used[60 + m] = 1
used[s] = 1
used[60 + s] = 1
if  t2 < t1:
    t1, t2=t2, t1
t3 = 60 + t1
if not (sum(used[t1:t2]) == 0 or sum(used[t2:t3]) == 0):
    print("NO")
else:
    print("YES")