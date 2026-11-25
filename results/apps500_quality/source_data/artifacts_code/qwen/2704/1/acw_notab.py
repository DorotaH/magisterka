from typing import List


def can_end_up_with_t(N: int, Q: int, A: List[int], queries: List[int]) -> List[str]:
    # If N is 1, the only possible value is the single element in the array
    if N == 1:
        return ["Yes" if a == t else "No" for t in queries]
    
    # If N is 2, the only possible values are the elements themselves and any number between them
    if N == 2:
        min_val, max_val = min(A), max(A)
        return ["Yes" if min_val <= t <= max_val else "No" for t in queries]
    
    # For N > 2, the array can end up with any number that is the sum of any two elements
    # This is because we can always find a way to pair elements and replace them with their sum
    return ["Yes" for _ in queries]


# Read input from standard input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
Q = int(data[1])
A = list(map(int, data[2:2 + N]))
queries = list(map(int, data[2 + N:]))

# Answer the queries
results = can_end_up_with_t(N, Q, A, queries)

# Print the results to standard output
for result in results:
    print(result)
