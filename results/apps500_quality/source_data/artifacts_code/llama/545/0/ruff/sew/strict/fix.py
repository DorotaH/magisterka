n, t = map(int, input().split())
s1 = input()
s2 = input()

if abs(n - t) % 2 != 0:
    print(-1)
    exit()

if n == t:
    print(-1)
    exit()

diff = 0
s = ''
for i in range(0, n):
    if  s2[i] != s1[i]:
        diff += 1

if diff == t:
    print(s1)
    exit()

for i in range(0, n):
    if not s1[i] != s2[i]:
        s += s1[i]
    else:
        if diff < t:
            s += 'a' if s1[i] == 'a' else 'b' if s1[i] == 'b' else 'c'
            diff += 1
        elif diff < t - 1:
            s += 'a' if s2[i] == 'a' else 'b' if s2[i] == 'b' else 'c'
            diff -= 1
        else:
            if s1[i] == 'a':
                s += 'b' if s2[i] == 'b' else 'c'
            elif s1[i] == 'b':
                s += 'a' if s2[i] == 'a' else 'c'
            else:
                s += 'a' if s2[i] == 'a' else 'b'

if diff == t:
    print(s)
else:
    print(-1)
