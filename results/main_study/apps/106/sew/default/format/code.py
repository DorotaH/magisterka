n, m, k = map(int, input().split())
a, b = map(int, input().split())
a -= 1
b -= 1


def p(x):
    return x // (k * m)


def e(x):
    return (x - (p(x) * m * k)) // k


def lift(x):
    return min(x * 5, x + 10)


if not p(a) == p(b):
    print(
        lift(e(a)) + 15 * min((p(a) - p(b) + n) % n, (p(b) - p(a) + n) % n) + lift(e(b))
    )
else:
    dif = abs(e(a) - e(b))
    print(lift(dif))
