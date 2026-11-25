from sys import stdin, stdout

n = int(stdin.readline())
names = [[0, 0] for _ in range(n)]
p = [0] + list(map(int, stdin.readline().split()))

for i in range(1, 1 + n):
    f, s = stdin.readline().split()
    names[i - 1] = [len(f), len(s), i]

names.sort(key=lambda x: (-x[0], -x[1], x[2]))

used = [False] * (1 + n)
used[p[1]] = True
for i in range(2, 1 + n):
    if names[p[i - 2] - 1][0] <= names[p[i - 1] - 1][0]:
        used[p[i - 1]] = True

for i in range(1, 1 + n):
    used[i] = 1 if used[i] else 0
result = "YES" if all(i == 0 or used[i] for i in range(1, 1 + n)) else "NO"
stdout.write(result + "\n")
