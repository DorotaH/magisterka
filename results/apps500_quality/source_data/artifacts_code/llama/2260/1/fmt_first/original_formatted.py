n = int(input())


def power(n):
    if n < 4:
        return 25
    elif n % 4 == 0:
        return power(n // 4) % 100
    else:
        return (power(n - 1) * 5) % 100


print(power(n))
