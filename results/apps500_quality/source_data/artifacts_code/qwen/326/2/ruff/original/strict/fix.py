import heapq
from collections import Counter


def min_cost_to_palindrome(N, S, C):
    # Count the frequency of each character in all strings
    char_count = Counter(''.join(S))

    # Identify characters that have odd frequencies
    odd_chars = [char for char, count in char_count.items() if count % 2 != 0]

    # If there are more than one character with odd frequency, it's impossible to form a palindrome
    if len(odd_chars) > 1:
        return -1

    # If there's exactly one character with an odd frequency, we need to use one string that contains this character
    if len(odd_chars) == 1:
        odd_char = odd_chars[0]
        min_cost = float('inf')
        for i in range(N):
            if odd_char in S[i]:
                min_cost = min(min_cost, C[i])
        if min_cost == float('inf'):
            return -1
        else:
            return min_cost

    # If all characters have even frequencies, we can use any subset of the strings to form a palindrome
    # We use a priority queue to always pick the cheapest string that can help form a palindrome
    pq = []
    for i in range(N):
        heapq.heappush(pq, (C[i], S[i]))

    total_cost = 0
    while len(pq) > 1:
        cost1, s1 = heapq.heappop(pq)
        cost2, s2 = heapq.heappop(pq)
        if s1 == s2[::-1]:
            total_cost += cost1
        else:
            heapq.heappush(pq, (cost2, s2))

    if pq:
        total_cost += pq[0][0]

    return total_cost

# Read input from standard input
N = int(input().strip())
S = []
C = []
for _ in range(N):
    s, c = input().strip().split()
    S.append(s)
    C.append(int(c))

# Print the minimum total cost needed to form a palindrome
print(min_cost_to_palindrome(N, S, C))
