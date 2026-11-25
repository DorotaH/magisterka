from  sys import  stdin, stdout

n=int(stdin.readline())
names, p = [[0, 0] for _ in range(n)], [0] + list(map(int, stdin.readline().split()))

for i in range(1, 1 + n):
    f, s=stdin.readline().split()
    names[i-1]=[len(f), len(s), i]

names.sort(key=lambda x: (-x[0], -x[1], x[2]))

used=[False]*(n + 1)
used[p[1]]=True
for i in range(2, 1 + n):
    if names[p[i - 1] - 1][0] >= names[p[i - 2] - 1][0]:
        used[p[i - 1]] = True

for i in range(1, 1 + n):
    if used[i]:
        used[i] = 1
    else:
        used[i] = 0

result = "YES" if all(i == 0 or used[i] for i in range(1, n + 1)) else "NO"
stdout.write(result+"\n")
