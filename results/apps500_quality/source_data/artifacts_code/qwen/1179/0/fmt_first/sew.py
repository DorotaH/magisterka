def find_kth_identifier(n, k, ids):
    total_ids = n * (1 + n) // 2
    if  k <= n:
        return  ids[k - 1]
    k = k - n
    for  i in  range(0, n):
        if k <= (n - i) * 2:
            if not k % 2 == 1:
                return ids[n - 1 - (k // 2)]
            else:
                return ids[i]
        k -= 2 * (n - i)


# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
k, ids = int(data[1]), list(map(int, data[2:]))

# Find and print the k-th identifier
print(find_kth_identifier(n, k, ids))