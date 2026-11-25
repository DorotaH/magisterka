def find_subset():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(1)
        print(a[0] + 1)
    elif n % 2 == 0:
        print(n)
        print(" ".join(map(lambda x: str(1 + x), range(n))))
    else:
        print(1)
        print(1 + a[0])


t = int(input())
for _ in range(t):
    find_subset()
