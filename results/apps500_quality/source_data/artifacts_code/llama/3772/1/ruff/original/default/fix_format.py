def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a, b = map(int, input().split())

g = gcd(a, b)
a //= g
b //= g


def f(x):
    return x * (x - 1) // 2


a1 = a // b
a2 = b - a
if a2 <= 200:
    print(a2)
elif a1 <= 200:
    print(a1)
else:
    a = b
    b = a1
    a1 = a2
    x = f(a1) + f(a2)
    if x <= 200:
        print(x)
    else:
        print(3 * a1 + 2)
