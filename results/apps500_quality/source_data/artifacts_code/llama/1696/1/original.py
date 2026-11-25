import math
import sys
import math
input = sys.stdin.readline

def distance(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

def min_time(n, m, k, centers):
    def get_min_time(center):
        return max(math.ceil(distance(center, c) / 2) for c in centers)

    min_t = min(get_min_time(center) for center in centers)

    for _ in range(1, k):
        min_t += 1

    return min_t

n, m, k = map(int, input().split())
centers = []
for _ in range(k):
    x, y = map(int, input().split())
    centers.append((x, y))

ans = min_time(n, m, k, centers)
print(ans)
