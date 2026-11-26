from typing import List
import heapq


def find_kth_statistic(
    n: int, s: int, m: int, k: int, a: List[int], segments: List[List[int]]
) -> int:
    # Convert segments to a min-heap based on the number of elements they cover
    heap = []
    for l, r in segments:
        length = r - l + 1
        heapq.heappush(heap, (length, l, r))

    # Extract elements from the segments to form the multiset
    covered_elements = []
    while heap:
        length, l, r = heapq.heappop(heap)
        if length == 0:
            continue
        covered_elements.extend(a[i] for i in range(l - 1, r))
        covered_elements.sort()

    # If the multiset has less than k elements, return -1
    if len(covered_elements) < k:
        return -1

    # Return the k-th order statistic
    return covered_elements[k - 1]


# Read input
n, s, m, k = map(int, input().split())
a = list(map(int, input().split()))
segments = [list(map(int, input().split())) for _ in range(s)]

# Find the k-th order statistic
result = find_kth_statistic(n, s, m, k, a, segments)

# Print the result
print(result)
