import math


def min_blocked_points(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    ans = 0
    for k in range(1, n+1):
        ans += 4 * (k-1) * 4**(k-1)
        if is_prime(k):
            ans -= 4 * (k-1) * 4**(k-1)
    return ans

n = int(input())
print(min_blocked_points(n))
