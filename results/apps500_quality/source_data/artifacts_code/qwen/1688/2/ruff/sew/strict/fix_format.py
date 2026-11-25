import sys

input = sys.stdin.read
data = input().split()
n, a = int(data[0]), list(map(int, data[1:]))


def count_tracks(start):
    max_coolness, count = a[start], 1
    for i in range(1, n):
        track = (start + i) % n
        if a[track] < max_coolness // 2:
            return count
        max_coolness = max(max_coolness, a[track])
        count = count + 1
    return -1


results = [count_tracks(i) for i in range(n)]
print(" ".join(map(str, results)))
