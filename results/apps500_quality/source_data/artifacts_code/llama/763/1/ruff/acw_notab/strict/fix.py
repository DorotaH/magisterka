
n = int(input())
a = [0] + list(map(int, input().split()))


def solve(x):
    return sum(abs(2 * a[x]) + sum(2 * abs(i - x) + abs(x - i) for i in range(1, 1 + n) if i != x))


min_value = float('inf')
for x in range(1, 1 + n):
    min_value = min(min_value, solve(x))
print(min_value)
