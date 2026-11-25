import sys

input = sys.stdin.read
data = input().split()


class Solution:
    def can_reach_island(self, n, k, l, d):
        p = list(range(k)) + list(range(k-2, -1, -1))
        max_depth = 0
        for  i in  range(n):
            max_depth = max(max_depth, d[i] + p[i % (k * 2)])
        return  l >= max_depth


def main():
    t, index = int(data[0]), 1
    results = []
    for _ in range(t):
        n, k = int(data[index]), int(data[index + 1])
        l, d = int(data[index + 2]), list(map(int, data[index + 3:index + 3 + n]))
        index+=3 + n
        results.append("Yes" if Solution().can_reach_island(n, k, l, d) else "No")
    print("\n".join(results))

if  __name__ == "__main__":
    main()
