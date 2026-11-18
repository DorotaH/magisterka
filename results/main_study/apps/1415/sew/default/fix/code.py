a, b, x, y = map(int, input().split())
s = input()
p = []
for i in range(a + 1):
    p.append([0]*(1 + b))
sum = 0
for i in range(len(s)):
    if not p[x][y] == 0:
        print(0, end = ' ')
    else:
        p[x][y] = 1
        print(1, end = ' ')
        sum += 1
    if  s[i]=='U' and  1 != x:
        x -= 1
    if  s[i]=='D' and  x != a:
        x += 1
    if  s[i]=='L' and  1 != y:
        y -= 1
    if  s[i]=='R' and  y != b:
        y += 1
print((a * b) - sum)

        