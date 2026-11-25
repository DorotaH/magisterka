import sys

n = int(sys.stdin.readline())
arr = [i + 1 for i in range(2 * n)]
arr[::2], arr[1::2] = arr[n:], arr[:n]
print(*arr)
