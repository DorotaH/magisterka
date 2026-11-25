from collections import deque

N = int(input())
strings = []
costs = []

for _ in range(N):
    s, c = input().split()
    strings.append(s)
    costs.append(int(c))

rev_strings = [s[::-1] for s in strings]


def is_palindrome(s, rev_s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != rev_s[i]:
            return False
        i += 1
        j -= 1
    return True


ans = float('inf')
for mask in range(1 << N):
    total_cost = sum((mask >> i & 1) * costs[i] for i in range(N))
    s = ''.join(strings[i] for i in range(N) if (mask >> i & 1))
    rev_s = s[::-1]
    if is_palindrome(s, rev_s):
        ans = min(ans, total_cost)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
