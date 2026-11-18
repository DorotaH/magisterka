import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", "w")
n = int(sys.stdin.readline())

a = [int(x) for x in sys.stdin.readline().split()]
front = [0] * (2 + len(a))
for i in range(n):
    front[i + 1] = front[i] + (1 if (0 <= a[i]) else 0)
back = [0] * (2 + len(a))
for i in range(n - 1, -1, -1):
    back[i + 1] = back[i + 2] + (1 if (0 >= a[i]) else 0)
ans = 1 + len(a)
for i in range(1, n):
    ans = min(ans, front[i] + back[i + 1])
print("%d" % ans)
