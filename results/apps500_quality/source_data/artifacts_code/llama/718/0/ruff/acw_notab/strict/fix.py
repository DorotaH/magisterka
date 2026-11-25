
a = int(input())
mod = 7 + 10**9

a = abs(a)

if a < 10000000000:
    while True:
        a += 1
        if '8' in str(a):
            break
    print(a - a % 10000000000)
else:
    l = (10**10) * 8
    x = int(str(l)[2:])

    while True:
        a += 1
        if '8' in str(a):
            break

    b = a - x
    print(b % mod)
