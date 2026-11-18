import sys

input = lambda: sys.stdin.readline().rstrip()
read = lambda: list(map(int, input().split()))


def write(*args, sep="\n"):
    for i in args:
        sys.stdout.write(f"{i}" + sep)


INF = float("inf")
MOD = int(1e9 + 7)

for _ in range(int(input())):
    h, n = read()
    arr = [0] + list(read())

    if n == 1:
        write(0)
        continue

    ans = 0

    cur = h
    for i in range(1, n):
        if cur == arr[i]:
            continue
        if arr[i + 1] == arr[i] - 1:
            cur = arr[i] - 1
        else:
            ans += 1

    write(ans)
