def find_kth_identifier(n, k, ids):
    total_ids = n * (n + 1) // 2
    if k <= n:
        return ids[k - 1]
    k -= n
    for i in range(n):
        if k <= 2 * (n - i):
            if k % 2 == 1:
                return ids[i]
            else:
                return ids[n - 1 - (k // 2)]
        k -= 2 * (n - i)


# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
ids = list(map(int, data[2:]))

# Find and print the k-th identifier
print(find_kth_identifier(n, k, ids))
