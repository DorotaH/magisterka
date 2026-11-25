from collections import Counter


def count_prefixes(n, x, s):
    balance = 0
    count = Counter({0: 1})
    result = 0
    
    for i in range(n):
        balance += 1 if s[i] == '1' else -1
        if balance == x:
            result += count[balance]
        count[balance] += 1
    
    if balance == x:
        result += float('inf')
    
    return result

T = int(input())
results = []
for _ in range(T):
    n, x = map(int, input().split())
    s = input().strip()
    results.append(count_prefixes(n, x, s))

for result in results:
    if result == float('inf'):
        print(-1)
    else:
        print(result)
