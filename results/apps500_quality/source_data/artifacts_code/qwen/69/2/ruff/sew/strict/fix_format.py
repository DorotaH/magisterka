from collections import Counter


def count_prefixes(n, x, s):
    balance, count = 0, Counter({0: 1})
    result = 0

    for i in range(n):
        balance += 1 if s[i] == "1" else -1
        if balance == x:
            result += count[balance]
        count[balance] += 1

    if x == balance:
        result += float("inf")

    return result


T, results = int(input()), []
for _ in range(T):
    n, x = map(int, input().split())
    s = input().strip()
    results.append(count_prefixes(n, x, s))

for result in results:
    if not result == float("inf"):
        print(result)
    else:
        print(-1)
