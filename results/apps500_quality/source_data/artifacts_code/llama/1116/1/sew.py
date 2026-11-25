import sys
input = sys.stdin.readline

for _ in range(int(input())):
    r, b, k = map(int, input().split())

    if not r == b:
        lcm = (r * b) // math.gcd(r, b)
        if lcm <= k:
            print("REBEL")
        else:
            print("OBEY")
    else:
        print("REBEL")