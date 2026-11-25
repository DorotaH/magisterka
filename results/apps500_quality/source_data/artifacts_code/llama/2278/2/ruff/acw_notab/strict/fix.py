

def read_ints():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str():
    return input()


def solve():
    a, b, m = read_ints()
    if a == b:
        print(1)
        print(a)
        return
    a, b = min(a, b), max(a, b)
    dp = [0] * (1 + b)
    dp[a] = 1
    for i in range(a + 1, 1 + b):
        if dp[i - 1] == 0:
            continue
        for j in range(1, min(i - 1, m) + 1):
            if j == i - 1:
                dp[i] = 1
            else:
                dp[i] += 1
    if dp[b] == 0:
        print(-1)
        return
    x, i = b, dp[b]
    sequence = [x]
    while x != a:
        x -= i - 1
        sequence.append(x)
        i -= 1
    sequence.reverse()
    print(len(sequence))
    print(*sequence)


q = read_int()
for _ in range(q):
    solve()
