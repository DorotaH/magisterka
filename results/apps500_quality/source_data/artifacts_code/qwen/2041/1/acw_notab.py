from typing import List
import heapq


def optimal_subsequence(a: List[int], k: int) -> List[int]:
    # Extract k elements with the largest sum
    max_heap = [(-x, i) for i, x in enumerate(a)]
    heapq.heapify(max_heap)
    top_k_elements = []
    for _ in range(k):
        val, idx = heapq.heappop(max_heap)
        top_k_elements.append((val, idx))
    
    # Sort by index to get lexicographically smallest
    top_k_elements.sort(key=lambda x: x[1])
    return [-x[0] for x in top_k_elements]


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(m)]
    
    results = []
    for k, pos in queries:
        subseq = optimal_subsequence(a, k)
        results.append(subseq[pos - 1])
    
    for result in results:
        print(result)


# Call the solve function to read input and print output
solve()
