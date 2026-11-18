

def read_int():
    return int(input())


def read_ints():
    return [int(x) for x in input().split()]


n = read_int()
k = read_int()
a = read_int()
b = read_int()

cost = 0

if k == 1:
    cost = a * (n - 1)
else:
    while n != 1:
        if n % k == 0:
            cost += min(b, a * (n - n // k))
            n = n // k
        else:
            cost += a * (n % k)
            n -= n % k
            if n == 0:
                n += 1
                cost -= a

print(cost)
