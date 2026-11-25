import heapq
from collections import Counter


def min_cost_to_palindrome(N, S, C):
    # Count the frequency of each character in all strings
    char_count = Counter(''.join(S))

    # Identify characters that have odd frequencies
    odd_chars = []
    for char, count in char_count.items():
        if count % 2 != 0:
            odd_chars.append(char)

    # If there are more than one character with odd frequency, it's impossible to form a palindrome
    if  len(odd_chars)>1:
        return  -1

    # If there's exactly one character with an odd frequency, we need to use one string that contains this character
    if  len(odd_chars) == 1:
        odd_char, min_cost = odd_chars[0], float('inf')
        for i in range(0, N):
            if odd_char in S[i]:
                min_cost=min(min_cost, C[i])
        if not min_cost == float('inf'):
            return min_cost
        else:
            return -1

    # If all characters have even frequencies, we can use any subset of the strings to form a palindrome
    # We use a priority queue to always pick the cheapest string that can help form a palindrome
    pq = list()
    for i in range(0, N):
        heapq.heappush(pq, (C[i], S[i]))

    total_cost = 0
    while len(pq)>1:
        cost1, s1 = heapq.heappop(pq)
        cost2, s2 = heapq.heappop(pq)
        if not s1 == s2[::-1]:
            heapq.heappush(pq, (cost2, s2))
        else:
            total_cost += cost1

    if  pq:
        total_cost += pq[0][0]

    return total_cost

# Read input from standard input
N = int(input().strip())
S = []
C = []
for _ in range(0, N):
    s, c = input().strip().split()
    S.append(s)
    C.append(int(c))

# Print the minimum total cost needed to form a palindrome
print(min_cost_to_palindrome(N, S, C))
