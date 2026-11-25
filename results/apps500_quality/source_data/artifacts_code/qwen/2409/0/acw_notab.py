import sys
input = sys.stdin.read
data = input().split()


class Solution:
    def can_reach_island(self, n, k, l, d):
        p = list(range(k - 2, -1, -1)) + list(range(k))
        max_depth = 0
        for i in range(n):
            max_depth = max(max_depth, d[i] + p[i % (2 * k)])
        return max_depth <= l


def main():
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        k = int(data[1 + index])
        l = int(data[2 + index])
        d = list(map(int, data[3 + index:3 + index + n]))
        index += 3 + n
        results.append("Yes" if Solution().can_reach_island(n, k, l, d) else "No")
    print("\n".join(results))


if __name__ == "__main__":
    main()
