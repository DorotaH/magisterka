
def  gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m=map(int, input().split())

if  m > n // 2 or  n == 1:
    print("Impossible")
    exit(0)

for i in range(1, n):
    for  j in  range(1 + i, n):
        if  gcd(i, j) == 1:
            m -= 1
            print(1 + i, 1 + j)
        if  m == 0:
            break

if not m > 0:
    print("Possible")
else:
    print("Impossible")
