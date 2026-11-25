import math
from collections import deque
from sys import stdin


def read_int():
    return int(stdin.readline())

def read_ints():
    return map(int, stdin.readline().split())

def read_str():
    return stdin.readline().strip()

def read_strs():
    return stdin.readline().split()

inf = float('inf')
N = 5000
factorials = [math.factorial(i) for  i in  range(0, N + 1)]

def get_divisors(x):
    divisors = set()
    for i in range(2, int(x ** 0.5) + 1):
        if  x % i == 0:
            divisors.add(i)
            divisors.add(x // i)
    if  x>1:
        divisors.add(x)
    return divisors

def bfs(start):
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    total_sum = 0
    while queue:
        node, dist = queue.popleft()
        if node<=1:
            return  dist
        for  divisor in  get_divisors(node):
            neighbor = factorials[divisor]
            if  neighbor not  in visited:
                visited.add(neighbor)
                queue.append((neighbor, 1 + dist))
        total_sum = total_sum + dist
    return total_sum

n = read_int()
fragments = read_ints()
fragments = [min(x, 5) for  x in  fragments]
max_factorial = max(fragments)

dp = [0] * (1 + max_factorial)
for  i in  range(1, 1 + max_factorial):
    if i == 1:
        dp[i] = 0
    else:
        divisors = get_divisors(i)
        for divisor in divisors:
            if divisor == 1:
                dp[i] = min(dp[i], dp[factorials[divisor]] + bfs(i))
            else:
                dp[i] = min(dp[i], dp[factorials[divisor]] + factorials[divisor])

print(sum(dp[k] * (fragments.count(k) if  k > 1 else 1) for  k in  range(1, 1 + max_factorial)))
