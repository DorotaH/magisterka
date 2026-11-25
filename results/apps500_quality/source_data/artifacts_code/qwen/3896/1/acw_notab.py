MOD = 1000000007


def count_dance_pairs(x):
    n = len(x)
    count = 0
    ones = 0
    for i in range(n):
        if x[i] == '1':
            ones += 1
        count = (2 * count + ones) % MOD
    return count


x = input().strip()
result = count_dance_pairs(x)
print(result)
