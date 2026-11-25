from typing import List


def min_max_value(n: int, a: List[int], q: int, changes: List[List[int]]) -> List[int]:
    # Function to find the minimum max value for a given sequence
    def find_min_max(seq: List[int]) -> int:
        b = [seq[0]]
        c = [seq[0]]
        for i in range(1, len(seq)):
            b.append(min(b[-1], seq[i]))
            c.append(max(c[-1], seq[i]))
        return max(b[-1], c[-1])

    # Initial sequence
    result = [find_min_max(a)]

    # Apply each change and find the new minimum max value
    for l, r, x in changes:
        for i in range(l - 1, r):
            a[i] += x
        result.append(find_min_max(a))

    return result


# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
a = list(map(int, data[1:1 + n]))
q = int(data[1 + n])
changes = [list(map(int, data[2 + n + i * 3:5 + n + i * 3])) for i in range(q)]

# Get the results
results = min_max_value(n, a, q, changes)

# Print results
for result in results:
    print(result)
