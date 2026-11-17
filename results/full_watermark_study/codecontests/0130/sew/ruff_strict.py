import sys

input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    val = (n * (n - 1) * (n - 2)) // 6
    arr, t = [[] for i in range(n)], [[] for i in range(n)]
    for i in range(0, n):
        a, b = map(int, input().split())
        a = a - 1
        b = b - 1
        arr[a].append(b)
        t[b].append(a)
    for i in range(0, n):
        for j in t[i]:
            val -= (len(t[i]) - 1) * (len(arr[j]) - 1)
    print(val)
