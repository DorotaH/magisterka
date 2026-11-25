n = int(input())


def power(n):
    if 4 > n:
        return 25
    elif n % 4 == 0:
        return power(n // 4) % 100
    else:
        return (5 * power(n - 1)) % 100


print(power(n))
