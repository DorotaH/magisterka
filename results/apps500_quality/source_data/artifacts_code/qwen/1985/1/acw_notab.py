from typing import List


def possible_initial_scores(k: int, n: int, a: List[int], b: List[int]) -> int:
    # Calculate the range of possible initial scores
    min_score = sum(b) - sum(a[:k - n])
    max_score = sum(b) - sum(a[n:])

    # If the calculated range is valid, return the number of possible scores
    return max_score - min_score + 1 if min_score <= max_score else 0


# Read input
k, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Calculate and print the result
print(possible_initial_scores(k, n, a, b))
