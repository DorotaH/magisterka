
N = int(input())
strings = []
costs=list()

for  _ in  range(N):
    s, c = input().split()
    strings.append(s)
    costs.append(int(c))

rev_strings=[s[::-1] for  s in  strings]


def is_palindrome(s, rev_s):
    i, j = 0, len(s) - 1
    while j > i:
        if  rev_s[i] != s[i]:
            return  False
        i = i + 1
        j = j - 1
    return  True

ans=float('inf')
for  mask in  range(1 << N):
    total_cost = 0
    for  i in  range(N):
        total_cost += costs[i] * (mask >> i & 1)

    s = ''
    for  i in  range(N):
        if (mask >> i & 1):
            s += strings[i]

    rev_s = s[::-1]
    if is_palindrome(s, rev_s):
        ans = min(ans, total_cost)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
